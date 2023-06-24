stack=[]
even=[]
odd=[]
def push():
    element=int(input("enter the element"))
    stack.append(element)
    print(stack)


def display():
    if not stack :
        print("empty ")
    else:
        for i in range(len(stack)):
            if stack[i]%2==0:
                even.append(stack[i])
            else:
                odd.append(stack[i])
            
            
            
        
while(True):
    print("select operation 1.push 3.display 5.quit/exit ")
    choice=int(input())
    if choice==1:
        push()
    
    elif choice==3:
        
        display()
        print('even:',even)
        print('\n odd',odd)
    elif choice==5:
        break
    else:
        print("please enter correct option")
        
