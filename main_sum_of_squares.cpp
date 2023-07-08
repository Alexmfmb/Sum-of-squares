#include <iostream>
#include "Sum_of_squares.cpp"
#include <vector>

int main(){
    /*for (int i = 0; i < 100; i++){
        std::cout << i << ":" << sum_of_n(i,2)[0] << sum_of_n(i,2)[1] << sum_of_n(i,2)[2] << std::endl;
    }
    */

    int upper_limit_num = 1000000;
    int upper_limit_sum = 3;
    for (int i = 1; i < upper_limit_num; i++){
        for(int j = 2; j < upper_limit_sum; j++){
            std::vector<int> calc = sum_of_n(i,j);

            //only print hits
            if(calc.at(0) == 1){                 
                std::cout << i << "-->" << calc.at(0) << "||";
                for(int k = 1; k < j+1; k++){
                    std::cout << calc.at(k) << ",";
                }
                std::cout << std::endl;
            }
            
        }
    }
    
}