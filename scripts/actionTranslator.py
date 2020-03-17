#!/usr/bin/env python

# Translates action messages to various topics for controlling the car

# @author: Patrick Gavigan
# @date: 17 Mar 2020

import rospy
import re
from std_msgs.msg import String
from std_msgs.msg import Float64


# Callback function for translating the messages and sending them along
def actionReceiver(data, publishers):
    (steeringPublisher, throttlePublisher, brakePublisher) = publishers

    message = data.data
    rospy.loginfo("Recived command: " + message)
    
    parameter = re.search(r'\((.*?)\)',message).group(1)
    command = message.split('(')[0]
    
    toSend = Float64()
    toSend.data = float(parameter)
    
    if command == "steering":
        rospy.loginfo("Steering command sent: " + str(parameter))
        
        steeringPublisher.publish(toSend)
    elif command == "throttle":
        throttlePublisher.publish(toSend)
    elif command == "brake":
        brakePublisher.publish(toSend)
    else:
        rospy.info("Unknown command received, no action taken")


# Main method for this node, sets up the callback for the action translator
# as well as the publishers for all the relevant nodes that commands need to be
# sent to.
def actionTranslator():
    rospy.init_node('actionTranslator', anonymous=True)
    
    # Setup the publishers
    steeringPublisher = rospy.Publisher('/control/steering', Float64, queue_size=1)
    throttlePublisher = rospy.Publisher('/control/throttle', Float64, queue_size=1)
    brakePublisher = rospy.Publisher('/control/brake', Float64, queue_size=1)
    
    publishers = (steeringPublisher, throttlePublisher, brakePublisher)
    
    # Setup the subscriber
    rospy.Subscriber('actions', String, actionReceiver, publishers)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

# Launch the program
if __name__ == '__main__':
    try:
        actionTranslator()
    except rospy.ROSInterruptException:
        pass
