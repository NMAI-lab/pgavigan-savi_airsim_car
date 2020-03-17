#!/usr/bin/env python

# Demonstration program of the savi_ros_bdi system

# Created on Wed Feb 19 16:17:21 2020
# @author: Patrick Gavigan

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

def lkaSteeringReceiver(data, publisher):
    angleString = str(data.data)
    message = str("lkaSteering(" + angleString + ")")
    publisher.publish(message)
    


# Callback function for action messages.
# Message is pritned to the console logs
def actionReceiver(data): 
    message = str(rospy.get_caller_id() + 'I heard: ' + str(data.data))
    rospy.loginfo(message)



# Demo program that publishes perceptions and inbox messages and listens to 
# outobx and action messages
def saviTranslator():
    rospy.init_node('demoSaviTranslator', anonymous=True)
    
    # Setup the publishers
    perceptionPublisher = rospy.Publisher('perceptions', String, queue_size=10)
    
    # Setup the subscribers
    rospy.Subscriber('lka/steering', Float64, lkaSteeringReceiver, perceptionPublisher)
    rospy.Subscriber('actions', String, actionReceiver)

 
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        
        # Publish the perception
        message = "time(%s)" % rospy.get_time()
        rospy.loginfo("I said: " + message)
        perceptionPublisher.publish(message)

        # Delay until next cycle
        rate.sleep()


if __name__ == '__main__':
    try:
        saviTranslator()
    except rospy.ROSInterruptException:
        pass
