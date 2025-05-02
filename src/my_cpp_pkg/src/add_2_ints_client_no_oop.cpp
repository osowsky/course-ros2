#include "rclcpp/rclcpp.hpp"
/*
# ros2 interface show example_interfaces/srv/AddTwoInts
# AddTwoInts.a <- name of the first op. 
# AddTwoInts.b <- name of the second op.
# AddTwoInts.sum <- response sum = a + b.
*/
#include "example_interfaces/srv/add_two_ints.hpp"

// using namespace std::chrono_literals;

#define SERVICE_NAME "add_2_ints"

int main( int argc, char **argv )
{
    rclcpp::init( argc, argv );
    auto node = std::make_shared<rclcpp::Node>( "add_2_ints_client_no_oop" );

    auto client = node->create_client<example_interfaces::srv::AddTwoInts>( SERVICE_NAME );
    while( !client->wait_for_service( std::chrono::seconds( 1 ) ) ) {
        RCLCPP_WARN( node->get_logger(), "Waiting for AddTwoInts server." );
    }

    auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
    request->a = 3;
    request->b = -1;

    auto future = client->async_send_request( request );
    rclcpp::spin_until_future_complete( node, future );

    auto response =  future.get();
    RCLCPP_INFO( node->get_logger(), "%ld + %ld = %ld",
                 request->a, request->b, response->sum );

    rclcpp::shutdown();
    return 0;
};
