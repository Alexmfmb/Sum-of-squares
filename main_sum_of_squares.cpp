#include <iostream>
#include "Sum_of_squares.cpp"
#include <vector>

int main(){
    for (int i = 0; i < 100; i++){
        for(int j = 1; j < 3; j++){
            for(int k = 0; k < j; k++){
                std::cout << sum_of_n(i,j).at(k);
            }
            std::cout << std::endl;
        }
    }
}