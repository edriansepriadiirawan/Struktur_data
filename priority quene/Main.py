from PriorityQueneUnsorted import priorityQueneUnsorted

myQueue = priorityQueneUnsorted()
myQueue.add('Amber', 5)
myQueue.add('Diluc', 1)
myQueue.add('Beidou', 3)
myQueue.add('Kaeya', 4)
myQueue.print_all()
data, priority = myQueue.peek()
print(data)
print(priority)
myQueue.remove()
myQueue.print_all()
myQueue.remove()
myQueue.print_all()
myQueue.remove()
myQueue.print_all()