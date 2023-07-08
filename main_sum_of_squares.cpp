#include <iostream>
#include "Sum_of_squares.cpp"
#include <vector>

int main(){
    /*for (int i = 0; i < 100; i++){
        std::cout << i << ":" << sum_of_n(i,2)[0] << sum_of_n(i,2)[1] << sum_of_n(i,2)[2] << std::endl;
    }
    */

    //limits for numbers checked
    int lower_limit_num = 1;
    int upper_limit_num = 10000000;

    //limits for number of summands
    int lower_limit_sum = 3;
    int upper_limit_sum = 3;

    int false_or_true = 0; //set 1 to print true results, set 0 to print false results

    for (int i = lower_limit_num; i < upper_limit_num + 1; i++){
        for(int j = lower_limit_sum; j < upper_limit_sum + 1; j++){
            std::vector<int> calc = sum_of_n(i,j);

            //only print hits
            if(calc.at(0) == false_or_true){                 
                std::cout << i << "-->" << calc.at(0) << "||";
                for(int k = 1; k < j+1; k++){
                    std::cout << calc.at(k) << ",";
                }
                std::cout << std::endl;
            }
            
        }
    }
    
}