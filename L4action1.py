
# =============================================================================
# import networkx as nx
# import matplotlib.pyplot as plt
# 
# G=nx.DiGraph()
# 
# edges=[('A','B'),('A','D'),('A','E'),('A','F'),('B','C'),('C','E'),('D','C'),('D','A'),('D','E'),('E','C'),('E','B'),('F','D')]
# 
# for edge in edges:
#     G.add_edge(edge[0],edge[1])
#     
# layout=nx.circular_layout(G)
# nx.draw(G,pos=layout,with_labels=True,hold=False)
# plt.show()
# 
# pr=nx.pagerank(G,alpha=1)
# print('简化模型的PR值：',pr)
# 
# pr=nx.pagerank(G,alpha=0.85)
# print('随机模型的PR值：',pr)
# =============================================================================

import numpy as np
a=np.array([[0,0,0,1/3,0,0],
            [1/4,0,0,0,1/2,0],
            [0,1,0,1/3,1/2,0],
            [1/4,0,0,0,0,1],
            [1/4,0,1,1/3,0,0],
            [1/4,0,0,0,0,0]])

b=np.array([1/6,1/6,1/6,1/6,1/6,1/6])
w=b

def work(a,w):
    for i in range(100):
        w=np.dot(a,w)
        print(w)
        
def random_work(a,w,n):
    d=0.85
    for i in range(100):
        w=(1-d)/n+d*np.dot(a,w)
        print(w)
        
work(a,w)
random_work(a,w,6)
