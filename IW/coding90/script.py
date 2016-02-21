from pwn import *
import ast

class Node:
 
    # Constructor to create a new node
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
 
    def build_from_preorder(self, l):
        if not l:
            return
        #print "Node takes value ", str(l[0])
        self.data = l[0]
        index = 1
        for val in l[1:]:
            if val > self.data:
                if l[1:index]:
                    #print "building left with ", l[1:index]
                    self.left = Node()
                    self.left.build_from_preorder(l[1:index])
                if l[index:]:
                    #print "building right with ", l[index:]
                    self.right = Node()
                    self.right.build_from_preorder(l[index:])
                return
            index += 1
        if l[1:index]:
            #print "building left with ", l[1:index]
            self.left = Node()
            self.left.build_from_preorder(l[1:index])

    def display(self):
        print self.print_tree()

    def print_tree(self):
        if self.data == None:
            return ""
        res = str(self.data)
        if self.right != None:
            res = res + ", " + self.right.print_tree()
        if self.left != None:
            res = res + ", " + self.left.print_tree()
        return res

# rep is [15, 75, 70, 74, 74, 49, 44, 10]
#test = [15, 10, 75, 70, 49, 44, 74, 74]
"""test = [18, 10, 53, 40, 30, 25]
n = Node()
n.build_from_preorder(test)
var = n.print_tree()
var = "[" + var + "]"
print var
"""


HOST='188.166.133.53'
PORT=11491
s = remote(HOST,PORT)

intro = s.recvuntil('path?\n')
print intro

print "time to finish"
i = 0
iteration = 0
while True:
    if i == 1: 
        response = s.recvuntil('!\n')
        print "reponse: " + response
    if iteration == 50:
        print s.recv(1024)
    level = s.recvuntil(']')
    print "level: " + level
    values = []
    try:
        values = ast.literal_eval(level[10:])
    except:
       values = ast.literal_eval(level[11:])
    print values
    n = Node()
    n.build_from_preorder(values)
    var = n.print_tree()
    var = "[" + var + "]"
    print "[*] sending " + var
    s.send(var + "\n")
    i = 1
    iteration += 1