"""
Write a Python code to accept a string from the user
and display characters present at an even index number.
"""
stringa=str(input("metti la stringa: "))
Lstringa=len(stringa)
for i in range(Lstringa):
    if i%2==0:
        print("lettera {}: {}".format(i+1,stringa[i]))

    