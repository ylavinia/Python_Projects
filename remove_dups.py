'''
author: ylavinia

Remove duplicates from an unsorted linked list without temporary buffer

'''

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def has_next(self):
        return self.next != None 
        
    def get_data(self):
        return self.data
        
    def get_next(self):
        return self.next
        
    def set_data(self, data):
        self.data = data
        
    def set_next(self, next):
        self.next = next
        
class LinkedList(object):
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size  
        
    def is_empty(self):
        return self.size == 0
        
    def insert(self, data):
        new_node = Node(data)
        if self.is_empty():
        
            new_node.set_next(self.head)
            self.head = new_node
            
        else:
            current = self.head
            while current.has_next():
                current = current.get_next()
            current.set_next(new_node)
        self.size += 1
            
        
    def remove_dups(self):
        current = self.head
        while current:
            runner = current
            while runner.get_next():
                if runner.get_next().get_data() == current.get_data():
                    runner.set_next(runner.get_next().get_next())
                else:
                    runner = runner.get_next()
            current = current.get_next()
        
def main():
    new_list = LinkedList()
    new_list.insert("a")
    new_list.insert("b")
    new_list.insert("c")
    new_list.insert(1)
    new_list.insert(1)
    new_list.insert("a")
    new_list.insert("k")
    new_list.insert("b")
    new_list.insert("a")
    new_list.insert("c")
    new_list.insert("b")
    
    current = new_list.head
    cur_list = []
    
    while current:
        #print(current.get_data())
        cur_list.append(current.get_data())
        current = current.get_next()
    
    print("Current list:", cur_list)
    
    new_list.remove_dups()
    
    print("After removing duplicates")
    new_head = new_list.head
    no_dups_list = []
    
    while new_head:
        #print(new_head.get_data())
        no_dups_list.append(new_head.get_data())
        new_head = new_head.get_next()
    print("New list: ", no_dups_list)

if __name__ == "__main__":
    main()
    
    