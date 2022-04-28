import math

#lists of prices of wood
menards = [9.95,11.82,14.40]
lowes = [11.18,14.27,18.27]
l_cost = [0,0,0]
m_cost = [0,0,0]
best_value = [0,0,0]
savings = 0
over_budget = 0
best_value_string = ["","",""]
print("1. 4x4 bed\n2. 2x8 bed")
bedType = input("Would you like to make 4x4 or 2x8 beds? (Enter 1/2): ")

class Garden:
    def BoardFeet(self,x,y): #quantity,lf
        return x*y
    def NumBoards(self,b): #bf
        return math.ceil(b/8)
    def BestValuePrice(self,x,y,z): #l_cost, m_cost, best_value
        for i in range(0,len(lowes)):
            if x[i]>y[i]:
                z[i] = y[i]
            else:
                z[i] = x[i]
    def BestValueStore(self,x,y,z): #l_cost, m_cost, best_value_string
        for i in range(0,len(lowes)):
            if x[i]>y[i]:
                z[i] = "Menards"
            else:
                z[i] = "Lowes"
        
g = Garden()

if bedType in ('1','2'):
    quantity = int(input("How many beds do you want to build? "))
    if bedType =="1":
        lf = 16
    else:
        lf = 22
    
    bf = g.BoardFeet(quantity,lf)
    bv = g.BestValuePrice(m_cost,l_cost,best_value)
    bvs = g.BestValueStore(m_cost,l_cost,best_value_string)
    total_boards = g.NumBoards(bf)
    cost = total_boards * 13.87
    for i in range(0,len(lowes)):  #populate lists
        l_cost[i] = total_boards * lowes[i]
        m_cost[i] = total_boards * menards[i]
    print("\n\nPrice for " + str(quantity) + " beds (" + str(bf) + " boards)")
    print("Lowes:")
    print("  -  2x6x8 - " + "${:,.2f}". format(lowes[0]) + " - " + "${:,.2f}". format(l_cost[0]))
    print("  -  2x8x8 - " + "${:,.2f}". format(lowes[1]) + " - " + "${:,.2f}". format(l_cost[1]))
    print("  -  2x10x8 - " + "${:,.2f}". format(lowes[2]) + " - " + "${:,.2f}". format(l_cost[2]) + "\n")
    print("Menards:")
    print("  -  2x6x8 - " + "${:,.2f}". format(menards[0]) + " - " + "${:,.2f}". format(m_cost[0]))
    print("  -  2x8x8 - " + "${:,.2f}". format(menards[1]) + " - " + "${:,.2f}". format(m_cost[1]))
    print("  -  2x10x8 - " + "${:,.2f}". format(menards[2]) + " - " + "${:,.2f}". format(m_cost[2]) + "\n")
    
    print("Best Cost Summary:")
    if m_cost[0]>l_cost[0]:
        savings = m_cost[1]-m_cost[0]
        print("  -  2x6x8 - " + "${:,.2f}". format(l_cost[0]) + " - " + "Lowes (save " + "${:,.2f}". format(savings) + ")")
    else:
        savings = l_cost[1]-l_cost[0]
        print("  -  2x6x8 - " + "${:,.2f}". format(m_cost[0]) + " - " + "Menards (save " + "${:,.2f}". format(savings) + ")")
    if m_cost[1]>l_cost[1]:
        print("  -  2x8x8 - " + "${:,.2f}". format(l_cost[1]) + " - " + "Lowes")
    else:
        print("  -  2x8x8 - " + "${:,.2f}". format(m_cost[1]) + " - " + "Menards")
    if m_cost[2]>l_cost[2]:
        over_budget = l_cost[2]-l_cost[1]
        print("  -  2x10x8 - " + "${:,.2f}". format(l_cost[2]) + " - " + "Lowes (+ " + "${:,.2f}". format(over_budget) + ")")
    else:
        over_budget = m_cost[2]-m_cost[1]
        print("  -  2x10x8 - " + "${:,.2f}". format(m_cost[2]) + " - " + "Menards (+" + "${:,.2f}". format(over_budget) + ")")
else:
    print("invalid input")


