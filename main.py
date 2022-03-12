

if __name__ == '__main__':

    a, b, i, j = 0, 0, 0, 0

    print("Enter lower bound of the interval:", end="")

    a = int(input())
    print(a)

    print("Enter upper bound of the interval:", end="")

    b = int(input())
    print(b)

    print("Prime numbers between", a, "and", b, "are:", end="")

    if (a == 1):
        print(a, end=" ")
        a += 1
        if (b >= 2):
            print(a, end=" ")
            a += 1
    if (a == 2):
        print(a, end=" ")


    if (a % 2 == 0):
        a += 1

    for i in range(a, b + 1, 2):


        flag = 1


        j = 2
        while (j * j <= i):
            if (i % j == 0):
                flag = 0
                break
            j += 1

        if (flag == 1):
            print(i, end=" ")

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self , data):
        if self.data:
          if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
          elif data > self.data:
             if self.right is None:
                self.right = Node( data)
             else:
                 self.right.insert(data)
        else:
            self.data = data

