#include <iostream>
#include <cmath>
#include <vector>

bool Is_square(int num){
    if(num == 0){
        return false;
    }

    double root = sqrt(num);

    double square = pow(int(root + 0.5),2);

    if(square == num){
        return true;
    }
    else{
        return false;
    }
}

int next_smaller_square(int num){
    if(num == 1){
        return 0;
    }
    int a = 0;
    for(int i = 0; i < num; i++){
        if(Is_square(i)){
            a = i;
        }
    }
    return a;
}

std::vector<int> sum_of_n(int num, int n){
    if(n == 1){
        std::vector<int> ret = {0,0};
        if(Is_square(num) == true){
            ret.at(0) = 1;
        }
        double root = sqrt(num);
        ret.at(1) = root;
        return ret;
    }

    std::vector<int> ret = {0};
    int start = num;
    while(start != 0){
        int a = next_smaller_square(start);

        if(a == 0){
            std::vector<int> ret(n + 1);
            ret.at(0) = 0;
            return ret;
        }

        int b = num - a;

        std::vector<int> sum_n_minus_1(n);

        if(n == 2){
            if(Is_square(b)){
                sum_n_minus_1 = {1, int(sqrt(b))};
            }
            else{
                sum_n_minus_1 = {0, int(sqrt(b))};    
            }
        }
        else if(n > 2){
            sum_n_minus_1 = sum_of_n(b, n-1);
        }

        ret = {sum_n_minus_1.at(0)};

        if(sum_n_minus_1.at(0) == 1){
            double droota = sqrt(a);
            int roota = int(droota);

            ret.push_back(roota);

            ret.insert(ret.end(),sum_n_minus_1.begin() + 1,sum_n_minus_1.end());
            return ret;
        }
        else{
            start = a;
        }

    }

    ret.at(0) = 999;
    return ret;
}
