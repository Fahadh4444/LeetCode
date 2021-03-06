### discard()

- Use of discard() method

The built-in method, discard() in Python, removes the element from the set only if the element is present in the set. If the element is not present in the set, then no error or exception is raised and the original set is printed.

- Example:

  ```# Python program to remove random elements of choice
     # Function to remove elements using discard()
  def Remove(sets):
  sets.discard(20)
  print (sets)
            # Driver Code
            sets = set([10, 20, 26, 41, 54, 20])
            Remove(sets)
  Output: {41, 10, 26, 54}
  ```

### join()

- Use of join() method

  - The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.

- Example:

  ```# Python program to remove random elements of choice
    list1 = ['1','2','3','4']

    s = "-"

    # joins elements of list1 by '-'
    # and stores in sting s
    s = s.join(list1)

    # join use to join a list of
    # strings to a separator s
    print(s)
  Output: 1-2-3-4
  ```
