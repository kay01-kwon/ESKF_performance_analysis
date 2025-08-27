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
        self.p_mocap = p_mocap
        self.q_mocap = q_mocap

        self.t_eskf = t_eskf
        self.p_eskf = p_eskf
        self.q_eskf = q_eskf
        self.v_eskf = v_eskf
        self.w_eskf = w_eskf

    def plot_position(self):
        fig = plt.figure(0)

        ax1 = fig.add_subplot(3,1,1)

        ax1.plot(self.t_mocap, self.p_mocap[:,0],
                 color='orangered', linewidth=2,
                 label='mocap')

        ax1.plot(self.t_eskf, self.p_eskf[:,0],
                 color='blue', linewidth=2,
                 linestyle='--', label='eskf')

        ax1.title('$p_{x} - t$')
        ax1.set_xlabel('t (s)')
        ax1.set_ylabel('$p_{x} (m)$')

        ax1.legend()
        ax1.grid(True)

        plt.show()



    def compute_angle_axis_vec(self, q1, q2):
        q1_conj = math_tool.conjugate(q1)
        del_q = math_tool.otimes(q1_conj, q2)
        theta = (math_tool.
                 quaternion_to_angle_axis_vec(del_q))
        return theta