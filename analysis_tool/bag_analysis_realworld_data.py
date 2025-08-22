from bag_file_extractor import BagFileExtractor
from state_demuxer import state_demux, pose_demux
import matplotlib.pyplot as plt

if __name__ == '__main__':
    bag_folder_name = '../realworld_bag2/'

    topic_list = ['/eskf_state',
                   '/mocap_state']

    bag_extractor = BagFileExtractor(bag_folder_name)

    odom_eskf = bag_extractor.extract_odometry(topic_list[0])
    pose_mocap = bag_extractor.extract_odometry(topic_list[1])

    t_eskf, p_eskf, q_eskf, v_eskf, w_eskf = state_demux(odom_eskf, False)
    t_mocap, p_mocap, q_mocap, _,_ = state_demux(pose_mocap, False)
    temp_t0 = t_eskf[0]
    t_eskf = t_eskf - temp_t0
    t_mocap = t_mocap - temp_t0

    plt.figure(0)

    plt.subplot(3,1,1)
    plt.plot(t_eskf, p_eskf[:,0], label='eskf', color='limegreen')
    plt.plot(t_mocap, p_mocap[:,0], label='mocap', color='violet')
    plt.title('$p_x - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$p_x$ (m)')
    plt.legend(loc='center left', bbox_to_anchor=(1.05,0.5))
    plt.grid(True)

    plt.subplot(3,1,2)
    plt.plot(t_eskf, p_eskf[:,1], label='eskf', color='limegreen')
    plt.title('$p_y - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$p_y$ (m)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t_eskf, p_eskf[:,2], label='eskf', color='limegreen')
    plt.title('$p_z - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$p_z$ (m)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig('position.png', dpi=600)

    plt.figure(1)

    plt.subplot(4,1,1)
    plt.plot(t_eskf, q_eskf[:,0], label='eskf', color='limegreen')
    plt.title('$q_w - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$q_w$')
    plt.grid(True)
    plt.legend()

    plt.subplot(4,1,2)
    plt.plot(t_eskf, q_eskf[:,1], label='eskf', color='limegreen')
    plt.title('$q_x - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$q_x$')
    plt.grid(True)
    plt.legend()

    plt.subplot(4,1,3)
    plt.plot(t_eskf, q_eskf[:,2], label='eskf', color='limegreen')
    plt.title('$q_y - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$q_y$')
    plt.grid(True)
    plt.legend()

    plt.subplot(4,1,4)
    plt.plot(t_eskf, q_eskf[:,3], label='eskf', color='limegreen')
    plt.title('$q_z - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$q_z$')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('quaternion.png', dpi=600)

    plt.figure(2)

    plt.subplot(3,1,1)
    plt.plot(t_eskf, v_eskf[:,0], label='eskf', color='limegreen')
    plt.title('$v_x - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$v_x$ (m/s)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(t_eskf, v_eskf[:,1], label='eskf', color='limegreen')
    plt.title('$v_y - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$v_y$ (m/s)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t_eskf, v_eskf[:,2], label='eskf', color='limegreen')
    plt.title('$v_z - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$v_z$ (m/s)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig('linear_velocity.png', dpi=600)

    plt.figure(3)

    plt.subplot(3,1,1)
    plt.plot(t_eskf, w_eskf[:,0], label='eskf', color='limegreen')
    plt.title('$\omega_x - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$\omega_x$ (rad/s)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(t_eskf, w_eskf[:,1], label='eskf', color='limegreen')
    plt.title('$\omega_y - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$\omega_y$ (rad/s)')
    plt.grid(True)
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t_eskf, w_eskf[:,2], label='eskf', color='limegreen')
    plt.title('$\omega_z - t$')
    plt.xlabel('time (s)')
    plt.ylabel('$\omega_z$ (rad/s)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    # plt.savefig('angular_velocity.png', dpi=600)

    plt.show()