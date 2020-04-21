import networkx as nx
import matplotlib.pyplot as plt
from math import log2

sorted_list = [1,2,3,4,5,6,7,8,9]
print(f'sorted_list:{sorted_list}')


# G.add_edge(router - 1, router)

# def binary_search_tree(sorted_list, nodes, k):
#     # find the middle value and set this as the node value
#     size = len(sorted_list)
#     for k in range(0, int(log2(size))):
#         div = 2*(k + 1)
#         div_width = int(size / div)
# 
#         index = int(div_width)
# 
#         row_node_count = 0
#         index = int(div_width)
#         while index < size:
#         
#             print(f'k: {k} add node {sorted_list[index]} from index {index}')
#             nodes.append(sorted_list[index])
#             row_node_count += 1
#             index = int(div_width + div_width*2*row_node_count)
#     
#         # for index in range(div_width, size, 2*div_width):
#         #    print(f'k: {k} add node {sorted_list[index]} from index {index}')
#         #    nodes.append(sorted_list[index])


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(tree, key):
    if key >= tree.key:
        if tree.right:
            insert(tree.right, key)
        else:
            tree.right = Node(key)
    else:
        if tree.left:
            insert(tree.left, key)
        else:
            tree.left = Node(key)

def find(tree, key):
    if tree is None:
        return False
    elif tree.key == key:
        return True
    
    if key > tree.key:
        return find(tree.right, key)
    else:
        return find(tree.left, key)


def find_remove_leaf(tree, parent=None, parent_is_left=None):
    if not tree.left and not tree.right:
        if parent:
            if parent_is_left:
                parent.left = None
            else:
                parent.right = None
            return tree.key
        else:
            return None

    if tree.left:
        return find_remove_leaf(tree.left, tree, True)
    elif tree.right:
        return find_remove_leaf(tree.right, tree, False)


def fix_tree(tree):
    if tree.left and tree.key < tree.left.key:
        # swap
        tree.key = tree.key ^ tree.left.key
        tree.left.key = tree.key ^ tree.left.key
        tree.key = tree.key ^ tree.left.key
        fix_tree(tree.left)
    elif tree.right and tree.key > tree.right.key:
        # swap
        tree.key = tree.key ^ tree.right.key
        tree.right.key = tree.key ^ tree.right.key
        tree.key = tree.key ^ tree.right.key
        fix_tree(tree.right)


def bfs_print_levels(tree):
    nodes_to_visit = [tree]
    level = 0
    while len(nodes_to_visit) > 0:
        next_nodes = []
        for tree in nodes_to_visit:
            print(f'level: {level}  key: {tree.key}')
            if tree.left:
                print(f'level: {level}  key: {tree.key} has left:{tree.left.key}')
                next_nodes.append(tree.left)
            if tree.right:
                print(f'level: {level}  key: {tree.key} has right:{tree.right.key}')
                next_nodes.append(tree.right)
        nodes_to_visit = next_nodes
        level += 1
        


def delete(tree, key):
    if not find(tree, key):
        print(f'delete, key {key} not found')
        return

    # if swap_key == None:
    #     print(f'ERROR')
    #     return

    def _delete(tree, key, parent, parent_is_left):
        print(f'delete:: deleting key: {key}')
        if key == tree.key:
            # get the swap key first, it must be a leaf
            swap_key = find_remove_leaf(tree, parent=parent, parent_is_left=parent_is_left)
            if swap_key == None:
                print(f'ERROR')
                return
            else:
                print(f'swap_key: {swap_key}')
            tree.key = swap_key
            fix_tree(tree)
        else:
            if tree.left and key < tree.key:
                _delete(tree.left, key, tree, True)
            elif tree.right:
                _delete(tree.right, key, tree, False)

    _delete(tree, key, None, False)

def print_tree(tree, k=0):
    # print(f'print_tree k:{k} key:{tree.key}') 
    if tree.left:
        G.add_edge(tree.key, tree.left.key)
        print_tree(tree.left, k=k+1)
    if tree.right:
        G.add_edge(tree.key, tree.right.key)
        print_tree(tree.right, k=k+1)

def binary_tree_insertor(list_fragment, tree):
    mid_point = int(len(list_fragment) / 2)
    if tree == None:
        tree = Node(list_fragment[mid_point])
    else:
        insert(tree, list_fragment[mid_point]) 
    # print(f'inserting into tree: {list_fragment[mid_point]}')
    # print(f'inserting into tree mid value: {list_fragment[mid_point]}')
    
    if len(list_fragment) > 1:
        binary_tree_insertor(list_fragment[0:mid_point], tree)
        if mid_point + 1 < len(list_fragment):
            binary_tree_insertor(list_fragment[mid_point+1:], tree)

    return tree


def walk_tree_sorted(tree):
    # to get the values in order, we perform a depth first search, left...
    sorted_output = []
    def _DFS(tree):
        if tree.left:
            _DFS(tree.left)
        sorted_output.append(tree.key)
        if tree.right:
            _DFS(tree.right)

    _DFS(tree)

    return sorted_output

tree = binary_tree_insertor(sorted_list, None)
labels = {}
for i in sorted_list:
    labels[i] = f'{i}'

G = nx.Graph()
G.add_nodes_from(sorted_list)
print_tree(tree)
pos=nx.spring_layout(G)
nx.draw_networkx_labels(G,pos,labels,font_size=12)
nx.draw(G,pos)
plt.show()

# nodes = []
# binary_search_tree(sorted_list, nodes, 0)
# print(f'sorted_list: {sorted_list}')
# print(f'nodes: {nodes}')

for test_val in [1, 2, 3, 9, 10, 11, 12]:
    print(f'find {test_val}: {find(tree, test_val)}')

delete(tree, 1)
delete(tree, 7)
delete(tree, 9)
delete(tree, 5)

for test_val in [1, 2, 3, 9, 10, 11, 12]:
    print(f'after delete find {test_val}: {find(tree, test_val)}')


sorted_list = walk_tree_sorted(tree)
print(f'walk_tree_sorted: {sorted_list}')
bfs_print_levels(tree)

labels = {}
for i in sorted_list:
    labels[i] = f'{i}'
G = nx.Graph()
G.add_nodes_from(sorted_list)
print_tree(tree)
pos=nx.spring_layout(G)
nx.draw_networkx_labels(G,pos,labels,font_size=12)
nx.draw(G,pos)
plt.show()
