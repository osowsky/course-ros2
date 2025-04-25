#include "rclcpp/rclcpp.hpp"

// ros2 interface show example_interfaces/msg/String
// string.data <- name of the variable in string class. 
#include "example_interfaces/msg/string.hpp"

using namespace std::chrono_literals;

#define MSG_BUF_SIZE 10
#define PUB_FREQ 0.5s
#define TOPIC_NAME "robot_news"

/*
 * Comands to see the topic.
 * ros2 topic list
 * ros2 topic echo /${TOPIC_NAME}
*/

class RobotNewsStationNode : public rclcpp::Node
{
    public:
        RobotNewsStationNode() : Node( "robot_news_station" ), robot_name_( "R2D2" )
        {
            this->publisher_ = this->create_publisher<example_interfaces::msg::String>(  TOPIC_NAME, MSG_BUF_SIZE );
            this->timer_ = this->create_wall_timer( PUB_FREQ,
                                                    std::bind( &RobotNewsStationNode::publishNews, this ) );
            RCLCPP_INFO( this->get_logger(), "RobotNewsStation has been started." );
        };

    private:
        std::string robot_name_;
        rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
        rclcpp::TimerBase::SharedPtr timer_;

        void publishNews( void )
        {
            auto msg = example_interfaces::msg::String();
            msg.data = std::string( "Hi, this is " ) + this->robot_name_ + std::string( " from the RNStation." );
            this->publisher_->publish( msg );
        };
};

int main( int argc, char **argv )
{
    rclcpp::init( argc, argv );
    auto node = std::make_shared<RobotNewsStationNode>();
    rclcpp::spin( node );
    rclcpp::shutdown();
    return 0;
};
