# ******************************
# Make your Code
# ******************************
# Sarah Castorena
# SID
numbers = []
count = 0
while count < 5:
    num = int(input('Enter numbers in acending order'))
    numbers.append(num) 
    count = count + 1

insertNum = int(input('Enter the insert number'))
if insertNum > numbers[4]:
   numbers.append(insertNum)
elif insertNum < numbers[0]:
    numbers.insert(0,insertNum)   
for i in range(len(numbers)-1):
    
    if (insertNum > numbers[i]) and (insertNum < numbers[i+1]) :
        x = numbers.index(numbers[i])
        numbers.insert(x+1, insertNum)
    
     


print(numbers)