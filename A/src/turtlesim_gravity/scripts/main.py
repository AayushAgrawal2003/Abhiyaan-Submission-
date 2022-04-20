#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PKG = 'turtlesim_gravity'
import roslib; roslib.load_manifest(PKG)
import math
import numpy

rot1 = Twist()
rot2 = Twist()
G = 1
M = 1
x1,y1,x2,y2= 0,0,5,5
def callback1(data):
    global x1,y1
    x1 = data.x
    y1 = data.y
def callback2(data):
    global x2,y2
    x2 = data.x
    y2 = data.y
    
    
def move():
    global x1,y1,x2,y2
    rospy.Subscriber("two/pose", Pose,callback2)
    rospy.Subscriber("one/pose", Pose,callback1)
    s1 = (x2-x1)
    s2 = (y2-y1) 
    h = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    sin =  s2/h
    cos =  s1/h

    #thetad = math.degrees(theta)
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    vel = math.sqrt(G*M/distance) 
    rot1.linear.x = vel * cos
    rot1.linear.y = vel * sin
    rot2.linear.x = - vel * cos
    rot2.linear.y = - vel * sin
    rospy.loginfo(vel * sin)
    rospy.loginfo(vel * cos)
    
rospy.init_node('turtle_bot')

pub2 = rospy.Publisher('two/cmd_vel', Twist ,queue_size = 1)
pub1 = rospy.Publisher('one/cmd_vel', Twist ,queue_size = 1)
rate = rospy.Rate(10)







while not rospy.is_shutdown():
    move()
    pub1.publish(rot1)
    pub2.publish(rot2)
    rate.sleep()