#!/usr/bin/env python3.6
# coding=utf-8
#
# Programme permettant de tester la publication sur un topic ainsi qu'un calcul avec Pytorch
# donc test ROS + Pytorch (python3)
#
# Pour avoir ROS
import rospy
from std_msgs.msg import String

import torch

x = torch.empty(5, 3)
print(x)
try:
    pub = rospy.Publisher('torch', String, queue_size=10)
    rospy.init_node('test_torch', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        ch = str("pytorch OK")
        rospy.loginfo(ch)
        pub.publish(ch)
        rate.sleep()
except rospy.ROSInterruptException:
    pass
