class Deque:
    def __init__ (self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def tesret(damn):
    return damn

def cekpalindrom(aString):
    chardeque = Deque()
    aString = aString.replace(" ","")
    for ch in aString:
        chardeque.addRear(ch)
    sama = True
    while chardeque.size() > 1 and sama:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            sama = False
    return sama

