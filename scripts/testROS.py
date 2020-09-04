#!/usr/bin/env python3.6
#
# Programme permettant de tester la publication sur un topic d'une info calculée par Akida
# donc test ROS + Akida (python3)
#
# Pour avoir ROS
import rospy
from std_msgs.msg import String

import numpy as np
from tensorflow.keras.utils import get_file
from tensorflow.keras.datasets import mnist

# Akida specific imports
from akida import Model


# Retrieve MNIST dataset
(train_set, train_label), (test_set, test_label) = mnist.load_data()

# Add a dimension to images sets as akida expects 4 dimensions inputs
train_set = np.expand_dims(train_set, -1)
test_set = np.expand_dims(test_set, -1)

# Load pre-trained MNIST model
model_file = get_file("gxnor_mnist.fbz",
                   "http://data.brainchip.com/models/gxnor/gxnor_mnist.fbz",
                   cache_subdir='models/gxnor')
model = Model(model_file)

# Test the first image of the test set
sample_image = 0
image = test_set[sample_image]
labels = model.predict(image.reshape(1,28,28,1))
print(labels[0])
assert labels[0] == test_label[sample_image]
try:
    pub = rospy.Publisher('mnist', String, queue_size=10)
    rospy.init_node('akida', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        ch = str(labels[0])
        rospy.loginfo(ch)
        pub.publish(ch)
        rate.sleep()
except rospy.ROSInterruptException:
    pass
