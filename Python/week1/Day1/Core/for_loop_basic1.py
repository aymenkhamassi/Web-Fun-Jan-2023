for i in range(1,150):
    print(i)

#Multiples of five
for j in range(5,1000):
    print(j*5)

#Counting, the Dojo Way
for y in range(1,100):
    if (y%5 == 0)and(y%10!=0):
        print("coding")
    elif (y%10 == 0)and(y%5!=0):
        print("coding dojo")

#Whoa. That Sucker's Huge
sum = 0
for i in range(0,500):
    if i%2 !=0:
        sum = sum + i
print(sum)

#Countdown by Fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(2,9):
    print(i*3)
