from operator import itemgetter
#Quick Sort
#==========
def QuickSort(A,start,end):
    if start<end:
        pindex=partition(A,start,end)
        QuickSort(A,start,pindex-1)
        QuickSort(A,pindex+1,end)

def partition(A,start,end):
    pivot = A[end]
    pindex = start
    for i in range(start,end):
        if (A[i] <= pivot):
            A[i],A[pindex]=A[pindex],A[i]
            pindex += 1
    A[pindex],A[end] = A[end],A[pindex]
    return pindex

data = [
    {
        "nama":"Siapa itu",
        "ipk":4.0
     },
    {
        "nama":"Siapa iha",
        "ipk":2.67
     },
    {
        "nama":"Siapa dia",
        "ipk":3.99
     },
    {
        "nama":"Siapa aku",
        "ipk":3.45
     },
    {
        "nama":"Siapa kamu",
        "ipk":3.12
     },
    {
        "nama":"Siapa kalian",
        "ipk":2.6
     },
]
A = [54,26,93,17,77,31,44,55,20]
B = ['a','c','g','b']

QuickSort(A,0,len(A)-1)
QuickSort(B,0,len(B)-1)

print(A,B) #cuman sorting 1 tipe data

nama = (sorted(data,key=itemgetter('nama','ipk')))
print("sorting berdasarkan nama")
for i in range(len(nama)):
    print(nama[i],end="\n")

print()

ipk = (sorted(data,key=itemgetter('ipk','nama')))
print("sorting berdasarkan ipk")
for i in range(len(ipk)):
    print(ipk[i],end="\n")


