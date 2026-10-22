# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target learning_interface::learning_interface
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${learning_interface_TARGETS}.
if(learning_interface_TARGETS AND NOT TARGET learning_interface::learning_interface)
  add_library(learning_interface::learning_interface INTERFACE IMPORTED)
  set_target_properties(learning_interface::learning_interface PROPERTIES
    INTERFACE_LINK_LIBRARIES "${learning_interface_TARGETS}")
endif()
