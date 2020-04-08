from Node import *

class BinaryTree:

    def __init__(self,root):
        self.__root = root

    def getr(self):
        return self.__root

    def isRoot(self,node):
        if self.__root == node :
            return True
        else:
            return False

    #def size(self,node):
        

Arbre = BinaryTree(Node(12,None,None))
Arbre.getr().setL(Node(5,None,None))
Arbre.getr().getL.setL(Node(4,None,None))
Arbre.getr().getL.setR(Node(6,None,None))
Arbre.getr().getL.getL.setL(Node(3,None,None))

Arbre.getr().setR(Node(17,None,None))
Arbre.getr().getR.setR(Node(19,None,None))
Arbre.getr().getR.getR(Node(18,None,None))
Arbre.getr().getR.getR.setR(Node(21,None,None))
