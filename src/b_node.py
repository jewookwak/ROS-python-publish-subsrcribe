#! /usr/bin/env python  
import rospy  
from std_msgs.msg import Int32 
if __name__=='__main__': 

    rospy.init_node("b_node") 

    pub = rospy.Publisher("b", Int32, queue_size=10) #topic (abc)  

    r = rospy.Rate(10) # 10hz 

    while not rospy.is_shutdown(): 

        b=5 

        pub.publish(b) 

        r.sleep()  