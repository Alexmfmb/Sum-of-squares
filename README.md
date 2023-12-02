# Sum-of-squares

This algorithm searches for solutions and the degeneracy of the solutions for the following problem:

Can a positive integer s be written as a sum of n square numbers

$s = x_1^2 + x_2^2 + ... + x_n^2$

where all $x_i$ are positive integers.

In the following this problem will be referred to as (s,n)

## For the python version

1. download Sum_of_squares.py
1. use ```from Sum_of_squares import [...]```
[...] can be `Sum_of_n`, `degeneracy` or `degeneracy_long`

These three functions are the most important functions.

- `Sum_of_n(s,n)` returns an array `[bool,x_1,x_2,x_3,...,x_n]`, where bool is `True` when there is a solution and `False` if there is none
- `degeneracy(s,n)` returns an array `[bool,d,[x_1,x_2,x_3,...,x_n],[y_1,y_2,y_3,...,y_n],...]` where d is the degeneracy of the solution without counting permutations of one solution. `[y_1,y_2,y_3,...,y_n]` is another solution
- `degeneracy_long(s,n)` returns an array `[bool,d,[x_1,x_2,x_3,...,x_n],[x_2,x_3,x_1,...,x_n],...,[y_1,y_2,y_3,...,y_n],...]`. This array contains also all permutations of one solution. d is the degeneracy where all permutations are counted.

The idea for this code came from an exercise I had to do for my quantum-mechanics course.
We had to find the smallest 10 Energies $E(n,m,k)$ where $E(n,m,k) \propto n^2 + m^2 + k^2$

The algorithm works (i think), but takes very long for numbers larger than ~10^4.
There is no mathematical proof (yet) that this algorithm always works.
The c++ version of the same algorithm works faster for large numbers.

There is now a function in the python version that calculates the degeneracy of a solution.
There is again no mathematical proof (yet) that the outputs are correct but the results look promising.
