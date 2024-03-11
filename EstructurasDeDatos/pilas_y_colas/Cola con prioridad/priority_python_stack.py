from queue import PriorityQueue

custompriority  = PriorityQueue()
custompriority.put((2,"John"))
custompriority.put((3,"Jorge"))
custompriority.put((1,"Mario"))

print(custompriority)
print(custompriority.get())