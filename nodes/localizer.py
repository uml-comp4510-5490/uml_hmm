#!/usr/bin/env python

################################################################################
##
## Programmer: Victoria Albanese
## Date: September 28, 2017
## Filename: localizer.cpp
##
## Description: This file enables the robot to localize itself in a given 
## environment using a histogram filter.
##
################################################################################

#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
import rospy
from std_msgs import String
from geometry_msgs import Twist

import helper_functions
import robot_class

import sys
import os
import numpy as np

FORWARD  =  4.0
BACKWARD = -4.0

def main():
    # verify that commandline arguments are all there
    if not len(sys.argv) is 2:
        print "Usage: rosrun pset4_localization_victoria_albanese localize.py <+ or ->"
        print "\t +: start with positive velocity (travel right)"
        print "\t -: start with negative velocity (travel left)"
        exit()
    
    # set velocity from commandline argument
    vel = 0.0
    if sys.argv[1] == "+":
        velocity = FORWARD
    elif sys.argv[1] == "-":
        velocity = BACKWARD
    else:
        print "\nUsage: rosrun pset4_localization_victoria_albanese localize <+ or ->", sys.argv[1], "\n"
        print "\t +: start with positive velocity (travel right)"
        print "\t -: start with negative velocity (travel left)"
        exit()
    
    # initialize node and create the node handle
    rospy.init_node('controller', anonymous=True)
    
    # make a new robot
    robot = Robot()
    
    # setup a publisher and its loop rateee
    pub = rospy.Publisher('robot/cmd_vel', Twist, 1000)
    rate = rospy.Rate(10)
    
    # get a sensor reading
    rospy.Subscriber("robot/wall_door_sensor", 1000, Robot.callback, robot)
    #ros::SpinOnce()
    
    # make two histograms, one for measurement, one to hold intermediate movement step
    size = 600
    histogram_measurement = [None] * 600
    histrogram_movement = [None] * 600
    total_probability = 0.0
    
    # initialize the two arrays
    for i in range(0, size):
        histogram_measurement[i] = 1.0 / float(size)
        histogram_movement[i] = 0.0
    
    
    # do the stuff
    while not rospy.is_shutdown():
        ## YOUR CODE GOES HERE
        ## implement the histogram/grid localization method 
        ## Table 8.1 on page 238 of your textbook
        ## "Godspeed my friends" - Victoria
        ## "Abandon hope all ye who enter here" - James
        
        # spin and sleep
        rate.sleep()
    
    
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

################################################################################

