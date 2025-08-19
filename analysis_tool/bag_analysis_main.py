from bag_file_extractor import BagFileExtractor

if __name__ == '__main__':
    bag_folder_name = '../simulation_bag/'

    topic_list = ['/custom_hexacopter/ground_truth/odometry',
                   '/eskf_state',
                   '/mocap/pose']

    bag_extractor = BagFileExtractor(bag_folder_name)

    odom_true = bag_extractor.extract_odometry(topic_list[0])
    odom_eskf = bag_extractor.extract_odometry(topic_list[1])
    pose_mocap = bag_extractor.extract_pose(topic_list[2])

