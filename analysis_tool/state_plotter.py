import numpy as np
import math_tool
from state_demuxer import state_demux, pose_demux
import matplotlib.pyplot as plt

class StatePlotter:
    def __init__(self, pose_mocap, odom_eskf):

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

    def plot_timestep(self):
        fig = plt.figure(6)
        ax = fig.add_subplot(1,1,1)
        dt_mocap = np.diff(self.t_mocap)
        t_tmocap = self.t_mocap[0:len(self.t_mocap)-1]
        ax.plot(t_tmocap, dt_mocap)

    def plot_show(self):
        plt.show()

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
                 linestyle='--', label='eskf')

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
                linestyle='--', label='eskf')

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
                linestyle='--', label='eskf')

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


    def set_title_label(self, ax, title_name, y_label_name):
        ax.set_title(title_name)
        ax.set_xlabel('t (s)')
        ax.set_ylabel(y_label_name)

        ax.legend()
        ax.grid(True)

    def compute_velocity_from_p_mocap(self):

        dt_mocap = np.diff(self.t_mocap[:])

        N = len(dt_mocap)

        delx = np.diff(self.p_mocap[:,0])
        dely = np.diff(self.p_mocap[:,1])
        delz = np.diff(self.p_mocap[:,2])

        vx = np.zeros((N,))
        vy = np.zeros((N,))
        vz = np.zeros((N,))

        v_mocap = np.zeros((N,3))

        for i in range(N):

            if dt_mocap[i] < 0.002:
                dt = 0.010
            else:
                dt = dt_mocap[i]
            vx[i] = delx[i]/dt
            vy[i] = dely[i]/dt
            vz[i] = delz[i]/dt

        v_mocap[:,0] = vx
        v_mocap[:,1] = vy
        v_mocap[:,2] = vz

        return v_mocap
    def compute_angle_axis_vec(self, q1, q2):
        q1_conj = math_tool.conjugate(q1)
        del_q = math_tool.otimes(q1_conj, q2)
        theta = (math_tool.
                 quaternion_to_angle_axis_vec(del_q))
        return theta