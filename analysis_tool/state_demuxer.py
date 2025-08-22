import numpy as np
from math_tool import quat_to_rotm

def state_demux(odom, frame_transform_required = False):
    t = odom['time']
    data = odom['data']

    N = len(data)
    p = np.zeros((N,3))
    q = np.zeros((N,4))
    v = np.zeros((N,3))
    w = np.zeros((N,3))

    for i in range(N):
        p[i,:] = data[i, 0:3]
        q[i,:] = data[i, 3:7]
        v[i,:] = data[i, 7:10]
        w[i,:] = data[i, 10:13]
        
        if frame_transform_required == True:
            rotm = quat_to_rotm(q[i,:])
            v[i,:] = rotm @ v[i,:]
            
    return t, p, q, v, w

def pose_demux(pose):
    t = pose['time']
    data = pose['data']

    N = len(data)
    p = np.zeros((N,3))
    q = np.zeros((N,4))

    return t, p, q