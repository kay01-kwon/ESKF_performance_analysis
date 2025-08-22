import os, fnmatch
import rosbag
import numpy as np

class BagFileExtractor():
    def __init__(self, bag_file_folder_name):

        self.bag_file_folder_name = bag_file_folder_name

        file_list = self.find_files()
        print(file_list)
        self.bag = rosbag.Bag( bag_file_folder_name + '/' +file_list[0])


    def find_files(self):
        file_names = []
        for root, dirs, files in os.walk(self.bag_file_folder_name):
            for name in files:
                if fnmatch.fnmatch(name, '*.bag'):
                    file_names.append(name)
                    print(name)
        return file_names

    def count_messages(self, topic_name):
        num_message = self.bag.get_message_count(topic_name)
        return num_message

    def extract_odometry(self, topic_name):

        N_count = self.count_messages(topic_name)

        odom_time = np.zeros((N_count,1))
        odom_data = np.zeros((N_count,13))

        idx = 0
        for topic, msg, time in self.bag.read_messages(topics=[topic_name]):
            odom_time[idx] = (time.to_time())
            odom_data[idx,:] = [msg.pose.pose.position.x,
                                msg.pose.pose.position.y,
                                msg.pose.pose.position.z,
                                msg.pose.pose.orientation.w,
                                msg.pose.pose.orientation.x,
                                msg.pose.pose.orientation.y,
                                msg.pose.pose.orientation.z,
                                msg.twist.twist.linear.x,
                                msg.twist.twist.linear.y,
                                msg.twist.twist.linear.z,
                                msg.twist.twist.angular.x,
                                msg.twist.twist.angular.y,
                                msg.twist.twist.angular.z]
            idx = idx + 1
        odom_dict = {'time': odom_time, 'data':odom_data}
        return odom_dict

    def extract_pose(self, topic_name):

        N_count = self.count_messages(topic_name)

        pose_time = np.zeros((N_count,1))
        pose_data = np.zeros((N_count,7))

        idx = 0
        for topic, msg, time in self.bag.read_messages([topic_name]):
            pose_time[idx] = (time.to_time())
            pose_data[idx,:] = [msg.pose.position.x,
                                msg.pose.position.y,
                                msg.pose.position.z,
                                msg.pose.orientation.w,
                                msg.pose.orientation.x,
                                msg.pose.orientation.y,
                                msg.pose.orientation.z]
            idx = idx + 1
        pose_dict = {'time': pose_time, 'data':pose_data}
        return pose_dict