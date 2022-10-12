# ******************************
# Make your Code
# ******************************
# Sarah Castorena
# SID
#numbers = []
num = input('Enter 5 number in acending order')
numbers = list(map(int,num.split()))
    #numbers.append(num) 
  

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