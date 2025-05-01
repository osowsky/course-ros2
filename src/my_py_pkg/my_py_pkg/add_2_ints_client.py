#!/usr/bin/env python3
#

import rclpy
from rclpy.node import Node
from rclpy.task import Future

# ros2 interface show example_interfaces/srv/AddTwoInts
# AddTwoInts.a <- name of the first op. 
# AddTwoInts.b <- name of the second op.
# AddTwoInts.sum <- response sum = a + b.
from example_interfaces.srv import AddTwoInts
from functools import partial 

SERVICE_NAME = "add_2_ints"

class Add2IntsClientNode( Node ):
    def __init__( self ):
        super().__init__( "add_2_ints_client" )
        self.client_ = self.create_client( AddTwoInts, SERVICE_NAME )
        self.get_logger().info( "ADD2IntsClient has been started." )

    def call_add_2_ints( self, a, b ):
        while not self.client_.wait_for_service( 1.0 ):
            self.get_logger().warn( "Waiting for AddTwoInts server." )
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = self.client_.call_async( request )
        future.add_done_callback( 
            partial( self.callback_call_add_2_ints, request=request ) )

    def callback_call_add_2_ints( self, future: Future,
                                  request: AddTwoInts.Request ):
        response: AddTwoInts.Response = future.result()
        self.get_logger().info( str( request.a ) + " + " + 
                                str( request.b ) +
                                " = " + str( response.sum ) )


def main( args = None ):
    rclpy.init( args = args )
    node = Add2IntsClientNode()
    node.call_add_2_ints( 2, 7 )
    node.call_add_2_ints( -2, 2 )
    node.call_add_2_ints( -4, 10 )

    rclpy.spin( node )
    rclpy.shutdown()


if __name__ == "__main__":
    main()
