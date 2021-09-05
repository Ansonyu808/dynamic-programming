# Memoizaton Recipe

1. Solve the problem recursively
   a. Visualize the problem as a tree
   b. Figure out the recursive step
   c. Figure out the base case
   d. implement it using recursion
   e. this is your 'brute force' solution
   f. if it works, then we can continue
2. Make it efficient
   a. Use some data-structure to save found values
   b. A common pattern might be the following:
   _ Add a a memo object as a dictionary to the argument of the function
   _ Add an additional base case which checks if the memo has saved the values \* when we return the value in the recursive step from part 1, set that to the memo object instead, and return the memo object
