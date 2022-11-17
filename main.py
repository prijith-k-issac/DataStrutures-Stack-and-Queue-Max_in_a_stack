# Max in a stack problem overview
# The aim is to design an algorithm that can return the maximum item of a stack in O(1)
# running time complexity. We can use O(N) extra memory!

# Hint: we can use another stack to track the max item!


class StackMaxValue:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, data):
        self.stack.append(data)

        if len(self.max_stack) == 0:
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1]:
            self.max_stack.append(data)

        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if len(self.stack) <= 0:
            return "no item remains to remove"

        removed_item = self.stack[-1]
        del self.stack[-1]
        del self.max_stack[-1]
        return f"the removed item is {removed_item}"

    def max_value(self):
        if len(self.max_stack) <= 0:
            return "No item remains in the list"
        return f"the max value is {self.max_stack[-1]}"

    def peek(self):
        if len(self.max_stack) <= 0:
            return "No item remains in the list"
        return f"the last value inserted is {self.stack[-1]}"


stack_max_value = StackMaxValue()
stack_max_value.push(2)
stack_max_value.push(5)
stack_max_value.push(10)
stack_max_value.push(2)
stack_max_value.push(3)
stack_max_value.push(8)
stack_max_value.push(5)
print(stack_max_value.max_value())
print(stack_max_value.pop())
print(stack_max_value.pop())
print(stack_max_value.pop())
print(stack_max_value.pop())
print(stack_max_value.pop())
print(stack_max_value.max_value())


