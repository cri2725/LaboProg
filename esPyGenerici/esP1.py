"""Given two integer numbers, write a Python code to return 
their product only if the product is equal to or lower than 1000.
Otherwise, return their sum.
"""
val1=int(input("primo valore "))
val2=int(input("secondo valore "))
prod= val1*val2
if(prod<=1000):
    print("il prod è {}".format(prod))
else:
    print("la som è {}".format(val1+val2))