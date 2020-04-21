# Python program to check if a given Binary Tree is  
# symmetric or not 
  
# Node structure 
class Node: 
  
    # Utility function to create new node 
    def __init__(self, key): 
        self.key = key 
        self.left = None
        self.right = None

def isMirror(left_tree, right_tree):
    if (left_tree.left and not left_tree.right or left_tree.right and not left_tree.left):
        return False

    def _DFS(tree, left_first, tally):
        if not tree.left and not tree.right:
            return
        if left_first:
            if tree.left:
                tally.append(True)
            else:
                tally.append(False)
            if tree.left:
                _DFS(tree.left, left_first, tally)

            if tree.right:
                tally.append(True)
            else:
                tally.append(False)
            if tree.right:
                _DFS(tree.right, left_first, tally)
        else:
            if tree.right:
                tally.append(True)
            else:
                tally.append(False)
            if tree.right:
                _DFS(tree.right, left_first, tally)

            if tree.left:
                tally.append(True)
            else:
                tally.append(False)
            if tree.left:
                _DFS(tree.left, left_first, tally)

    tally_left = []
    _DFS(left_tree.left, True, tally_left)
    tally_right = []
    _DFS(right_tree.right, False, tally_right)

    print(f'tally_left: {tally_left}')
    print(f'tally_right: {tally_right}')

    if tally_left == tally_right:
        return True
    else:
        return False

#    left_nodes = [left_tree.left]
#    right_nodes = [right_tree.right]
#    while len(left_nodes) > 0:
#        t_left_nodes = []
#        t_right_nodes = []
#        for node in left_nodes:
#            if node.left:
#                t_left_nodes.append(node.left)
#            if node.right:
#                t_left_nodes.append(node.left)
#        for node in right_nodes:
#            if node.left:
#                t_right_nodes.append(node.left)
#            if node.right:
#                t_right_nodes.append(node.left)
#
#        left_nodes = t_left_nodes
#        right_nodes = t_right_nodes
          


def isSymmetric(root): 
  
    # Check if tree is mirror of itself 
    return isMirror(root, root)
  
# Driver Program  
# Let's construct the tree show in the above figure 
root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3) 
is_sym = isSymmetric(root)
print(f' is_ sym: {is_sym}')

root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.right = Node(3) 
root.right.right = Node(3) 
is_sym = isSymmetric(root)
print(f' is_ sym: {is_sym}')
