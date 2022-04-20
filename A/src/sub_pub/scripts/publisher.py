#!/usr/bin/python3
import rospy
from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('team_abhiyaan', String, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(0.5) 
    while not rospy.is_shutdown():
        hello_str = "Team Abhiyaan rocks:" 
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass