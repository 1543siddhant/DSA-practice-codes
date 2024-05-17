# DSA-practice-codes

##1. Arrays:

Definition: A linear data structure that stores a fixed-size, homogeneous collection of elements in contiguous memory locations. This means all elements have the same data type and are stored sequentially in memory, allowing for efficient random access using indexing.

Operations:

Access: Elements can be directly accessed using their index (array[index]). This operation has constant time complexity (O(1)) in the average case, as it's just a memory lookup based on the index.
Modification: Elements can be modified by assigning a new value to their index (array[index] = new_value). This is also a constant time operation.
Traversal: Iterating through all elements can be done using a loop that goes from 0 to the array's length minus 1 (for element in array: ...). This has linear time complexity (O(n)), as it visits each element once.
Searching: Linear search can be used to find a specific element by comparing it to each element in the array sequentially. This has linear time complexity in the worst case (O(n)) as the entire array might need to be searched.
Insertion: Inserting elements is generally inefficient because it requires shifting elements to make space for the new element. The time complexity for insertion can be linear (O(n)) or worse (O(n^2)) depending on the insertion position and whether resizing is necessary.
Deletion: Deleting elements is also inefficient, as it involves shifting elements to close the gap created by the removal. The time complexity for deletion is similar to insertion, linear (O(n)) or worse (O(n^2)).
Strengths: Efficient random access, simple and memory-efficient for storing similar data types.

Weaknesses: Fixed size (cannot grow or shrink dynamically), inefficient insertion and deletion (especially in the middle), not suitable for storing different data types.
