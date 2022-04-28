import math

#lists of prices of wood
menards = [9.95,11.82,14.40]
lowes = [11.18,14.27,18.27]
l_cost = [0,0,0]
m_cost = [0,0,0]
print("1. 4x4 bed\n2. 2x8 bed")
bedType = input("Would you like to make 4x4 or 2x8 beds? (Enter 1/2): ")

class Garden:
    def BoardFeet(self,x,y):
        return x*y
    def NumBoards(self,b):
        return math.ceil(b/8)
        
g = Garden()

if bedType in ('1','2'):
    quantity = int(input("How many beds do you want to build? "))
    if bedType =="1":
        lf = 16
    else:
        lf = 22
    
    bf = g.BoardFeet(quantity,lf)
    total_boards = g.NumBoards(bf)
    cost = total_boards * 13.87
    for i in range(0,len(lowes)):
        l_cost[i] = total_boards * lowes[i]
        m_cost[i] = total_boards * menards[i]
    
    print(l_cost)
    
else:
    print("Invalid input")
