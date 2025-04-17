#!/usr/bin/env python3
#

import rclpy
from rclpy.node import Node

def main( args=None ):
    rclpy.init( args=args )
    node = Node( "py_test" )
    node.get_logger().info( "Hello, world!" )
    rclpy.spin( node ) # keep the node alive.
    rclpy.shutdown()

if __name__ == "__main__":
    main()
