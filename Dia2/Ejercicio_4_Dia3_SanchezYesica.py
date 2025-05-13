# #####################
# #### clase dia 2 ####
# #####################

num=int(input("ingresa un numero: "))
primo=True

for n in range(2,num):
    if num % n == 0:
        print("no es primo")
        primo=False
        break
if primo:
    print("es un numero primo")


# Desarrollado por: yesica sanchez - c.c 1095304945