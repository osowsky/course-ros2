#!/usr/bin/env python3
#

import rclpy
from rclpy.node import Node

# ros2 interface show example_interfaces/msg/Int64
# int64.data <- name of the variable in int64 class. 
from example_interfaces.msg import Int64

MSG_BUF_SIZE = 10
PUB_FREQ = 1.0
TOPIC_NAME_SUB = "number"
TOPIC_NAME_PUB = "number_count"

# Comands to see the topic.
# ros2 topic list
# ros2 topic echo /${TOPIC_NAME}

class NumberCounterNode( Node ):
    def __init__( self ):
        super().__init__( "number_counter" )
        self.number_ = 0
        self.publisher_ = self.create_publisher( Int64, TOPIC_NAME_PUB,
                                                 MSG_BUF_SIZE )
        self.subscriber_ = self.create_subscription( Int64, TOPIC_NAME_SUB,
                                                     self.callback_number,
                                                     MSG_BUF_SIZE )
        # self.timer_ = self.create_timer( PUB_FREQ, self.publish )
        self.get_logger().info( "NumberCounter has been started." )

    # def publish( self ):
    #     msg = Int64()
    #     msg.data = self.number_counter_
    #     self.publisher_.publish( msg )

    def callback_number( self, msg: Int64 ):
        self.get_logger().info( str( msg.data ) )
        self.number_+= msg.data
        msg_pub = Int64()
        msg_pub.data = self.number_
        self.publisher_.publish( msg_pub )


def main( args = None ):
    rclpy.init( args = args )
    node = NumberCounterNode()
    rclpy.spin( node )
    rclpy.shutdown()


if __name__ == "__main__":
    main()
