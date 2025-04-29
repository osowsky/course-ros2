#include "rclcpp/rclcpp.hpp"

// ros2 interface show example_interfaces/msg/String
// string.data <- name of the variable in string class. 
#include "example_interfaces/msg/string.hpp"

using namespace std::placeholders;

#define MSG_BUF_SIZE 10
#define TOPIC_NAME "robot_news"

class SmartphoneNode : public rclcpp::Node
{
    public:
        SmartphoneNode() : Node( "smartphone" )
        {
            this->subscriber_  = this->create_subscription<example_interfaces::msg::String>( TOPIC_NAME,
                                MSG_BUF_SIZE,
                                std::bind( &SmartphoneNode::callbackRobotNews, this,
                                _1 ) );  // If using namescape std::placeholders.
                                // std::placeholders::_1 ) );
            RCLCPP_INFO( this->get_logger(), "Smartphone has been started." );
        };

    private:
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;

        void callbackRobotNews( const example_interfaces::msg::String::SharedPtr msg )
        {
            RCLCPP_INFO( this->get_logger(), "%s", msg->data.c_str() );
        };
};

int main( int argc, char **argv )
{
    rclcpp::init( argc, argv );
    auto node = std::make_shared<SmartphoneNode>();
    rclcpp::spin( node );
    rclcpp::shutdown();
    return 0;
};
