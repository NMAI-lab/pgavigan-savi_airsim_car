#!/usr/bin/env python

# Translates lka steering to perceptions for savi

# @author: Patrick Gavigan
# @date: 17 Mar 2020

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64


# Callback function for translating the messages and sending them along
def lkaSteeringReceiver(data, publisher):
    angleString = str(data.data)
    message = str("lkaSteering(" + angleString + ")")
    rospy.loginfo("Perception: " + message)
    publisher.publish(message)


# Main method for this node, sets up the callback for the lka/steering receiver
# as well as the publisher for the perceptions to be sent to.
def lkaTranslator():
    rospy.init_node('lkaTranslator', anonymous=True)
    
    # Setup the publisher
    perceptionPublisher = rospy.Publisher('perceptions', String, queue_size=10)
    
    # Setup the subscribers
    rospy.Subscriber('lka/steering', Float64, lkaSteeringReceiver, perceptionPublisher)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        lkaTranslator()
    except rospy.ROSInterruptException:
        pass
