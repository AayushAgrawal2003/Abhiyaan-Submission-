#!/usr/bin/python3
import rospy
from std_msgs.msg import String


def callback(data):
    #setup a publisher

    pub = rospy.Publisher('naayihba_maet',String,queue_size=10) 
    val = ''.join(reversed(data.data))
    pub.publish(val)
    rospy.loginfo(val)


def listener():
    rospy.init_node('reverser' , anonymous = True)
    rospy.Subscriber('team_abhiyaan' , String , callback)
    rospy.spin()


if __name__ == '__main__':
    listener()

