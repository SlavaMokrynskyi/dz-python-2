span_1 = int(input("Enter first span --> "))
span_2 = int(input("Enter second span --> "))
if span_1 > span_2:
    for i in range(span_2,span_1,1):
        if i%7==0:
            print(i)
if span_2 > span_1:
    for i in range(span_1, span_2,1):
        if i%7==0:
            print(i)

span_1 = int(input("Enter first span --> "))
span_2 = int(input("Enter second span --> "))
count = 0
if span_1 > span_2:
    for i in range(span_2,span_1,1):
        print(i)
    for i in range(span_1,span_2,-1):
        print(i)    
    for i in range(span_2,span_1,1):
        if i%7==0:
            print(i)
    for i in range(span_2,span_1,1):
        if i%5==0:
            count +=1
    else:
        print(count)
    
if span_2 > span_1:
    for i in range(span_1,span_2,1):
        print(i)
    for i in range(span_2,span_1,-1):
        print(i)    
    for i in range(span_1,span_2,1):
        if i%7==0:
            print(i)
    for i in range(span_1,span_2,1):
        if i%5==0:
            count +=1
    else:
        print(count)

span_1 = int(input("Enter first span --> "))
span_2 = int(input("Enter second span --> "))
if span_1 > span_2:
    for i in range(span_2,span_1,1):
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print(" Fizz Buzz")
        if i % 3 != 0 and i % 5 != 0:
            print(i)
if span_2 > span_1:
    for i in range(span_1,span_2,1):
        if i % 3 == 0:
            print("Fizz")
        if i % 5 == 0:
            print("Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print(" Fizz Buzz")
        if i % 3 != 0 and i % 5 != 0:
            print(i)