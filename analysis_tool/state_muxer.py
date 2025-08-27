import numpy as np
import math_tool

def odom_muxer(t, p, q, v, w, N):
    state = np.zeros((N, 13))
    state[:,0:3] = p
    state[:,3:7] = q
    state[:,7:10] = v
    state[:,10:13] = w
    odom = {'time': t, 'data': state}
    return odom

def pose_muxer(t, p, q, N):
    state = np.zeros((N,7))
    state[:,0:3] = p
    state[:,3:7] = q
    pose = {'time': t, 'data': state}
    return pose