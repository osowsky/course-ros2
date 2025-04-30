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

class Add2IntsServerNode( Node ):
    def __init__( self ):
        super().__init__( "add_2_ints_server" )
        self.server_ = self.create_service( AddTwoInts, SERVICE_NAME,
                                            self.callback_add_2_ints )
        self.get_logger().info( "ADD2IntsServer has been started." )

    def callback_add_2_ints( self, request: AddTwoInts.Request,
                             response: AddTwoInts.Response ):
        response.sum = request.a + request.b
        self.get_logger().info( str( request.a ) + " + " + 
                               str( request.b ) +
                               " = " + str( response.sum ) )
        return response
    

def main( args = None ):
    rclpy.init( args = args )
    node = Add2IntsServerNode()
    rclpy.spin( node )
    rclpy.shutdown()


if __name__ == "__main__":
    main()
