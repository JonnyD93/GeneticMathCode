import random
import operator
from collections import defaultdict
Questions = {}
Answers = {}
for x in range(1,(10+1)):
	y = random.randint(0,10)
	z = random.randint(0,10)
	Answers[x] = z + y
	Questions[x] = str(y) + " + "  + str(z) + " = "

Parents = {}
FitnessofParents = {}

##The Randomizer
def randomizer(number1,number2):
	X = [random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2)]
	return X
	
#The Startup Generation
def createGen0(numberofparents,range1,range2):
	parent = dict()
	for x in range(1, (numberofparents+1)):
		Parents['parent{0}'.format(x)] = randomizer(range1,range2)
		FitnessofParents['parent{0}'.format(x)] = 0
		
#Creating the initial Generation
createGen0(10,0,20)
print (Parents)

#Checking the fitness of each parent
def fitness(parentnumber):
	for x in range(1,11):
		checker = Parents['parent'+str(parentnumber)][x-1]
		if str(checker) == str(Answers[x]):
			FitnessofParents['parent'+str(parentnumber)] = FitnessofParents['parent'+str(parentnumber)] + 100
		elif int(checker)-1 == Answers[x] or int(checker)+1 == Answers[x]:
			FitnessofParents['parent'+str(parentnumber)] = FitnessofParents['parent'+str(parentnumber)] + 75
		elif int(checker)-2 == Answers[x] or int(checker)+2 == Answers[x]:
			FitnessofParents['parent'+str(parentnumber)] = FitnessofParents['parent'+str(parentnumber)] + 50
		elif int(checker)-3 == Answers[x] or int(checker)+3 == Answers[x]:
			FitnessofParents['parent'+str(parentnumber)] = FitnessofParents['parent'+str(parentnumber)] + 25

#The checking of all the parents
for x in range(1,11):
	fitness(x)
print(FitnessofParents)

#Finding the 5 highest parents
for x in range (1,6):
	globals()['Fitness{0}'.format(x)] = max(FitnessofParents, key=FitnessofParents.get)
	FitnessofParents.pop(max(FitnessofParents, key=FitnessofParents.get),None)
print(FitnessofParents)
print(Fitness1)
print(Fitness2)
print(Fitness3)
print(Fitness4)
print(Fitness5)


#Comparer











