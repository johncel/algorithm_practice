class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        next_val = None
        if self.next:
            next_val = self.next.val
        return f'<Node val:{self.val} next:{next_val}>'


class LinkedList():
    def __init__(self, val):
        self.node = Node(val)

    def insert(self, val):
        self.node = Node(val, next=self.node)
    
    def append(self, val):
        i_node = self.node
        while i_node.next:
            i_node = i_node.next

        i_node.next = Node(val) 

    def remove(self, val, all=True):
        i_node = self.node
        last_node = None
        while i_node:
            # print(f'remove:: i_node.val:{i_node.val} self.node:{self.node} i_node:{i_node}')
            # print(f'remove:: i_node.val:{i_node.val} self.node:{self.node}')
            if i_node.val == val:
                if last_node == None:
                    self.node = i_node.next
                else:
                    last_node.next = i_node.next
                    if all is not True:
                        return
            last_node = i_node
            i_node = i_node.next

    def remove_i(self, j):
        i = 0
        i_node = self.node
        last_node = None
        while i_node:
            if i == j:
                if last_node == None:
                    self.node = i_node.next
                else:
                    last_node.next = i_node.next
                    if all is not True:
                        return
            last_node = i_node
            i_node = i_node.next
            i += 1
        

    def to_list(self):
        t_list = []
        i_node = self.node
        while i_node:
            t_list.append(i_node.val)
            i_node = i_node.next

        return t_list

    def reverse(self, node=None):
        last_node = None # new terminator
        node = self.node
        while node:
            t = node.next
            node.next = last_node

            last_node = node
            node = t

        self.node = last_node

    def reverse_recursive(self, curr_node, prev_node):
        if curr_node == None:
            curr_node = self.node

        if curr_node.next == None:
            self.node = curr_node
            self.node.next = prev_node
            return

        next_node = curr_node.next
        curr_node.next = prev_node
        self.reverse_recursive(next_node, curr_node)


ll = LinkedList(0)

t_list = ll.to_list()
print(f'linked_list, after init: {t_list}')

for val in range(1, 10):
    ll.append(val)
t_list = ll.to_list()
print(f'linked_list, after append: {t_list}')

for val in range(1, 10):
    ll.insert(val)
t_list = ll.to_list()
print(f'linked_list, after insert: {t_list}')

ll.remove(9, all=True)
t_list = ll.to_list()
# print(f'linked_list.node: {ll.node}')
print(f'linked_list, after remove 9(all): {t_list}')
ll.remove(1, all=False)
t_list = ll.to_list()
print(f'linked_list, after remove 9(all),1: {t_list}')
ll.remove(0)
t_list = ll.to_list()
print(f'linked_list, after remove 9(all),1,0: {t_list}')

ll.remove_i(0)
t_list = ll.to_list()
print(f'linked_list, after remove 9(all),1,0, remove_i(0): {t_list}')
ll.remove_i(1)
t_list = ll.to_list()
print(f'linked_list, after remove 9(all),1,0, remove_i(0,1): {t_list}')
ll.remove_i(7)
t_list = ll.to_list()
print(f'linked_list, after remove 9(all),1,0, remove_i(0,1,7): {t_list}')


ll = LinkedList(0)
t_list = ll.to_list()
print(f'linked_list, after init: {t_list}')

for val in range(1, 10):
    ll.append(val)
ll.reverse()
t_list = ll.to_list()
print(f'linked_list, reverse of 0,1,2,3,4,5,6,7,8,9: {t_list}')

ll = LinkedList(0)
t_list = ll.to_list()
print(f'linked_list, after init: {t_list}')

for val in range(1, 10):
    ll.append(val)
ll.reverse_recursive(None, None)
t_list = ll.to_list()
print(f'linked_list, reverse of 0,1,2,3,4,5,6,7,8,9: {t_list}')
