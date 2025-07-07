cmake_minimum_required(VERSION 3.10)
project(com_piler)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(
    common
    token
    lex
    test
)

file(GLOB SOURCES
    main.cpp
    lex/lex.cpp
    test/test.cpp
    token/token.cpp
)

add_executable(com_piler ${SOURCES}) 