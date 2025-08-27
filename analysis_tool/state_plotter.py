import numpy as np
import math_tool
import matplotlib.pyplot as plt

class StatePlotter:
    def __init__(self, t_mocap, state_mocap, t_eskf, state_eskf):

        self.t_mocap = t_mocap
        self.t_eskf = t_eskf
        self.state_eskf = state_eskf
        self.state_mocap = state_mocap
