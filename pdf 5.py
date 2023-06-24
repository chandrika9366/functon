# Q5.ion that takes a list and returns a new list with unique elements of the
# first list.Sample List : [1,2,3,3,3,3,4,5]
def unique(a):
    k=[]
    for i in a:
        if i not in k:
            k.append(i)
    print(k)       
unique([1,2,3,3,3,3,4,5])    