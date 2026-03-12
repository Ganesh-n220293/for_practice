 # default function
# def average(a=9,b=10):
#     print("the average is",(a+b)/2)

# average()
# average(2,3)  9 and 10 are replaced by 2,3

# variable arguements
def average(*numbers):
    sum=0
    for i in numbers:
       sum=sum+i
    print("average is:",sum/len(numbers))
average(1,2,3,4,5,6,7,8,9,10)