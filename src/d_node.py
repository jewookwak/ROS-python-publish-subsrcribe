#! /usr/bin/env python  

import rospy  
from std_msgs.msg import Float32 , Int32

 


def sum_callback(data): 

    global sum
    sum=data.data 

 
 

if __name__=='__main__': 

    rospy.init_node("d_node") 

    rospy.Subscriber("c", Float32, sum_callback) 

    sum = 0

    d = 0

    while not rospy.is_shutdown(): 

        print(sum) 