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

    temp_t0 = t_true[0]
    t_true = t_true - temp_t0
    t_eskf = t_eskf - temp_t0

    plt.figure(0)

    plt.subplot(3,1,1)
    plt.plot(t_eskf, p_eskf[:,0], label='eskf', color='limegreen')
    plt.plot(t_true, p_true[:,0], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$p_x - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$p_x$ (m)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(t_eskf, p_eskf[:,1], label='eskf', color='limegreen')
    plt.plot(t_true, p_true[:,1], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$p_y - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$p_y$ (m)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t_eskf, p_eskf[:,2], label='eskf', color='limegreen')
    plt.plot(t_true, p_true[:,2], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$p_z - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$p_z$ (m)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    plt.figure(1)

    plt.subplot(4,1,1)
    plt.plot(t_eskf, q_eskf[:,0], label='eskf', color='limegreen')
    plt.plot(t_true, q_true[:,0], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$q_w - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$q_w$')
    plt.grid(True)
    plt.legend()

    plt.subplot(4,1,2)
    plt.plot(t_eskf, q_eskf[:,1], label='eskf', color='limegreen')
    plt.plot(t_true, q_true[:,1], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$q_x - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$q_x$')
    plt.grid(True)
    plt.legend()

    plt.subplot(4,1,3)
    plt.plot(t_eskf, q_eskf[:,2], label='eskf', color='limegreen')
    plt.plot(t_true, q_true[:,2], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$q_y - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$q_y$')
    plt.grid(True)
    plt.legend()

    plt.subplot(4,1,4)
    plt.plot(t_eskf, q_eskf[:,3], label='eskf', color='limegreen')
    plt.plot(t_true, q_true[:,3], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$q_z - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$q_z$')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()

    plt.figure(2)

    plt.subplot(3,1,1)
    plt.plot(t_eskf, v_eskf[:,0], label='eskf', color='limegreen')
    plt.plot(t_true, v_true[:,0], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$v_x - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$v_x$ (m/s)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(t_eskf, v_eskf[:,1], label='eskf', color='limegreen')
    plt.plot(t_true, v_true[:,1], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$v_y - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$v_y$ (m/s)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t_eskf, v_eskf[:,2], label='eskf', color='limegreen')
    plt.plot(t_true, v_true[:,2], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$v_z - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$v_z$ (m/s)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    plt.figure(3)

    plt.subplot(3,1,1)
    plt.plot(t_eskf, w_eskf[:,0], label='eskf', color='limegreen')
    plt.plot(t_true, w_true[:,0], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$\omega_x - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$\omega_x$ (rad/s)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(t_eskf, w_eskf[:,1], label='eskf', color='limegreen')
    plt.plot(t_true, w_true[:,1], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$\omega_y - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$\omega_y$ (rad/s)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t_eskf, w_eskf[:,2], label='eskf', color='limegreen')
    plt.plot(t_true, w_true[:,2], '--', linewidth=1.8, label='true', color='violet')
    plt.title('$\omega_z - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$\omega_z$ (rad/s)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()

    plt.show()