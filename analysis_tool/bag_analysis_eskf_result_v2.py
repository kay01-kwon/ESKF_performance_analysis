import matplotlib.pyplot as plt

from bag_file_extractor import BagFileExtractor
from state_demuxer import state_demux, pose_demux
from state_muxer import odom_muxer, pose_muxer
from state_plotter import StatePlotter

if __name__ == '__main__':
    bag_folder_name = '../realworld_bag/'

    topic_list = ['/mocap/JetsonPlatform/pose','/eskf/Odom']

    bag_extractor = BagFileExtractor(bag_folder_name)


    pose_mocap = bag_extractor.extract_pose(topic_list[0])
    odom_eskf = bag_extractor.extract_odometry(topic_list[1])

    t_mocap, p_mocap, q_mocap = pose_demux(pose_mocap)
    t_eskf, p_eskf, q_eskf, v_eskf, w_eskf = state_demux(odom_eskf, False)
    temp_t0 = t_eskf[0]
    t_eskf = t_eskf - temp_t0
    t_mocap = t_mocap - temp_t0

    N1 = len(t_eskf)
    N2 = len(t_mocap)

    N = N1 if N1 <= N2 else N2

    pose_mocap = pose_muxer(t_mocap, p_mocap, q_mocap, N)
    odom_eskf = odom_muxer(t_eskf, p_eskf, q_eskf, v_eskf, w_eskf, N)

    state_plotter_obj = StatePlotter(pose_mocap, odom_eskf)

    state_plotter_obj.plot_pos_group()

    state_plotter_obj.plot_quat_group()

    state_plotter_obj.plot_vel_group()
    state_plotter_obj.plot_savefig('linear_velocity.png',600)

    state_plotter_obj.plot_angular_vel_group()
    state_plotter_obj.plot_savefig('angular_velocity.png',600)

    # state_plotter_obj.plot_timestep()

    state_plotter_obj.plot_show()

