#! /usr/bin/env python  
import rospy  
from std_msgs.msg import Int32,Float32

def a_callback(data): 

    global a 

    a=data.data 

    #print(a) 

def b_callback(data): 

    global b 

    b=data.data 

 
 
 

if __name__=='__main__': 

    rospy.init_node("c_node") 

    rospy.Subscriber("a", Int32, a_callback) 

    rospy.Subscriber("b", Int32, b_callback)  

    pub = rospy.Publisher("c", Float32, queue_size=10) #topic (abc)
 
    r = rospy.Rate(10) # 10hz

    a=0 

    b=0 

    sum=0 

    while not rospy.is_shutdown(): 

        sum=a+b 

        print(sum)

        pub.publish(sum)

        r.sleep()