from bag_file_extractor import BagFileExtractor
from state_demuxer import state_demux, pose_demux
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    bag_folder_name = '../realworld_bag_mocap_only3/'

    topic_list = ['/mocap/JetsonPlatform/pose']

    bag_extractor = BagFileExtractor(bag_folder_name)

    pose_mocap = bag_extractor.extract_pose(topic_list[0])

    t_mocap, p_mocap, q_mocap = pose_demux(pose_mocap)
    temp_t0 = t_mocap[0]

    t_mocap = t_mocap - temp_t0

    dt = np.diff(t_mocap.squeeze())
    dt = dt*1000
    N = len(dt)

    print(temp_t0)

    dt_avg = np.mean(dt)
    dt_avg_array = np.ones((N,1))*dt_avg
    dt_std = np.std(dt)

    dt_max = np.max(dt)
    dt_min = np.min(dt)

    print('dt_avg:', dt_avg)
    print('dt_max:', dt_max)
    print('dt_min:', dt_min)
    print('dt_avg:', dt_avg)
    print('dt_std:', dt_std)

    idx = np.arange(1, N+1)

    plt.figure(0)

    plt.plot(idx,dt)
    plt.plot(idx, dt_avg_array, color='limegreen', linewidth=2)
    plt.grid(True)
    plt.title('Mocap dt (ms)')
    plt.xlabel('Sequence')
    plt.ylabel('dt (ms)')
    plt.savefig(bag_folder_name+'time_step.png',dpi=600)
    plt.show()

    # plt.figure(0)
    #
    # plt.subplot(3,1,1)
    # plt.plot(t_mocap, p_mocap[:,0], label='mocap', color='violet')
    # plt.title('$p_x - t$')
    # plt.xlabel('time (s)')
    # plt.ylabel('$p_x$ (m)')
    # plt.legend(loc='center left', bbox_to_anchor=(1.05,0.5))
    # plt.grid(True)
    #
    # plt.subplot(3,1,2)
    # plt.plot(t_mocap, p_mocap[:,1], label='eskf', color='limegreen')
    # plt.title('$p_y - t$')
    # plt.xlabel('time (s)')
    # plt.ylabel('$p_y$ (m)')
    # plt.grid(True)
    # plt.legend()
    #
    # plt.subplot(3,1,3)
    # plt.plot(t_mocap, p_mocap[:,2], label='eskf', color='limegreen')
    # plt.title('$p_z - t$')
    # plt.xlabel('time (s)')
    # plt.ylabel('$p_z$ (m)')
    # plt.grid(True)
    # plt.legend()
    #
    # plt.tight_layout()
    # # plt.savefig('position.png', dpi=600)
    #
    #
    # plt.show()