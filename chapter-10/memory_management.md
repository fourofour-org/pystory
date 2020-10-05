# Memory Management

1. Python uses Garbage Collector instead of Manual memory management

2. Private heap is used to allocate memory

3. Mean all the objects are allocated space in the private heap 

4. Dev does not have the access to the private heap and it's taken care of by the interpreter

5. Python memory manager manages allocations 

6. Memory manager uses the reference counting algorithm

7. Memory manager ( more precisely GC ) looks periodically for the objects which are no longer used by the program 

8. Garbage collector works comes into picture when the count of references to an object is ZERO and the memory has to be recycled 

```
import sys 

## declare an object 
days = [ "a", "b", "c" ]
sys.getrefcount(days) # returns the reference count 
```

