class MinStack:

    def __init__(self):
       self.stack = [] 
       self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val) #[0, 2, 1]
        #if stack empty push into min stack 
        #else then check if val is less than the top of stack if so push 
        if not self.minStack:
            self.minStack.append(val)
        else:
            #here i need to take the minimum val between the top elem and curr val
            curr_min = min(val, self.minStack[-1])
            self.minStack.append(curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]