'''
Operator precedence
Outline:
Write a program to understand how the operator precedence works
'''
#v = 4
#w = 5
#x = 8
#y = 2
#z = 0
#z = (v+w)*x/y
#z = (4+5)*8/2
#z = 9*8/2
#z = 9*4
#z = 36
#a = 12
#b = 3
#c = 4
#d = 9
#answer = b**c + d/b*c + a
#answer = 3**4 + 9/3*4 + 12
#answer = 81 + 9/3*4 + 12
#answer = 81 + 3*4 + 12
#answer = 81 + 12 + 12
#answer = 105
'''
Divisible Number
Outline:
Write to check a number is divisible by another number.
'''
a = 100
b = 20
if a%b == 0:
    print("The Number",a,"is divisible by The number",b)
else:
    print("The Number",a,"is not divisible by The number",b)
'''
Mean Value
Outline:
The mean of 40 numbers is 38. Later on, I detected that I misread the number 56 as 36. Find the correct mean of given numbers.
'''
mean1 = 38
wrong_num = 36
cor_num = 56
tot_num = 40
sum = mean1*tot_num
print("The sum of the 40 numbers is equal to",sum)
sum1 = sum-wrong_num+cor_num
print(sum1,"is the correct sum")
cor_mean = sum1/tot_num
print(cor_mean)

'''
Average speed
Outline:
Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?
'''
s1 = 10
s2 = 20
s3 = 30
a = (s1+s2+s3)/3
print(a)
if s1<a:
    print("Cyclist 1 is riding slower than the average speed by",(a-s1))
if s2<a:
    print("Cyclist 2 is riding slower than the average speed by",(a-s2))
if s3<a:
    print("Cyclist 2 is riding slower than the average speed by",(a-s3))
