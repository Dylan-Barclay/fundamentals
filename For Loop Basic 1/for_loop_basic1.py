print("Basic")

for x in range(151):
    print(x)

print("Multiples of Five")

for y in range(5,1001,5):
    print(y)

print("Counting, the Dojo Way")

for z in range(1,101):
    if z % 10 == 0:
        print("Coding ")
    if z % 5 == 0:
        print("Dojo")
    print(z)

print("Whoa. That Sucker's Huge")

count = 0

for i in range(500001):
    if i % 2 != 0:
        count = count + i

print(count)

print("Countdown by Fours")

count_down = 2018
while count_down > 0:
    print(count_down)
    count_down = count_down - 4

print("Flexible Counter")
lowNum = 0
highNum = 90
mult = 3

for n in range(lowNum, highNum):
    if n % mult == 0:
        print(n)

        # 4, quorarion marks, 6 c,11 d,13 move on to the nect function call