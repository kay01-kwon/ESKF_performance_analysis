import numpy as np
import math_tool
from state_demuxer import state_demux, pose_demux
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


class StatePlotter:
    def __init__(self, pose_mocap, odom_eskf, transparency):

        t_mocap, p_mocap, q_mocap = pose_demux(pose_mocap)
        t_eskf, p_eskf, q_eskf, v_eskf, w_eskf = state_demux(odom_eskf)

        # The total number of messages
        self.N = len(t_mocap)

        self.t_mocap = t_mocap
        print(len(t_mocap))
        self.t_vmocap = t_mocap[0:len(t_mocap)-1]
        self.p_mocap = p_mocap
        self.q_mocap = q_mocap

        self.t_eskf = t_eskf
        self.p_eskf = p_eskf
        self.q_eskf = q_eskf
        self.v_eskf = v_eskf
        self.w_eskf = w_eskf

        self.v_mocap = self.compute_velocity_from_p_mocap()
        self.w_mocap = self.compute_w_from_q_mocap()

        self.transparency = transparency

    def plot_pos_group(self):
        fig = plt.figure(0)
        ax_list = []
        for idx in range(3):
            ax_temp = self.plot_pos(fig, idx)
            ax_list.append(ax_temp)
        plt.tight_layout()

    def plot_quat_group(self):
        fig = plt.figure(1)
        ax_list = []
        for idx in range(4):
            ax_temp = self.plot_quat(fig, idx)
            ax_list.append(ax_temp)
        plt.tight_layout()

    def plot_vel_group(self):
        fig = plt.figure(2)
        ax_list = []
        for idx in range(3):
            ax_temp = self.plot_vel(fig, idx)
            ax_list.append(ax_temp)
        plt.tight_layout()

    def plot_angular_vel_group(self):
        fig = plt.figure(3)
        ax_list = []
        for idx in range(3):
            ax_temp = self.plot_angular_vel(fig, idx)
            ax_list.append(ax_temp)
        plt.tight_layout()

    def plot_timestep(self):
        fig = plt.figure(6)
        ax = fig.add_subplot(1,1,1)
        dt_mocap = np.diff(self.t_mocap)
        t_tmocap = self.t_mocap[0:len(self.t_mocap)-1]
        ax.plot(t_tmocap, dt_mocap)

    def plot_pos(self, fig, idx):
        ax = fig.add_subplot(3,1,idx+1)

        # Plot mocap position data
        # idx 0:x, 1:y, 2:z
        ax.plot(self.t_mocap, self.p_mocap[:,idx],
                 color='orangered', linewidth=2,
                 label='mocap')
        # Plot eskf position data
        ax.plot(self.t_eskf, self.p_eskf[:,idx],
                 color='blue', linewidth=2,
                 alpha=self.transparency, label='eskf')

        if idx == 0:
            title_name= '$p_{x} - t$'
            y_label_name = '$p_{x} (m)$'
        elif idx == 1:
            title_name ='$p_{y} - t$'
            y_label_name = '$p_{y} (m)$'
        else:
            title_name ='$p_{z} - t$'
            y_label_name = '$p_{z} (m)$'

        self.set_title_label(ax, title_name, y_label_name)

        return ax

    def plot_quat(self, fig, idx):
        ax = fig.add_subplot(4,1,idx+1)

        ax.plot(self.t_mocap, self.q_mocap[:,idx],
                color='orangered', linewidth=2,
                label='mocap')

        ax.plot(self.t_eskf, self.q_eskf[:,idx],
                color='blue', linewidth=2,
                alpha=self.transparency, label='eskf')

        if idx == 0:
            title_name= '$q_{w} - t$'
            y_label_name = '$q_{w}$'
        elif idx == 1:
            title_name ='$q_{x} - t$'
            y_label_name = '$q_{x}$'
        elif idx == 2:
            title_name ='$q_{y} - t$'
            y_label_name = '$q_{y}$'
        else:
            title_name = '$q_{z} - t$'
            y_label_name = '$q_{z}$'

        self.set_title_label(ax, title_name, y_label_name)

        return ax

    def plot_vel(self, fig, idx):
        ax = fig.add_subplot(3,1,idx+1)
        ax.plot(self.t_vmocap, self.v_mocap[:,idx],
                color='orangered', linewidth=2,
                label='mocap')

        ax.plot(self.t_eskf, self.v_eskf[:,idx],
                color='blue', linewidth=2,
                alpha=self.transparency, label='eskf')

        if idx == 0:
            title_name= '$v_{x} - t$'
            y_label_name = '$v_{x} (m/s)$'
        elif idx == 1:
            title_name ='$v_{y} - t$'
            y_label_name = '$v_{y} (m/s)$'
        else:
            title_name ='$v_{z} - t$'
            y_label_name = '$v_{z} (m/s)$'

        self.set_title_label(ax, title_name, y_label_name)

    def plot_angular_vel(self, fig, idx):
        ax = fig.add_subplot(3,1,idx+1)
        ax.plot(self.t_vmocap, self.w_mocap[:,idx],
                 color='orangered', linewidth=2,
                 label='mocap')
        # Plot eskf position data
        ax.plot(self.t_eskf, self.w_eskf[:,idx],
                 color='blue', linewidth=2,
                 alpha=self.transparency, label='eskf')


        if idx == 0:
            title_name= '$\omega_{x} - t$'
            y_label_name = '$\omega_{x} (rad/s)$'
        elif idx == 1:
            title_name ='$\omega_{y} - t$'
            y_label_name = '$\omega_{y} (rad/s)$'
        else:
            title_name ='$\omega_{z} - t$'
            y_label_name = '$\omega_{z} (rad/s)$'

        self.set_title_label(ax, title_name, y_label_name)

        return ax

    def set_title_label(self, ax, title_name, y_label_name):
        ax.set_title(title_name)
        ax.set_xlabel('t (s)')
        ax.set_ylabel(y_label_name)

        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        ax.grid(True)

    def compute_velocity_from_p_mocap(self):
        dt_mocap = np.diff(self.t_mocap)
        N = len(dt_mocap)

        vx_lpf, vy_lpf, vz_lpf = 0, 0, 0

        v_mocap = np.zeros((N,3))

        alpha = 0.97

        for i in range(N):
            dt = dt_mocap[i]
            vx = (self.p_mocap[i+1, 0] - self.p_mocap[i, 0])/dt
            vy = (self.p_mocap[i+1, 1] - self.p_mocap[i, 1]) / dt
            vz = (self.p_mocap[i+1, 2] - self.p_mocap[i, 2]) / dt

            vx_lpf = alpha*vx_lpf + (1-alpha) * vx
            vy_lpf = alpha * vy_lpf + (1 - alpha) * vy
            vz_lpf = alpha * vz_lpf + (1 - alpha) * vz
            v_mocap[i,0] = vx_lpf
            v_mocap[i,1] = vy_lpf
            v_mocap[i,2] = vz_lpf

        return v_mocap

    def compute_w_from_q_mocap(self):
        dt_mocap = np.diff(self.t_mocap)
        N = len(dt_mocap)

        wx_lpf, wy_lpf, wz_lpf = 0, 0, 0

        w_mocap = np.zeros((N,3))
        alpha = 0.97
        for i in range(N):
            dt = dt_mocap[i]
            q_curr = self.q_mocap[i,:]
            q_next = self.q_mocap[i+1,:]
            w_curr = self.compute_angle_axis_vec(q_curr, q_next)/dt
            wx_lpf = alpha*wx_lpf + (1-alpha)*w_curr[0]
            wy_lpf = alpha*wy_lpf + (1-alpha)*w_curr[1]
            wz_lpf = alpha*wz_lpf + (1-alpha)*w_curr[2]

            w_mocap[i,0] = wx_lpf
            w_mocap[i,1] = wy_lpf
            w_mocap[i,2] = wz_lpf

        return w_mocap

    def plot_show(self):
        plt.show()

    def plot_savefig(self, filename='figure.png', dpi = 600):
        plt.savefig(filename, dpi=dpi)
    def compute_angle_axis_vec(self, q_curr, q_next):
        q_curr_conj = math_tool.conjugate(q_curr)
        del_q = math_tool.otimes(q_curr_conj, q_next)
        theta = (math_tool.
                 quaternion_to_angle_axis_vec(del_q))
        return theta