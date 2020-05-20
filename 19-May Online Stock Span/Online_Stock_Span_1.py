class StockSpanner:
    #Naive approch gives TLE. So let us save value and span for ith element so that we can calculate for i+1 th element as (1+ span of ith element)
    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        ct=1 
        while self.arr and self.arr[-1][0] <= price:
            prev_price, prev_span = self.arr.pop()     
            ct += prev_span
        self.arr.append((price, ct))
        return ct
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
