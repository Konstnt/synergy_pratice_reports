cmake_minimum_required(VERSION 3.14)
project(UnitTest_Case_4)

# Устанавливаем стандарт C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Подключаем заголовочные файлы проекта
include_directories(${PROJECT_SOURCE_DIR}/include)

# Подключаем GoogleTest из thirdparty
add_subdirectory(thirdparty/googletest)

# Создаём исполняемый файл для тестов
add_executable(runner tests/all_tests.cpp)

# Линкуем библиотеки GoogleTest
target_link_libraries(runner PRIVATE GTest::gtest_main)

# Если нужно включить флаги для работы с потоками
target_compile_options(runner PRIVATE -pthread)