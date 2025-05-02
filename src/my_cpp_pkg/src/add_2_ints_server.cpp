#include "rclcpp/rclcpp.hpp"
/*
# ros2 interface show example_interfaces/srv/AddTwoInts
# AddTwoInts.a <- name of the first op. 
# AddTwoInts.b <- name of the second op.
# AddTwoInts.sum <- response sum = a + b.
*/
#include "example_interfaces/srv/add_two_ints.hpp"

// using namespace std::placeholders;

#define SERVICE_NAME "add_2_ints"

class Add2IntsServerNode : public rclcpp::Node
{
    public:
        Add2IntsServerNode() : Node( "add_2_ints_server" )
        {
            this->server_ = this->create_service<example_interfaces::srv::AddTwoInts>( SERVICE_NAME,
                                                std::bind( &Add2IntsServerNode::callbackAdd2Ints, this,
                                                std::placeholders::_1, std::placeholders::_2 ) );
            RCLCPP_INFO( this->get_logger(), "Add2IntsServer has been started." );
        };

    private:
        rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr server_;

        void callbackAdd2Ints( const example_interfaces::srv::AddTwoInts::Request::SharedPtr request,
                               const example_interfaces::srv::AddTwoInts::Response::SharedPtr response )
        {
            response->sum = request->a + request->b;
            RCLCPP_INFO( this->get_logger(), "%ld + %ld = %ld",
                         request->a, request->b, response->sum );
        };
};

int main( int argc, char **argv )
{
    rclcpp::init( argc, argv );
    auto node = std::make_shared<Add2IntsServerNode>();
    rclcpp::spin( node );
    rclcpp::shutdown();
    return 0;
};
