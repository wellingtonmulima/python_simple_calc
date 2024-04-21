def addTwo(a,b):
    return a + b

def subtractTwo(a,b):
    return a - b

def multiplyTwo(a,b):
    return a * b

def divideTwo(a,b):
    if b == 0:
        return 'Error cannot divide by zero'
    else:
        return a/b
    
    
print('Simple calculator')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
    
while True:
 choice = input('Enter choice(1/2/3/4): ')
    
 if choice in ('1','2','3','4'):
     num1 = float(input('Enter your first number: '))
     num2 = float(input('Enter your second number: '))
     
     if choice == '1':
         print('Result is:',addTwo(num1,num2))
         
     elif choice == '2':
         print('Result is:',subtractTwo(num1,num2))
         
     elif choice == '3':
         print('Result:',multiplyTwo(num1,num2))
         
     elif choice == '4':
         print('Result:',divideTwo(num1,num2))
         
 else:
     print('Invalid input')
    
 next_calculation = input('Want to do another calculation (yes/no): ')
 
 if next_calculation.lower() !='yes':
     break
         
    
     

     