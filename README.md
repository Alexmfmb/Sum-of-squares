# Sum-of-squares
This is a program which checks for a given Integer, if it can be written as a sum of n square numbers.

The idea for this code came from an exercise I had to do for my quantum-mechanics course.
We had to find the smallest 10 Energies E(n,m,k) where E(n,m,k) ~ n^2 + m^2 + k^2

The algorithm works (i think), but takes very long for numbers larger than ~10^4.
There is no mathematical proof (yet) that this algorithm always works.
The c++ version of the same algorithm works better for large numbers.

There is now a function in the python version that calculates the degeneracy of a solution.
There is again no mathematical proof (yet) that the outputs are correct but the results look promising.
