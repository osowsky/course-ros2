#include "rclcpp/rclcpp.hpp"
/*
# ros2 interface show example_interfaces/srv/AddTwoInts
# AddTwoInts.a <- name of the first op. 
# AddTwoInts.b <- name of the second op.
# AddTwoInts.sum <- response sum = a + b.
*/
#include "example_interfaces/srv/add_two_ints.hpp"

using namespace std::chrono_literals;
using namespace std::placeholders;

#define SERVICE_NAME "add_2_ints"

class Add2IntsClientNode : public rclcpp::Node
{
    public:
        Add2IntsClientNode() : Node( "add_2_ints_client" )
        {
            this->client_ = this->create_client<example_interfaces::srv::AddTwoInts>( SERVICE_NAME );
            RCLCPP_INFO( this->get_logger(), "Add2IntsClient has been started." );
        };

        void callAdd2Ints( int64_t a, int64_t b )
        {
            while( !this->client_->wait_for_service( 1s ) ) {
                RCLCPP_WARN( this->get_logger(), "Waiting for AddTwoInts server." );
            }

            auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
            request->a = a;
            request->b = b;
            this->client_->async_send_request( request,
                std::bind( &Add2IntsClientNode::callbackCallAdd2Ints, this, _1 ) );
        };

    private:
        rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedPtr client_;

        void callbackCallAdd2Ints( rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedFuture future )
        {
            auto response = future.get();
            RCLCPP_INFO( this->get_logger(), "%ld", response->sum );
        };
};

int main( int argc, char **argv )
{
    rclcpp::init( argc, argv );
    auto node = std::make_shared<Add2IntsClientNode>();
    node->callAdd2Ints( 1, 3 );
    node->callAdd2Ints( -3, 3 );
    node->callAdd2Ints( -1, -3 );
    rclcpp::spin( node );
    rclcpp::shutdown();
    return 0;
};
