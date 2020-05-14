class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #Maintain a stack of elements that should be removed
        stack = []
        ct=0
        #increment ct till it reaches k
        for i in num:
            #Remove max elem at each step but if last is max, spare it
            while k-ct>0 and len(stack)>0 and stack[-1]>i:
                ct+=1
                stack.pop()
            stack.append(i)
        if k-ct>0:
            t = k-ct
            stack = stack[:-t]
        return "".join(stack).lstrip('0') or "0"
