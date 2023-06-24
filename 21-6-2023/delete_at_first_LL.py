
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        
        self.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):#1 iteratn 1 happen
            temp=temp.next
        np.next=temp.next
        temp.next=np
    #delete node in between/position
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        #2 iterations
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def delete(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    # deleting the last node
    def deletelast(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None #last but before node's next we make as none'''
    
        
    def display(self):
        if self.head is None:
            print("linkeed list id empty")
        else:
            temp=self.head
        while temp:
            print(temp.data,"-->",end="")
            temp=temp.next
            

obj= SLL()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print('\n inserting 1000')
obj.insert_position(4,1000)
obj.display()
print('\nafter deleting at pos 2')
obj.delete_position(2)
obj.display()
print('\n after deleting 1st node')
obj.delete()
obj.display()
print('\n after deleting at last node')
obj.deletelast()
obj.display()



        


        
