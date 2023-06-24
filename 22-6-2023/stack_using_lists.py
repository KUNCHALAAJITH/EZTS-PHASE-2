stack=[]
def push():
    element=int(input("enter the element"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed element",e)
        print(stack)
def top():
    if not stack:
        print("stack is empty")
    else:
        print(stack[-1])
def display():
    if not stack :
        print("empty ")
    else:
        print(stack)
while(True):
    print("select operation 1.push 2.pop 3.display 4.top 5.quit/exit ")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        top()
    elif choice==5:
        break
    else:
        print("please enter correct option")
        
