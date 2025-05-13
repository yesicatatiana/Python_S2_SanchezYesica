# ####################
# ##### dia 3 ########
# #################### 
 
# list comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())

out = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k !=n]
print(out)

# Desarrollado por: yesica sanchez - c.c 1.095.304.945
