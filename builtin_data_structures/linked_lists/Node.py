"""Node Class
The Node class has two components:
-Data
- Pointer
Data is the value you want to store in the node. 
The pointer refers us to the next node in the list. 
It is essential for connectivity."""

class Node:
    def __init__(self, data):
        self.data = data    # Data field
        self.next_element = None    # Pointer to next Node