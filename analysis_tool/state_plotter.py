import numpy as np
import math_tool
import matplotlib.pyplot as plt

class StatePlotter:
    def __init__(self, t_mocap, state_mocap, t_eskf, state_eskf):

        self.t_mocap = t_mocap
        self.t_eskf = t_eskf
        self.state_eskf = state_eskf
        self.state_mocap = state_mocap

    def compute_angle_axis_vec(self, q1, q2):
        q1_conj = math_tool.conjugate(q1)
        del_q = math_tool.otimes(q1_conj, q2)
        theta = (math_tool.
                 quaternion_to_angle_axis_vec(del_q))
        return theta
