#!/usr/bin/env python3
#

import rclpy
from rclpy.node import Node

# ros2 interface show example_interfaces/msg/String
# string.data <- name of the variable in string class. 
from example_interfaces.msg import String

MSG_BUF_SIZE = 10
TOPIC_NAME = "robot_news"

class SmartphoneNode( Node ):
    def __init__( self ):
        super().__init__( "smartphone" )
        self.subscriber_ = self.create_subscription( String, TOPIC_NAME,
                                                     self.callback_robot_news,
                                                     MSG_BUF_SIZE )
        self.get_logger().info( "Smartphone has been started." )

    def callback_robot_news( self, msg: String ):
        self.get_logger().info( msg.data )

def main( args = None ):
    rclpy.init( args = args )
    node = SmartphoneNode()
    rclpy.spin( node )
    rclpy.shutdown()


if __name__ == "__main__":
    main()
