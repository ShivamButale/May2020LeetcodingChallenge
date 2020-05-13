class Solution {
public:
    bool isPerfectSquare(int num){
        if(num == 0 || num == 1 || num == 4 || num == 9)
                return true;
        int z = (num%2);
        long int i = 4;
        if (z == 1)
            i = 3;
        int k =(num/4+1);
        for (; i < k; i=i+2){           //skips even nos. for odd squares and vice versa
            if ((i*i) == num){
                return true;
            }
        }
        return false;
    }
};
