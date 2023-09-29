print("what you want to learn WHILE LOOP OR FOR LOOP")
print(" WHILE LOOP ENTER 1    FOR LOOP ENTER 2 ")
def learn():
    l=int(input("enter"))
    if l==1:
         # Example: Print numbers from 1 to 5 using a while loop
        print("Syntax of a while loop: \n   counter=1\n    while counter<=5 \n     print(counter)\n     counter =+1\n       # Code to be executed as long as the condition is true")
        counter = 1
        while counter <= 5:
            print(counter)
            counter += 1
    elif l==2:
        print("syntex of a for loop\n   for variables in iterable\n     #code to be executed in each iteration\n for i in range(1,6)\n  print(i)")
        # Example 1: Print numbers from 1 to 5
        for i in range(1, 6):
            print(i)
    else:
        print(" please enter 1 or 2")
        learn()


   
        
learn()

        
