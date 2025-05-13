# ####################
# ##### dia 3 ########
# #################### 

# find the runner up-score!

n = int(input())
arr = map(int, input().split())
arr = list(set(arr))
arr.sort()
print(arr[-2])

# Desarrollado por: yesica sanchez - c.c 1.095.304.945
