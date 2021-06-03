Graph={
    'Arad':{'Zerind':75,'Timisoara':118,'Sibiu':140},
    'Zerind':{'Arad':75,'Oradea':71},
    'Oradea':{'Zerind':71,'Sibiu':151},
    'Timisoara':{'Arad':118,'Lugoj':111},
    'Lugoj':{'Timisoara':111,'Mehadia':70},
    'Mehadia':{'Dobreta':75,'Lugoj':70},
    'Dobreta':{'Mehadia':75,'Craiova':120},
    'Sibiu':{'Arad':140,'Oradea':151,'R.Vilcea':80,'Fagaras':99},
    'Craiova':{'Dobreta':120,'R.Vilcea':146,'Pitesti':124},
    'R.Vilcea':{'Sibiu':80,'Pitesti':97,'Craiova':146},
    'Pitesti':{'R.Vilcea':97,'Craiova':124,'Bucharest':100},
    'Fagaras':{'Sibiu':99,'Bucharest':211},
    'Bucharest':{'Pitesti':100,'Fagaras':211,'Giurgiu':90,'Urzeceni':85},
    'Giurgiu':{'Bucharest':90},
    'Urzeceni':{'Bucharest':85,'Hirsova':98},
    'Hirsova':{'Urzeceni':98,'Eforie':86,'Vaslui':142},
    'Eforie':{'Hirsova':86},
    'Vaslui':{'Hirsova':142,'Iasi':92},
    'Iasi':{'Vaslui':92,'Neamt':87},
    'Neamt':{'Iasi':87}
    }
h ={
    'Arad':366,
    'Zerind':374,
    'Timisoara':329,
    'Lugoj':244,
    'Mehadia':241,
    'Dobreta':242,
    'Craiova':160,
    'R.Vilcea':193,
    'Pitesti':98,
    'Fagaras':178,
    'Sibiu':253,
    'Oradea':380,
    'Bucharest':0,
    'Urzeceni':80,
    'Giurgiu':77,
    'Hirsova':151,
    'Eforie':161,
    'Vaslui':199,
    'Iasi':226,
    'Neamt':234
    }
start='Arad'
goal='Bucharest'
def Select(Open):
    min_f=Open[0][2]
    Vertex=Open[0]
    for item in Open:
        if min_f>item[2] or (min_f==item[2] and item[0]=='Bucharest'):
            min_f=item[2]
            Vertex=item
    return Vertex
def a_star(start,goal,graph):
    open=[[start,0,366]] 
    close=[] 
    open_name=[start] 
    close_name=[]
    while open!=[]:
        p=Select(open) 
        close.append(p)
        close_name.append(p[0])
        open.remove(p)
        open_name.remove(p[0])
        if p[0] is goal:
            return close_name    
        g_p=p[1] 
        for q in graph[p[0]]: 
            if q in close_name:
                continue
            if q in open_name: 
                for item in open:
                    if q==item[0]:
                        if item[1]> g_p + graph[p[0]][q]:
                            item[1]=g_p + graph[p[0]][q]
                            item[2]=item[1]+h[q]
                            break
            elif q not in open_name:
                g_q= g_p+graph[p[0]][q]
                f_q=g_q+h[q]
                open.append([q,g_q,f_q])
                open_name.append(q)
    return close_name
print("The shortest route from Arad to Bucharest: ",a_star(start,goal,Graph))
