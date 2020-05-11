/*
1       = 1
1+3     = 4
1+3+5   = 9
1+3+5+7 = 16
*/

class Solution {
    public boolean isPerfectSquare(int num) {
        int i = 1;
        while(num > 0){
            num -= i;
            i += 2;
            if(num == 0){ 
                return true;
            }
        }
        return false;
    }
}
