#pragma once

class Heap {
public:
    virtual void push(int value) = 0;
    virtual void pop() = 0;
    virtual int top() const = 0;
    virtual bool isEmpty() const = 0;
    virtual ~Heap() = default;
};