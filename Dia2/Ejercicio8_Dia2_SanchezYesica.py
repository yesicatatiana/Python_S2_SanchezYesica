# #######################
# #### clase dia 2 ######
# #######################

# gerenar serie fibonacci

num=int(input("cuantos digitos desesa de la serie de fibonacci: "))
num1=0
num2=1
print(num1)
print(num2)

for i in range(2,num):
    num3=num1+num2
    print(str(num3))
    num1 = num2
    num2 = num3

 
# Desarrollado por: yesica sanchez - c.c 1.095.304.945
