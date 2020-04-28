class Node:

    def __init__(self,val,right,left): #val = donnée du noeud / rigth = le fils droit / left = le fils gauche
        self.__v = val
        self.__r = right
        self.__l = left

    def getV(self):
        return self.__v

    def getR(self):
        return self.__r

    def getL(self):
        return self.__l

    def setR(self,right):
        self.__r = right
        return self.__r

    def setL(self,left):
        self.__l = left
        return self.__l

    def __str__(self):
        return "La valeur du noeud est: "+ str(self.__v)

N1 = Node(12,5,17)
print(N1)

