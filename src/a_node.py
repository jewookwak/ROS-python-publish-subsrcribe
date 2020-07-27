#! /usr/bin/env python  
import rospy  
from std_msgs.msg import Int32  
if __name__=='__main__': 

    rospy.init_node("a_node") 

    pub = rospy.Publisher("a", Int32, queue_size=10) #topic (abc)  

    r = rospy.Rate(10) # 10hz 

    while not rospy.is_shutdown(): 

        a=1 

        pub.publish(a) 

        r.sleep()