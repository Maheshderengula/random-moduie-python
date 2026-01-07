"""
squreit=lambda x:x*x
r1=squreit(10)
print(r1)

numbers  = [1,2,3,4,5,6,7,8,9,10]
def even_no (numbers):
    return numbers % 2==0

filter_obj= filter(even_no,numbers)
even_numbers= list (filter_obj)
print(even_numbers)

print(list(filter(lambda num : num % 2==0,[1,2,3,4,5,6,7,8,9,10])))
"""
print(list(map(lambda price:price+1==0,[98,198,298,398])))
