#!/usr/bin/env python

# Translates brake to perceptions for savi

# @author: Patrick Gavigan
# @date: 17 Mar 2020

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


# Callback function for translating the messages and sending them along
def brakeReceiver(data, publisher):
    brakeString = str(data.data)
    message = str("brake(" + brakeString + ")")
    rospy.loginfo("Perception: " + message)
    publisher.publish(message)


# Main method for this node, sets up the callback for the acc/throttle receiver
# as well as the publisher for the perceptions to be sent to.
def brakeTranslator():
    rospy.init_node('brakeTranslator', anonymous=True)
    
    # Setup the publisher
    perceptionPublisher = rospy.Publisher('perceptions', String, queue_size=10)
    
    # Setup the subscribers
    rospy.Subscriber('acc/brake', Float64, brakeReceiver, perceptionPublisher)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        brakeTranslator()
    except rospy.ROSInterruptException:
        pass
