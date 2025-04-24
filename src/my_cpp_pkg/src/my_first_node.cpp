// RCL means ROS Client Library.
// DDS means Data Distributed Service.

#include "rclcpp/rclcpp.hpp"

class MyNode : public rclcpp::Node
{
    public:
        MyNode() : Node( "cpp_test" ), counter_( 0 )
        {
            RCLCPP_INFO( this->get_logger(), "Hello, world!" );
            this->timer_ = this->create_wall_timer( std::chrono::seconds( 1 ),
                                                    std::bind( &MyNode::timerCallback, this ) );
        };

    private:
        void timerCallback()
        {
            RCLCPP_INFO( this->get_logger(), "Hello! [ %02d ]", this->counter_ );
            this->counter_++;
        };
        rclcpp::TimerBase::SharedPtr timer_;
        int counter_;
};

int main( int argc, char **argv )
{
    rclcpp::init( argc, argv );

    // No OOP.
    // auto node = std::make_shared<rclcpp::Node>( "cpp_test" ); // Shared pointers.
    // RCLCPP_INFO( node->get_logger(), "Hello, world!" );
    auto node = std::make_shared<MyNode>(); // Shared pointers.

    rclcpp::spin( node ); // keep the node alive.
    rclcpp::shutdown();
    return 0;
};
