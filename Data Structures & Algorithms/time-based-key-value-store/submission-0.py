class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))      

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key,[])
        if not arr:
            return ""
        
        left, right = 0, len(arr) - 1
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            mid_time, mid_val = arr[mid]
            if mid_time <= timestamp:
                ans = mid_val
                left = mid + 1
            else:
                right = mid - 1
        return ans