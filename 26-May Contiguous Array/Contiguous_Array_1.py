class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)==0 or not nums:
            return 0
        maxlength = float('-inf')
        #print("Nums = ", nums)
        
        #Track all 0s and 1s in array, decrement by 1 when 0 seen, increment by 1 when 1 seen  
        arr=[0]*(len(nums)+1)
        for i in range(len(nums)):
            if nums[i]==0:
                arr[i+1]=arr[i]-1
            else:
                arr[i+1]=arr[i]+1
        #print("Arr = ", arr)
        
        #Keep a dictionary to store indexes forevery new symbol encountered 
        dictionary = defaultdict(list)
        for index,value in enumerate(arr):
            dictionary[value].append(index)
        #print("Dictionary = ", dictionary)
        
        #Check if balance obtained is gretaer than current balance
        for i in dictionary.keys():
            if dictionary[i][-1] - dictionary[i][0] > maxlength:
                maxlength = dictionary[i][-1]-dictionary[i][0]
        
        return maxlength
