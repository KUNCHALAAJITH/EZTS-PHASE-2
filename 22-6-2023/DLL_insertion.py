class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
        
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
        
    def insert_end(self):
        n=Node(25)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
        
    def insert_pos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
        
    def deletestart(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
    def deleteatend(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
        
    def deleteatpos(self,pos):
         temp=self.head.next
         prev=self.head
         for i in range(1,pos-1):
                temp=temp.next
                prev=prev.next
         prev.next=temp.next
         temp.next=prev.next   
        
        
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
n4=Node(400)
n4.prev=n3
n3.next=n4
n5=Node(500)
n5.prev=n4
n4.next=n5
l.display()
print('\n insert at start')
l.insert_start()
l.display()
print("\ninsert at end")
l.insert_end()
l.display()
print('\n insert at position')
n=int(input('enter position'))
l.insert_pos(n)
l.display()
print('\nafter deleting 1st node')
l.deletestart()
l.display()
print("\ndelete last node")
l.deleteatend()
l.display()
print('\n delete at position')
k=int(input('enter position to delete'))
l.deleteatpos(k)
l.display()
