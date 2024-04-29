/* Consider telephone book database of N clients. Make use of a hash table implementation to quickly look up client‘s telephone number.
Make use of two collision handling techniques and compare them using number of comparisons required to find a set of telephone numbers*/


SIZE = 10
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = None     
def insert(head, data):
    node = Node(data, None)
    if (head == None):
        return node
    temp = head
    while (temp.next != None):
        temp = temp.next
    temp.next = node
    return head
class HashTable:
    ht = []
    def __init__(self):
        for i in range(SIZE):
            node = Node(-1, None)
            self.ht.append(node)
    def hashFunction(self, data):
        return (data % SIZE)
    def insert(self, data):
        index = self.hashFunction(data)
        if (self.ht[index].data == -1):
            print("No collision occurred while inserting")
            self.ht[index].data = data
        else:
            print("Collision occurred while inserting!")
            node = self.ht[index]
            node = insert(node, data)
    def display(self):
        print ()
        print ("Index","  |  ","Value")
        for i in range(SIZE):
            if (self.ht[i].data != -1):
                temp = self.ht[i]
                print ("[",i,"]","  |  ",end="")
                while (temp.next != None):
                    print(temp.data, end = "->")
                    temp = temp.next
                print(temp.data)
    def search(self, data):
        index = self.hashFunction(data)
        temp = self.ht[index]
        while (temp != None):
            if (temp.data == -1):
                print("Number not present in the directory!")
                return
            elif (temp.data == data):
                print("Number found in the directory!")
                print("Number found at index ",index)
                return
            temp = temp.next
        print("Number not present in the directory!")
    def delete(self, data):
        index = self.hashFunction(data)
        prev=None
        curr=self.ht[index]
        while (curr):
            if (curr.data == data):
                if (prev):
                    prev.next = curr.next
                else:
                    self.ht[index]=curr.next
            prev = curr
            curr = curr.next
#*************************Main Function**************************
ht = HashTable()
while (True):
    print ("\n**********Menu**********")
    print ("\n1. Insert")
    print ("\n2. Delete")
    print ("\n3. Search")
    print ("\n4. Display")
    print ("\n5. Exit")
    ch = int(input("\nEnter your choice from 1 to 5 : "))
    if (ch == 1):
        num = int(input("\nEnter the number : "))
        ht.insert(num)
    elif (ch == 2):
        num = int(input("\nEnter the number to be deleted : "))
        ht.delete(num)
    elif (ch == 3):
        num = int(input("\nEnter the number to search : "))
        ht.search(num)
    elif (ch == 4):
        ht.display()
    elif (ch == 5):
        break
    else:
        print ("\nInvalid choice")
print ("\nThank You")
    
    
        
    
                    
        

        
