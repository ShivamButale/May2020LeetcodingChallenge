class Solution {
public:
    int findComplement(int num) {
        int count = 0;
        int i = num;
        while(i != 0){
            i = i/2;
            count++;
        }
        //printf("%d", count);
        int k = pow(2,count) - 1;
        //printf("%d",k);
        return num ^ k;
    }
};
