class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int k = image[sr][sc];
        if(k == newColor)
            return image;
        flood(image, sr, sc, newColor, k);
        return image;
    }
        

    void flood(vector<vector<int>>& image,int sr,int sc,int newColor,int k){
        if (0 <= sr and sr < image.size() and 0 <= sc and sc < image[0].size()){
            if(image[sr][sc] == k){
                image[sr][sc] = newColor;
                flood(image, sr+1, sc, newColor, k);
                flood(image, sr, sc+1, newColor, k);
                flood(image, sr-1, sc, newColor, k);
                flood(image, sr, sc-1, newColor, k);
            }
        }
    }
};
