

class BinarySearch(list):
    def __init__(self, a, b):
        self.length = a
        self.append(b)
        list_len = 1
        while list_len < a: #Loop to generate the list
            self.append(self[list_len - 1] + b)
            list_len += 1

    def search(self, query):
        first = 0
        last = self.length - 1
        found = False
        result = {'count': 0, 'index': -1}
        if query == self[first]:
            result['index'] = 0
            return result
        elif query == self[last]:
            result['index'] = last
            return result
   
        while first<=last and not found:
            midpoint = (first + last)//2
            if self[midpoint] == query:
                result['count'] += 1
                result['index'] = midpoint
                found = True
            else:
                if query < self[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
  
        return result
