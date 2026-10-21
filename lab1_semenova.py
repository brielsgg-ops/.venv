import math
a=float(input("Введите переменную a: "))
x=float(input("Введите переменную x: "))
z=((math.pow(math.e,a)*math.log10(a/x))/(math.pi*math.sqrt(x/a)))
b= -0.485 * math.pow(z,0.4)
print("При введенных данных а и х z = |{0:.2f}".format(z))
print("и b = |{0:.2f}".format(b))
