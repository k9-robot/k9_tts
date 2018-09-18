cmake_minimum_required(VERSION 2.8.3)
project(k9_tts)


find_package(catkin REQUIRED
  rospy
  std_msgs
  message_generation
)



add_message_files(
  FILES
  tts.msg
)

add_service_files(
  FILES
  Say.srv
)

generate_messages(
  DEPENDENCIES
   std_msgs
)

catkin_package(

)

include_directories(
)

