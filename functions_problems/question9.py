
## Generator Function With Yield
## Write a generator function that yields even numbers up to a given limit.

def even_numbers_generator(limit):
   for i in range(2,limit + 1, 2):
        yield i  ## yield is used to return the value one by one and it will return the next value when next() function is called
        
for num in even_numbers_generator(10):  ## calling the generator function
    print(num)  ## printing the even numbers one by one