cmake_minimum_required(VERSION 3.15)
project(hello_world VERSION 1.0.0 LANGUAGES CXX)

# Enable testing if option enabled
include(CTest)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Use Conan dependencies
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Add main library
add_library(hello_world src/hello_world.cpp include/hello_world.h)

target_include_directories(hello_world PUBLIC include)

# Link libraries from Conan
target_link_libraries(hello_world ${CONAN_LIBS})

# Add test executable if testing enabled
if(ENABLE_TESTING)
    enable_testing()
    add_executable(hello_world_unit tests/hello_world_unit.cpp)
    target_link_libraries(hello_world_unit hello_world ${CONAN_LIBS} gtest_main)
    add_test(NAME hello_world_test COMMAND hello_world_unit)
endif()
