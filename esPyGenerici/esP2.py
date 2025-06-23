"""
Write a Python code to iterate the first 10 numbers, 
and in each iteration, print the sum of the current and previous number.
"""
t=0
for i in range(10):
    print("il num corrente è {}, quello prima è {}, la loro somma è {}".format(i,t,i+t))
    t=i