#include <chrono>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

#include "rclcpp/clock.hpp"
#include <cmath>
#include <ctime>
#include <unistd.h>

using namespace std::chrono_literals;

class Talker : public rclcpp::Node
{
    public:
    Talker()
    : Node("talker"), count_(1)
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);

        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "topic_echo", 10, std::bind(&Talker::listener_callback, this, _1));

        timer_ = this->create_wall_timer(
            500ms, std::bind(&Talker::sender_callback, this));

        clk_ = new rclcpp::Clock();
    }
    
    private:
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    size_t count_;

    rclcpp::Clock *clk_;
    rcl_time_point_value_t now_;

    std::chrono::duration<long int, std::ratio<1, 1000000000> > nowUnix_;
    
    void sender_callback()
    {
        timer_->cancel();
        auto message = std_msgs::msg::String();
        message.data = "";

        for (size_t i=0; i<(2 * count_); i++)
            message.data.append("a");

        // Get timestap with rclpy
        rclcpp::Time time = clk_->now();
        now_ = time.nanoseconds();
        //RCLCPP_INFO(this->get_logger(), "[RCLPY] Current time for %s: %lld", message.data.c_str(), now_);

        // Get timestamp with UNIX
        nowUnix_ = std::chrono::system_clock::now().time_since_epoch();
        //RCLCPP_INFO(this->get_logger(), "[UNIX] Current time for %s: %lld", message.data.c_str(), nowUnix_.count());

        publisher_->publish(message);
        //RCLCPP_INFO(this->get_logger(), "Publishing: \"%s\"", message.data.c_str());
        count_++;
    }

    void listener_callback(const std_msgs::msg::String::SharedPtr msg)
    {
        //RCLCPP_INFO(this->get_logger(), "I heard: \"%s\"", msg->data.c_str());

        // Get timestamp with rclpy
        rcl_time_point_value_t now = clk_->now().nanoseconds();
        //RCLCPP_INFO(this->get_logger(), "[RCLPY] Current time for %s: %lld", msg->data.c_str(), now);
        
        // Get timestamp with UNIX
        auto nowUnix = std::chrono::system_clock::now().time_since_epoch();
        //RCLCPP_INFO(this->get_logger(), "[UNIX] Current time for %s: %lld", msg->data.c_str(), nowUnix.count());

        std::cout << "[RCLPY] " << msg->data.length() << " " << now - now_ << std::endl;
        std::cout << "[UNIX] " << msg->data.length() << " " << nowUnix.count() - nowUnix_.count() << std::endl;
        
        if (count_ <= 400)
            this->sender_callback();
        else
        {
            auto msg = std_msgs::msg::String();
            msg.data = "exit";
            publisher_->publish(msg);
            sleep(1);
            rclcpp::shutdown();
            return;
        }
    }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Talker>());
    rclcpp::shutdown();
    return 0;
}
