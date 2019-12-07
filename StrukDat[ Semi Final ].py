myDick = [
	{
		"name" : "Sakti",
		"nim": 11181077,
        "ipk": 4.0
	},
	{
		"name" : "Habib",
		"nim": 11181010,
        "ipk": 4.0
	},
	{
		"name" : "Tegar",
		"nim": 11181058,
        "ipk": 4.0
	},
	{
		"name" : "Risna",
		"nim": 11181080,
        "ipk": 4.0
	}
]

def quick(lst):
    if len(lst) < 2:
        return lst
    pivot = lst[0]
    l = quick([x for x in lst[1:] if x < pivot])
    u = quick([x for x in lst[1:] if x >= pivot])
    return l + [pivot] + u

def sortedBy(Data,key):
	prepareData = []
	for i in range(len(Data)):
		prepareData.append(Data[i][key])
	return quick(prepareData)

def SemiFinal(data,terurut,key):	
    newDick = []
    for x in range(len(terurut)):
        for i in range(len(data)):
            dick = {}
            if(data[i][key] == terurut[x]):
                for j in (data[i]):
                    dick[j] = data[i][j]
                print()
            if(dick not in newDick and dick != {}):
                newDick.append(dick)
                dick = {}
    return newDick

def Final(data):	
    for i in range(len(data)):
        for j in (data[i]):
            print(data[i][j],end =" ")
        print()


def Ori(data):
    for i in range(len(data)):
        for j in data[i]:
            print(data[i][j],end=" ")
        print()

A = input("Sorted by : ")    
lol = sortedBy(myDick,A)
Dick = SemiFinal(myDick,lol,A)
print("Before")
Ori(myDick) # Data ori-nya
print()
print("After")
print(Dick)
Final(Dick) # Data ori yang sudah di urutkan
