from bag_file_extractor import BagFileExtractor
from state_demuxer import state_demux
import matplotlib.pyplot as plt

if __name__ == '__main__':
    bag_folder_name = '../simulation_bag/'

    topic_list = ['/custom_hexacopter/ground_truth/odometry',
                   '/eskf_state',
                   '/mocap/pose']

    bag_extractor = BagFileExtractor(bag_folder_name)

    odom_true = bag_extractor.extract_odometry(topic_list[0])
    odom_eskf = bag_extractor.extract_odometry(topic_list[1])
    pose_mocap = bag_extractor.extract_pose(topic_list[2])

    t_true, p_true, q_true, v_true, w_true = state_demux(odom_true, True)
    t_eskf, p_eskf, q_eskf, v_eskf, w_eskf = state_demux(odom_eskf, False)

    plt.figure(0)
    plt.plot(t_eskf, v_eskf[:,0], label='eskf')
    plt.plot(t_true, v_true[:,0], label='true')
    plt.legend()

    plt.figure(1)
    plt.plot(t_eskf, p_eskf[:,0], label='eskf')
    plt.plot(t_true, p_true[:,0], label='true')
    plt.legend()
    
    plt.show()