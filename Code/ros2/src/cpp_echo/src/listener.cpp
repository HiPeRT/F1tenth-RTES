#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

class Listener : public rclcpp::Node
{
    public:
    Listener()
    : Node("listener")
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>("topic_echo", 10);

        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "topic", 10, std::bind(&Listener::listener_callback, this, _1));
    }
    
    private:
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;

    void listener_callback(const std_msgs::msg::String::SharedPtr msg)
    {
        if (msg->data == "exit")
        {
            rclcpp::shutdown();
            return;
        }

        RCLCPP_INFO(this->get_logger(), "I heard: %d Bytes", msg->data.length());

        auto message = std_msgs::msg::String();
        message.data = msg->data;
        publisher_->publish(message);
        // RCLCPP_INFO(this->get_logger(), "Publishing: \"%s\"", message.data.c_str());
    }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Listener>());
    rclcpp::shutdown();
    return 0;
}
