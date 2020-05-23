class Solution:
    def frequencySort(self, s: str) -> str:
        cx = Counter(s)
        cc = sorted(cx.items(), key=lambda x:x[1], reverse=True)
        ans = ""
        for i in cc:
            ans += i[0]*i[1]
        return ans
