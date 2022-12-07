employee=[]
def push():
        emp_name=input("enter employee name")
        emp_id=input("enter id ")
        emp_salary=input("enter salary of the employee")
        a=(emp_name,emp_id,emp_salary)
        employee.append(a)
def pop():
    if employee==[]:
        print("under flow")
    else:
        
        print("elements  popped",employee.pop())
        

def display():
    if employee !=[]:
        n=len(employee)
        for i in range (n-1,-1,-1):
            print(employee[i])
    else:
        print("empty record")

while True:
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        print("end")
        break
    else:
        print("invalid choice")
        
