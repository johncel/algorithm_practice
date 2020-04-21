# heap
# array   node k, left is 2k, right is 2k + 1
import networkx as nx
import matplotlib.pyplot as plt
import sys
from math import log2


class MaxHeap:
    def __init__(self):
        self.nodes = []

    def insert(self, i):
        self.nodes.append(i) # add to the end of the heap
        # print(f'BEFORE HEAPIFY')
        self.print_heap_ascii()
        self.heapify(len(self.nodes))
        # print(f'AFTER HEAPIFY')
        # self.print_heap_ascii()

    def heapify(self, node_i):
        parent_i = node_i // 2
        # print(f'heapify swap?   {self.nodes[parent_i - 1]} < {self.nodes[node_i - 1]}')
        if self.nodes[parent_i - 1] < self.nodes[node_i - 1]:
            self.nodes[parent_i - 1] = self.nodes[parent_i - 1]^self.nodes[node_i - 1]
            self.nodes[node_i - 1]   = self.nodes[parent_i - 1]^self.nodes[node_i - 1]
            self.nodes[parent_i - 1] = self.nodes[parent_i - 1]^self.nodes[node_i - 1]
        if parent_i > 1:
            self.heapify(parent_i)

    def print_heap(self):
        print('THE HEAP')
        last_level = 0
        num_levels = int(log2(len(self.nodes))) + 1
        # print(f'NUM LEVELS: {num_levels}')
        num_spaces_last_level = 4 * len(self.nodes)
        # level_str = ' ' * (num_spaces_last_level // 2 - 2)
        level = 0
        level_str = ' ' * int(pow(2, (num_levels - level - 1))) * 4
        for i, val in enumerate(self.nodes):
            level = int(log2(i+1))
            # print(f'last_level:{last_level} level:{level}')
            # print(f'i:{i} val: {val} level: {level} last_level: {last_level}')
            if level != last_level:
                print(level_str)
                # print(f'making next level str last_level:{last_level} level:{level}')
                if level != num_levels - 1:
                    level_str = ' ' * int(pow(2, (num_levels - level - 1))) * 4
                else:
                    level_str = ''
                last_level = level
            level_str += f'{val:04d}'
            if level > 0:
            # if level < num_levels:
                # level_str += ' ' * int((num_levels + 1) // (level) * 12) 
                # level_str += ' ' * int(pow(2, (num_levels - level))) * 4 * 3 
                level_str += ' ' * int(pow(2, (num_levels - level))) * 4
        print(level_str)


    def print_heap_ascii(self):
        print(f'TREE n:{len(self.nodes)}')
        n = len(self.nodes)
        n_levels = int(log2(n)) + 1
        partial_level = 0
        # print(f'TREE n:{len(self.nodes)} n_levels:{n_levels} partial_level:{partial_level}')
        width = 2
        for level in range(0, n_levels + partial_level):
            if level == n_levels - 1 + partial_level: # special case for bottom row:
                level_str = ''
                for i in range(int(pow(2, level)) - 1, int(pow(2, level + 1)) - 1):
                    # print(f'bottom row printing i:{i}')
                    if i < len(self.nodes):
                        level_str += f'{self.nodes[i]:2d}' + ' '*width
            else:
                start_spaces = int(pow(2, n_levels - level - 1 + partial_level)) - 1
                level_str = ' ' * start_spaces * width
                for i in range(int(pow(2, level)) - 1, int(pow(2, level + 1)) - 1):
                    if i < len(self.nodes):
                        level_str += f'{self.nodes[i]:2d}' + ' ' * int(pow(2, n_levels - level + partial_level) - 1) * width

            print(level_str)


def print_heap2(nodes, G):
    for i, val in enumerate(nodes):
        level = int(log2(i+1))
        if level > 0:
            parent_i = (i + 1) // 2
            G.add_edge(nodes[parent_i - 1], nodes[i - 1])
    
    

heap = MaxHeap()
for i in range(0, 60):
    heap.insert(i) 
    heap.print_heap_ascii()
   
# G = nx.Graph()
# print_heap2(heap.nodes, G)

# G.add_nodes_from(heap.nodes)
# labels = {}
# for i in heap.nodes:
#     labels[i] = f'{i}'

# pos=nx.spring_layout(G)
# nx.draw_networkx_labels(G,pos,labels,font_size=12)
# nx.draw(G,pos)
# plt.show()

sys.exit(0)

import igraph
from igraph import Graph, EdgeSeq
nr_vertices = len(heap.nodes)
v_label = list(map(str, heap.nodes))
print(f'labels...')
print(v_label)
G = Graph.Tree(nr_vertices, 2) # 2 stands for children number
lay = G.layout('rt')

position = {k: lay[k] for k in range(nr_vertices)}
Y = [lay[k][1] for k in range(nr_vertices)]
M = max(Y)

es = EdgeSeq(G) # sequence of edges
E = [e.tuple for e in G.es] # list of edges

L = len(position)
Xn = [position[k][0] for k in range(L)]
Yn = [2*M-position[k][1] for k in range(L)]
Xe = []
Ye = []
for edge in E:
    Xe+=[position[edge[0]][0],position[edge[1]][0], None]
    Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]

labels = v_label

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   ))
fig.add_trace(go.Scatter(x=Xn,
                  y=Yn,
                  mode='markers',
                  name='bla',
                  marker=dict(symbol='circle-dot',
                                size=18,
                                color='#6175c1',    #'#DB4551',
                                line=dict(color='rgb(50,50,50)', width=1)
                                ),
                  text=labels,
                  hoverinfo='text',
                  opacity=0.8
                  ))


def make_annotations(pos, text, font_size=10, font_color='rgb(250,250,250)'):
    L=len(pos)
    if len(text)!=L:
        raise ValueError('The lists pos and text must have the same len')
    annotations = []
    for k in range(L):
        annotations.append(
            dict(
                text=labels[k], # or replace labels with a different list for the text within the circle
                x=pos[k][0], y=2*M-position[k][1],
                xref='x1', yref='y1',
                font=dict(color=font_color, size=font_size),
                showarrow=False)
        )
    return annotations


axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            )

fig.update_layout(title= 'Tree with Reingold-Tilford Layout',
              annotations=make_annotations(position, v_label),
              font_size=12,
              showlegend=False,
              xaxis=axis,
              yaxis=axis,
              margin=dict(l=40, r=40, b=85, t=100),
              hovermode='closest',
              plot_bgcolor='rgb(248,248,248)'
              )

fig.show()
