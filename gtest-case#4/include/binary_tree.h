#pragma once

class BinaryTree {
public:
    virtual void push(int value) = 0;
    virtual void pop(int value) = 0;
    virtual bool search(int value) const = 0;
    virtual ~BinaryTree() = default;
};