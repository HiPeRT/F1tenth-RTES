cmake_minimum_required(VERSION 3.5)
project(cpp_echo)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(client src/client_member_function.cpp)
ament_target_dependencies(client rclcpp std_msgs)

add_executable(server src/server_member_function.cpp)
ament_target_dependencies(server rclcpp std_msgs)

install(TARGETS
  client
  server
  DESTINATION lib/${PROJECT_NAME})

ament_package()
