import numpy as np
import math_tool

def state_muxer(t, p, q, v, w, N):
    state = np.zeros((N, 13))
    return t, state

def state_muxer(t, p, q, N):
    state = np.zeros((N,7))
    return t, state