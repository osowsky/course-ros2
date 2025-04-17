#!/usr/bin/env python3
#

import rclpy
from rclpy.node import Node

class MyNode( Node ):
    def __init__( self ):
        super().__init__( "py_test" )
        self.counter_ = 0
        self.get_logger().info( "Hello, world!" )
        self.create_timer( 1.0, self.timer_callback )

    def timer_callback( self ):
        self.get_logger().info( "Hello! [ " + str( self.counter_ ) + " ]" )
        self.counter_ += 1

def main( args=None ):
    rclpy.init( args=args )

    # node = Node( "py_test" )                  # No OOP
    # node.get_logger().info( "Hello, world!" ) # No OOP
    node = MyNode() # OOP

    rclpy.spin( node ) # keep the node alive.
    rclpy.shutdown()

if __name__ == "__main__":
    main()
