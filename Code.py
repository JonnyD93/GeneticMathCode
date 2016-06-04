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
NumberofParents = 10
Gen0 = {}
FitnessofCurrentGeneration = {}
MutationChance = 0.1

##The Randomizer
def randomizer(number1,number2):
	X = [random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2),random.randint(number1,number2)]
	return X

#The Startup Generation
def createGen0(numberofparents,range1,range2):
	Offspring = dict()
	for x in range(1, (numberofparents+1)):
		Gen0['Offspring{0}'.format(x)] = randomizer(range1,range2)
		FitnessofCurrentGeneration['Offspring{0}'.format(x)] = 0

#Creating the initial Generation
createGen0(NumberofParents,0,20)
print (Gen0)

#Checking the fitness of each parent
def fitness(ParentNumber,GenerationNumber):
	for x in range(1,11):
		checker = (globals()['Gen{0}'.format(GenerationNumber)])['Offspring'+str(ParentNumber)][x-1]
		if str(checker) == str(Answers[x]):
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 100
		elif int(checker)-1 == Answers[x] or int(checker)+1 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 75
		elif int(checker)-2 == Answers[x] or int(checker)+2 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 50
		elif int(checker)-3 == Answers[x] or int(checker)+3 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 25

#The checking of all the parents
for x in range(1,11):
	fitness(x,0)
print(FitnessofCurrentGeneration)

#Finding the 5 highest parents
for x in range (1,6):
	globals()['Fitness{0}'.format(x)] = max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get)
	FitnessofCurrentGeneration.pop(max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get),None)
print(FitnessofCurrentGeneration)
print(Fitness1)
print(Fitness2)
print(Fitness3)
print(Fitness4)
print(Fitness5)
#Creating Generations
"""Fitness1
Fitness1 + Fitness2
Fitness1 + Fitness3
Fitness1 + Fitness4
Fitness1 + Fitness5
Fitness2 + Fitness3
Fitness2 + Fitness5
Fitness3 + Fitness4
New Fitness
New Fitness
"""
#Creates Modular Generations
def createGenN(numberofparents,range1,range2,GenerationNumber):
	globals()['Gen{0}'.format(GenerationNumber)] = dict()
	#(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(1)] = (globals()['Gen{0}'.format(GenerationNumber-1)])[Fitness1]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(1)] = [placeholder0,placeholder1,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(2)] = [placeholder0,placeholder1,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness4][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(3)] = [placeholder0,placeholder1,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness5][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(4)] = [placeholder0,placeholder1,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(5)] = [placeholder0,placeholder1,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness5][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(6)] = [placeholder0,placeholder1,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness4][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(7)] = [placeholder0,placeholder1,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for x in range(8, (numberofparents+1)):
		(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(x)] = randomizer(range1,range2)
	for x in range(1, (numberofparents+1)):
		FitnessofCurrentGeneration['Offspring{0}'.format(x)] = 0




"""
createGenN(10,0,20,1)
print(Gen1)
for x in range(1,11):
	fitness(x,1)
print(FitnessofCurrentGeneration)
for x in range (1,6):
	globals()['Fitness{0}'.format(x)] = max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get)
	FitnessofCurrentGeneration.pop(max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get),None)
"""
for GenerationNumber in range(1,101):
	t = GenerationNumber
	createGenN(10,0,20,t)
	#print((globals()['Gen{0}'.format(t)]))
	for x in range(1,11):
		fitness(x,t)
	print ("Generation " + str(t))
	print(FitnessofCurrentGeneration)
	for x in range (1,6):
		globals()['Fitness{0}'.format(x)] = max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get)
		FitnessofCurrentGeneration.pop(max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get),None)
print(Answers)
#Comparer
"""[random.choice(x[0] + y[0]),random.choice(x[1] + y[1]),random.choice(x[2] + y[2]),random.choice(x[3] + y[3]),random.choice(x[4] + y[4]),random.choice(x[5] + y[5]),random.choice(x[6] + y[6]),random.choice(x[7] + y[7]),random.choice(x[8] + y[9])]
x = [10,20,30]
y = [44,55,66]
for z in range(0,3):
	locals()['placeholder{0}'.format(z)] = [x[z],y[z]]
	locals()['placeholder{0}'.format(z)] = random.choice(locals()['placeholder{0}'.format(z)])
xy = [placeholder0,placeholder1,placeholder2]
print (xy)"""
