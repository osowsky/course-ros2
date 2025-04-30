#!/usr/bin/env python3
#

import rclpy
from rclpy.node import Node

# ros2 interface show example_interfaces/msg/Int64
# int64.data <- name of the variable in int64 class. 
from example_interfaces.msg import Int64

MSG_BUF_SIZE = 10
PUB_FREQ = 1.0
TOPIC_NAME = "number"

# Comands to see the topic.
# ros2 topic list
# ros2 topic echo /${TOPIC_NAME}

class NumberPublisherNode( Node ):
    def __init__( self ):
        super().__init__( "number_publisher" )
        self.number_ = 10
        self.publisher_ = self.create_publisher( Int64, TOPIC_NAME,
                                                 MSG_BUF_SIZE )
        self.timer_ = self.create_timer( PUB_FREQ, self.publish )
        self.get_logger().info( "NumberPublisher has been started." )

    def publish( self ):
        msg = Int64()
        msg.data = self.number_
        self.publisher_.publish( msg )


def main( args = None ):
    rclpy.init( args = args )
    node = NumberPublisherNode()
    rclpy.spin( node )
    rclpy.shutdown()


if __name__ == "__main__":
    main()
