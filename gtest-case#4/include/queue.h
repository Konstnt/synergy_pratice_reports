#pragma once

class Queue {
public:
    virtual void push(int value) = 0;
    virtual void pop() = 0;
    virtual int front() const = 0;
    virtual bool isEmpty() const = 0;
    virtual ~Queue() = default;
};