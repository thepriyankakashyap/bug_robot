#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan


def clbk_laser(msg):
    regions = [
        # min(min(msg.ranges[270:306]), 5),
        # min(min(msg.ranges[307:342]), 5),
        # min(min(msg.ranges[0:18]), min(msg.ranges[343:359]), 5),
        # min(min(msg.ranges[19:54]), 5),
        # min(min(msg.ranges[55:90]), 5),
        min(min(msg.ranges[0:143]), 10),
        min(min(msg.ranges[144:287]), 10),
        min(min(msg.ranges[288:431]), 10),
        min(min(msg.ranges[432:575]), 10),
        min(min(msg.ranges[576:719]), 10),
        # msg.ranges[0],
        # msg.ranges[89],
        # msg.ranges[179],
        # msg.ranges[269],
        # msg.ranges[359],
        # min(msg.ranges[0], 5)
        # min(min(msg.ranges[0:89]), 5),
        # min(min(msg.ranges[90:179]), 5),
        # min(min(msg.ranges[180:269]), 5),
        # min(min(msg.ranges[270:359]), 5),
        # min(msg.ranges[359])
    ]
    rospy.loginfo(regions)


def main():
    rospy.init_node('reading_laser')
    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)
    rospy.spin()


if __name__ == '__main__':
    main()
