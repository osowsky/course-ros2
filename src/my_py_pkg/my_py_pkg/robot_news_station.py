#!/usr/bin/env python3
#

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
# ros2 interface show example_interfaces/msg/String
# string.data <- name of the variable in string class. 

MSG_BUF_SIZE = 10
PUB_FREQ = 0.5
TOPIC_NAME = "robot_news"

# Comands to see the topic.
# ros2 topic list
# ros2 topic echo /${TOPIC_NAME}

class RobotNewsStationNode( Node ):
    def __init__( self ):
        super().__init__( "robot_news_station" )
        self.robot_name_ = "C3P0"
        self.publisher_ = self.create_publisher( String, TOPIC_NAME,
                                                 MSG_BUF_SIZE )
        self.timer_ = self.create_timer( PUB_FREQ, self.publish )
        self.get_logger().info( "RobotNewsStation has been started." )

    def publish( self ):
        msg = String()
        msg.data = "Hi, this is " + self.robot_name_ + " from the RNStation."
        self.publisher_.publish( msg )


def main( args = None ):
    rclpy.init( args = args )
    node = RobotNewsStationNode()
    rclpy.spin( node )
    rclpy.shutdown()


if __name__ == "__main__":
    main()
