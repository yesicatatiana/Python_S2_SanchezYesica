# #######################
# #### clase dia 2 ######
# #######################

# numero primo

num=int(input("ingresa un muero: "))
primo=True

for i in range(2,num):
    if num % i==0:
        print("no es primo")
        primo=False
        break
if primo:
    print("es primo")

# Desarrolado por: yesica sanchez c.c 1095304945