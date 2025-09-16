class ArrayStack :
  def __init__(self, capacity):
    self.capacity = capacity
    self.array = [None] * self.capacity
    self.top = -1 

# 공백상태와 포화상태 검사
  def isEmpty(self):
    return self.top == -1
  def isFull(self):
    return self.top == self.capacity - 1

# 새로운 요소 e를 삽입하는 push(e)
  def push(self, item):
    if not self.isFull():
      self.top += 1
      self.array[self.top] = item
    else:
      print("stack overflow")

# 상단 요소를 삭제하는 pop()
  def pop(self):
    if not self.isEmpty():
      item = self.array[self.top]
      self.top -= 1
      return item
    else:
      print("stack underflow")

# 상단 요소를 들여다보는 peek()
  def peek(self):
    if not self.isEmpty():
      return self.array[self.top]
    else:
      print("stack underflow")