#To create ADT that implement the "set" concept. a. Add (new Element) -Place a value into the set , b.
# Remove (element) Remove the value c. Contains (element) Return true if element is in collection, d.
# Size () Return number of values in collection Iterator () Return an iterator used to loop over collection, e. 
#Intersection of two sets , f. Union of two sets, g. Difference between two sets, h. Subse

def add(s, new_element):
    if new_element not in s:
        s.append(new_element)

def remove(s, element):
    if element in s:
        s.remove(element)

def contains(s, element):
    return element in s

def size(s):
    return len(s)

def iterator(s):
    return iter(s)

def intersection(set1, set2):
    return [element for element in set1 if element in set2]

def union(set1, set2):
    return list(set(set1 + set2))

def difference(set1, set2):
    return [element for element in set1 if element not in set2]

def is_subset(subset, superset):
    return all(element in superset for element in subset)

#*************************Main Program***************************
set1 = [1,2,3]
set2 = [2,3,4]
while (True):
    print ("1. Add")
    print ("2. Remove")
    print ("3. Contains")
    print ("4. Size")
    print ("5. Iterator")
    print ("6. Intersection")
    print ("7. Union")
    print ("8. Difference")
    print ("9. Subset")
    print ("10. Exit")
    ch = int(input("Enter your choice : "))
    if (ch == 1):
        ele = int(input("Enter the element : "))
        ask = int(input("Enter in set 1 or 2 : "))
        if (ask == 1):
            add(set1,ele)
        elif (ask == 2):
            add(set2,ele)
        else:
            print ("Invalid choice")
    elif (ch == 2):
        ele = int(input("Enter the element : "))
        ask = int(input("Delete from set 1 or 2 : "))
        if (ask == 1):
            remove(set1,ele)
        elif (ask == 2):
            remove(set2,ele)
        else:
            print ("Invalid choice")
    elif (ch == 3):
        ele = int(input("Enter the element : "))
        ask = int(input("Contain from set 1 or 2 : "))
        if (ask == 1):
            contains(set1,ele)
        elif (ask == 2):
            contains(set2,ele)
        else:
            print ("Invalid choice")
    elif (ch == 4):
        ask = int(input("Size of set 1 or 2 : "))
        if (ask == 1):
            size(set1)
        elif (ask == 2):
            size(set2)
        else:
            print ("Invalid choice")
    elif (ch == 5):
        ask = int(input("Iterator of set 1 or 2 : "))
        if (ask == 1):
            print("Set 1:", list(iterator(set1)))            
        elif (ask == 2):
            print("Set 2:", list(iterator(set2)))
        else:
            print ("Invalid choice")
    elif (ch == 6):
        intersection_result = intersection(set1, set2)
        print("Intersection of Set 1 and Set 2:", list(iterator(intersection_result)))
    elif (ch == 7):
       union_result = union(set1, set2)
       print("Union of Set 1 and Set 2:", list(iterator(union_result)))
    elif (ch == 8):
        difference_result = difference(set1, set2)
        print("Difference between Set 1 and Set 2:", list(iterator(difference_result)))
    elif (ch == 9):
        is_subset_result = is_subset(set2, set1)
        print("Is Set 2 a subset of Set 1?", is_subset_result)
    elif (ch == 10):
        break
    else:
        print ("Invalid choice")
print ("Thank You")
        
        
        
        
        
            
        
        

