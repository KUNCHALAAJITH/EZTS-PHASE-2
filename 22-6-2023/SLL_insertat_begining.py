class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        
        self.head=None

    def insert_begining(self,data):
         nb=Node(data)
         nb.next=self.head
         self.head=nb
    
    def display(self):
         if self.head is None:
             print("linkeed list id empty")
         else:
            temp=self.head
         while temp:
            print(temp.data,"-->",end="")
            temp=temp.next

    
    

obj=SLL()
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
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")

obj.insert_begining(100)
obj.display()
print("")
print("after inserting 555")
obj.insert_begining(555)
obj.display()
