#! /usr/bin/env python

import rospy 
from sensor_msgs.msg import LaserScan

def callback(msg):
	#rospy.loginfo(msg)
	laser_values = [
		min(min(msg.ranges[0:143]),10),
		min(min(msg.ranges[144:287]),10),
		min(min(msg.ranges[288:431]),10),
		min(min(msg.ranges[432:575]),10),
		min(min(msg.ranges[576:719]),10)
	]

	rospy.loginfo(laser_values)

def main():
	rospy.init_node("laser_read")

	sub = rospy.Subscriber('/scan', LaserScan, callback)

	rospy.spin()

if __name__ == '__main__':
	main()
