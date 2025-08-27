import numpy as np

def odom_muxer(t, p, q, v, w, N):
    time = t[0:N]
    state = np.zeros((N, 13))
    state[:,0:3] = p[0:N,:]
    state[:,3:7] = q[0:N,:]
    state[:,7:10] = v[0:N,:]
    state[:,10:13] = w[0:N,:]
    odom = {'time': time, 'data': state}
    return odom

def pose_muxer(t, p, q, N):
    time = t[0:N]
    state = np.zeros((N,7))
    state[:,0:3] = p[0:N,:]
    state[:,3:7] = q[0:N,:]
    pose = {'time': time, 'data': state}
    return pose