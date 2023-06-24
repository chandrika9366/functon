#Q1 . You have to print the largest value out of the given list using the max function.
#numbers = [3, 5, 7, 34, 2, 89, 2, 5]
def max(numbers):
    i=0
    max=0
    while i<len(numbers):
        if numbers[i]>max:
            max=numbers[i]
        i+=1
    return max
    #print(max)
#max([3, 5, 7, 34, 2, 89, 2, 5])    
print(max([3, 5, 7, 34, 2, 89, 2, 5]))    

#Q2. You have to print the sum of the elements of the given list by using the sum function.
#numbers = [1, 2, 3, 4, 5]
def sum(number):
    i=0
    sum=0
    while i<len(number):
        sum+=number[i]
        i+=1
    print(sum)
sum([1,2,3,4,5])   

#Q4. By using reverse function print the reverse order of the list
#reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
def reverse(a):
    i=len(a)-1
    while i>0:
        print(a[i],end="")
        i-=1
reverse(["Z", "A", "A", "B", "E", "M", "A", "R", "D"]) 