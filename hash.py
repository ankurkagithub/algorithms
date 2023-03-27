
class HashTable():
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % 100

    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        for i in range(len(self.arr[hash])):
            if self.arr[hash][i][0] == key:
                self.arr[hash][i][1] = value
                return
        self.arr[hash].append([key,value])

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for i in range(len(self.arr[hash])):
            if self.arr[hash][i][0] == key:
                return self.arr[hash][i][1]

if __name__ == "__main__":
    t = HashTable()
    t["Tom"] = "Cruise"
    t["James"] = "Bond"
    t["Tom"] = "Bond"
    t["James"] = "Cruise"
    print(t["James"])
