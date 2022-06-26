def median(numbers):
    numbers.sort()
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return(numbers[midpoint])
    else:
        return((numbers[midpoint] + numbers[midpoint - 1]) / 2)
        
def mode(numbers):
    theDictionary = {}
    for word in numbers:
        number = theDictionary.get(word, None)
        if number == None:
            theDictionary[word] = 1
        else:
            theDictionary[word] = number + 1
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            return(key)

def mean(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return(total / len(numbers))

def main():
    print("The median is:", median(numbers))
    print("The mode is:", mode(numbers))
    print("The mean is:", mean(numbers))

    
#input the file
fileName = input("Enter the file name: ")
f = open(fileName, 'r')

#turn the file into a list
numbers = []
for line in f:
   words = line.split()
   for word in words:
       numbers.append(int(word))
       
main()
