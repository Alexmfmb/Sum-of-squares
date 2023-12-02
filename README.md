# Sum-of-squares
This algorithm searches for solutions and the degeneracy of the solutions for the following problem:
Can a positive integer s be written as a sum of n square numbers
$s = x_1^2 + x_2^2 + ... + x_n^2$
where all $x_i$ are positive integers.


The idea for this code came from an exercise I had to do for my quantum-mechanics course.
We had to find the smallest 10 Energies E(n,m,k) where $E(n,m,k) ~ n^2 + m^2 + k^2$

The algorithm works (i think), but takes very long for numbers larger than ~10^4.
There is no mathematical proof (yet) that this algorithm always works.
The c++ version of the same algorithm works faster for large numbers.

There is now a function in the python version that calculates the degeneracy of a solution.
There is again no mathematical proof (yet) that the outputs are correct but the results look promising.
