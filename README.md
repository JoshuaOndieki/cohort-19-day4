# cohort-19-day4
This repository has tasks for day 4 of Andela cohort 19 bootcamp.

## Missing Number Lab
The missing number function accepts two arrays as arguments.
The arrays are compared and if both are null or both have the same numbers, it returns 0
If one array is longer than the other, then the extra number in the longer array is returned.
E.g 
```
Array 1 : [91, 6, 45, 11]
Array 2 : [6, 11, 91]
```
The function will return *45*

## Binary Search
This lab implements the binary search algorithm.
The BinaryClass constructor takes in two arguments.
```
1. The length of the list to be created
2. The step or difference between consecutive values
```
The search method takes in the *query*( value being searched for as an argument)
The search method then returns a dictionary with the count( number of iteration needed to complete the search) and index of the value being searched for.