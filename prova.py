def somma(a,b):
    """
    somma due numeri 
    argo:a e b
    ret: somma
    """
    return a+b

var = 2
var2 = 4
for i in range(10):
    var+= 3
    var2+=5
somma=somma(var,var2)
print("num: {}".format(var))
print("num: {}".format(var2))
print("la somma è {}".format(somma))