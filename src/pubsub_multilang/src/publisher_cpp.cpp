#include <chrono>
#include <memory>
#include <string>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

class PublisherCpp : public rclcpp::Node {
public:
  PublisherCpp() : Node("publisher_cpp_node"), count_(0) {
    publisher_ = this->create_publisher<std_msgs::msg::String>("/chatter_topic", 10);
    timer_ = this->create_wall_timer(
      1000ms, std::bind(&PublisherCpp::timer_callback, this));
    RCLCPP_INFO(this->get_logger(), "Publisher C++ iniciado.");
  }

private:
  void timer_callback() {
    auto message = std_msgs::msg::String();
    message.data = "[CPP Publisher] Mensaje #" + std::to_string(count_++);
    RCLCPP_INFO(this->get_logger(), "Publicando: '%s'", message.data.c_str());
    publisher_->publish(message);
  }

  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char * argv[]) {
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<PublisherCpp>());
  rclcpp::shutdown();
  return 0;
}
