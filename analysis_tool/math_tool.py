import numpy as np

def quat_to_rotm(q):
    qw, qx, qy, qz = q[0], q[1], q[2], q[3]
    
    rotm = np.array([
        [1 - 2 * (qy * qy + qz * qz), 2 * (qx * qy - qw * qz), 2 * (qx * qz + qw * qy)],
        [2 * (qy * qx + qw * qz), 1 - 2 * (qx * qx + qz * qz), 2 * (qy * qz - qw * qx)],
        [2 * (qz * qx - qw * qy), 2 * (qz * qy + qw * qx), 1 - 2 * (qx * qx + qy * qy)]
    ])
    
    return rotm
