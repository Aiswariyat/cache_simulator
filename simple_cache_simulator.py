class Cache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache_list=[]

    def access_data(self, data):
        if data in self.cache_list:
            self.cache_list.remove(data)
            self.cache_list.append(data)
        else:
            if len(self.cache_list) >= self.cache_size:
                data_removed = self.cache_list.pop(0)
                print("Data '"+data_removed+"' is removed from the cache")
            self.cache_list.append(data)
            print("Data '"+data+"' is added to the cache")

    def cache_print(self):
        print("Current Cache has: ")
        for data in self.cache_list:
            print(data) 

#example
cache_size=3
cache=Cache(cache_size)

cache.access_data("P")
cache.access_data("Q")
cache.access_data("R")
cache.access_data("S")
cache.cache_print()

cache.access_data("B")
cache.cache_print()




