from bag_file_extractor import BagFileExtractor
from state_demuxer import state_demux
from state_muxer import odom_muxer, pose_muxer
import matplotlib.pyplot as plt
import math_tool

if __name__ == '__main__':
    bag_folder_name = '../realworld_bag/'

    topic_list = ['/eskf/Odom',
                   '/mocap/Odom']

    bag_extractor = BagFileExtractor(bag_folder_name)

    odom_eskf = bag_extractor.extract_odometry(topic_list[0])
    pose_mocap = bag_extractor.extract_odometry(topic_list[1])

    t_eskf, p_eskf, q_eskf, v_eskf, w_eskf = state_demux(odom_eskf, False)
    t_mocap, p_mocap, q_mocap, _, _ = state_demux(pose_mocap, False)
    temp_t0 = t_eskf[0]
    t_eskf = t_eskf - temp_t0
    t_mocap = t_mocap - temp_t0

    N1 = len(t_eskf)
    N2 = len(t_mocap)

    N = N1 if N1 <= N2 else N2

    odom_eskf = odom_muxer(t_eskf, p_eskf, q_eskf, v_eskf, w_eskf, N)
    pose_mocap = pose_muxer(t_mocap, p_mocap, q_mocap, N)