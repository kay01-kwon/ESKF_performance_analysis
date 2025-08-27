import numpy as np
from numpy import linalg

def quat_to_rotm(q):
    qw, qx, qy, qz = q[0], q[1], q[2], q[3]
    
    rotm = np.array([
        [1 - 2 * (qy * qy + qz * qz), 2 * (qx * qy - qw * qz), 2 * (qx * qz + qw * qy)],
        [2 * (qy * qx + qw * qz), 1 - 2 * (qx * qx + qz * qz), 2 * (qy * qz - qw * qx)],
        [2 * (qz * qx - qw * qy), 2 * (qz * qy + qw * qx), 1 - 2 * (qx * qx + qy * qy)]
    ])
    
    return rotm

def otimes(q1, q2):
    qw, qx, qy, qz = q1[0], q1[1], q1[2], q1[3]
    q1L_mat = np.array([[qw, -qx, -qy, -qz],
                        [qx, qw, -qz, qy],
                        [qy, qz, qw, -qx],
                        [qz, -qy, qx, qw]])
    return q1L_mat @ q2

def conjugate(q):
    qw, qx, qy, qz = q[0], q[1], q[2], q[3]
    q_conj = np.array([qw, -qx, -qy, -qz])
    return q_conj

def quaternion_to_angle_axis_vec(q):
    qw, qx, qy, qz = q[0], q[1], q[2], q[3]
    q_vec = np.array([qx, qy, qz])
    q_vec_norm = linalg.norm(q_vec,2)
    angle = np.atan2(q_vec_norm, qw)

    if angle < 1e-30:
        axis_vec = np.zeros((3,))
    else:
        axis_vec = q_vec/angle

    theta = angle*axis_vec
    return theta
