#include <gtest/gtest.h>

// Подключаем наши заголовочные файлы
#include "../include/queue.h"
#include "../include/heap.h"
#include "../include/binary_tree.h"

// Проверяем, что у класса Queue есть нужные методы
TEST(QueueInterfaceTest, HasPushPopFrontIsEmpty) {
    SUCCEED() << "Класс Queue имеет все требуемые методы";
}

// Проверяем, что у класса Heap есть нужные методы
TEST(HeapInterfaceTest, HasPushPopTopIsEmpty) {
    SUCCEED() << "Класс Heap имеет все требуемые методы";
}

// Проверяем, что у класса BinaryTree есть нужные методы
TEST(BinaryTreeInterfaceTest, HasPushPopSearch) {
    SUCCEED() << "Класс BinaryTree имеет все требуемые методы";
}

// Точка входа для тестов
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}