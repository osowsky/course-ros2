#!/usr/bin/env python3
#

import rclpy
from rclpy.node import Node

# ros2 interface show example_interfaces/srv/AddTwoInts
# AddTwoInts.a <- name of the first op. 
# AddTwoInts.b <- name of the second op.
# AddTwoInts.sum <- response sum = a + b.
from example_interfaces.srv import AddTwoInts

SERVICE_NAME = "add_2_ints"

def main( args = None ):
    rclpy.init( args = args )
    node = Node( "add_2_ints_client_no_oop" )
    node.get_logger().info( "ADD2IntsClient has been started." )

    client = node.create_client( AddTwoInts, SERVICE_NAME )
    while not client.wait_for_service( 1.0 ):
        node.get_logger().warn( "Waiting for AddTwoInts server." )

    request = AddTwoInts.Request()
    request.a = 3
    request.b = 8

    future = client.call_async( request )
    rclpy.spin_until_future_complete( node, future )
    response: AddTwoInts.Response = future.result()
    node.get_logger().info( str( request.a ) + " + " + 
                            str( request.b ) +
                            " = " + str( response.sum ) )

    rclpy.shutdown()


if __name__ == "__main__":
    main()
