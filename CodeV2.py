import random
import operator
from collections import defaultdict
Questions = {}
Answers = {}
answerhigh = 50000
NumberofParents = 15
MutationChance = 6 #1 = 100%, 2 = 50%, 3 = 30%, 4-5 = 20%, 6-7-8-9-10 = 10%
lowest = -(answerhigh + answerhigh)
highest = answerhigh + answerhigh

for x in range(1,(10+1)):
	y = random.randint(-answerhigh,answerhigh)
	z = random.randint(-answerhigh,answerhigh)
	Answers[x] = z + y
	Questions[x] = str(z) + " + "  + str(y) + " = "
MinimumMutation = -(answerhigh//10)
MaximumMutation = (answerhigh//10)
Range1 = -highest
Range2 = highest
Gen0 = {}
FitnessofCurrentGeneration = {}
File = open("Question&Answers.txt","w")
for x in range(1,11):
        File.write(Questions[x])
        File.write(str(Answers[x])+" ," )
File.close()
for x in range(1,NumberofParents+1):
	File = open("Offspring" + str(x)+".txt","w")
	File.close()
File = open("GeneticCodeAnswers.txt","w")
File.close()
File = open("GeneticList.txt","w")
File.close()
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
createGen0(NumberofParents,Range1,Range2)
print (Gen0)

#Checking the fitness of each parent
def fitness(ParentNumber,GenerationNumber):
	for x in range(1,11):
		checker = (globals()['Gen{0}'.format(GenerationNumber)])['Offspring'+str(ParentNumber)][x-1]
		if int(checker) == int(Answers[x]):
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 1000
		elif int(checker) <= Answers[x]+1 and int(checker) >= Answers[x]-1:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 975
		elif int(checker) <= Answers[x]+2 and int(checker) >= Answers[x]-2:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 950
		elif int(checker) <= Answers[x]+3 and int(checker) >= Answers[x]-3:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 925
		elif int(checker) <= Answers[x]+4 and int(checker) >= Answers[x]-4:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 900
		elif int(checker) <= Answers[x]+5 and int(checker) >= Answers[x]-5:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] +875
		elif int(checker) <= Answers[x]+6 and int(checker) >= Answers[x]-6:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 850
		elif int(checker) <= Answers[x]+7 and int(checker) >= Answers[x]-7:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 825
		elif int(checker) <= Answers[x]+8 and int(checker) >= Answers[x]-8:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 800
		elif int(checker) <= Answers[x]+9 and int(checker) >= Answers[x]-9:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 775
		elif int(checker) <= Answers[x]+10 and int(checker) >= Answers[x]-10:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] +750
		elif int(checker) <= Answers[x]+25 and int(checker) >= Answers[x]-25:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 500
		elif int(checker) <= Answers[x]+500 and int(checker) >= Answers[x]-50:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 250
		elif int(checker) <= Answers[x]+100 and int(checker) >= Answers[x]-100:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 100
		elif int(checker) <= Answers[x]+250 and int(checker) >= Answers[x]-250:
                                                                FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 75
		elif int(checker) <= Answers[x]+500 and int(checker) >= Answers[x]-500:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 50
		elif int(checker) <= Answers[x]+1000 and int(checker) >= Answers[x]-1000:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 25
		elif int(checker) <= Answers[x]+MaximumMutation and int(checker) >= Answers[x]-MinimumMutation:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 5
		else:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = 0

#The checking of all the parents
for x in range(1,NumberofParents):
	fitness(x,0)
	File = open("Offspring" + str(x)+".txt","a")
	File.write(str(FitnessofCurrentGeneration['Offspring'+str(x)])+" \n")
	File.close()
print(FitnessofCurrentGeneration)

#Finding the 5 highest parents
for x in range (1,6):
	globals()['Fitness{0}'.format(x)] = max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get)
	FitnessofCurrentGeneration.pop(max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get),None)
#Creating Generations
"""Fitness1
Fitness1 + Fitness2
Fitness1 + Fitness3
Fitness2 + Fitness4
Fitness1 + Fitness5
Fitness2 + Fitness3
Fitness2 + Fitness5
Fitness3 + Fitness4
Fitness1 + New Fitness
New Fitness
"""
#Creates Modular Generations
#(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(1)] = (globals()['Gen{0}'.format(GenerationNumber-1)])[Fitness1]
"""for z in range(0,10):
	globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z])]
	globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(1)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]"""
def createGenN(numberofparents,range1,range2,GenerationNumber):
	globals()['Gen{0}'.format(GenerationNumber)] = dict()
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(1)] = (globals()['Gen{0}'.format(GenerationNumber-1)])[Fitness1]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(2)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(3)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(4)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness4][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(5)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness5][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(6)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(7)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness5][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(8)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness4][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(9)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	placeholderRando = randomizer(range1,range2)
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),placeholderRando[z]]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(10)] = [placeholder0,placeholder1 ,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	placeholderRando = randomizer(range1,range2)
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),placeholderRando[z]]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(11)] = [placeholder0,placeholder1 ,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	placeholderRando = randomizer(range1,range2)
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z]),placeholderRando[z]]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(12)] = [placeholder0,placeholder1 ,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	placeholderRando = randomizer(range1,range2)
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z]),placeholderRando[z]]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(13)] = [placeholder0,placeholder1 ,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for x in range(14, (numberofparents+1)):
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
for GenerationNumber in range(1,1000001):
	t = GenerationNumber
	createGenN(NumberofParents,Range1,Range2,t)
	#print((globals()['Gen{0}'.format(t)]))
	for x in range(1,NumberofParents+1):
		fitness(x,t)
		File = open("GeneticCodeAnswers.txt","a")
		File.write("Offspring " + str(x)+ ": " +str(globals()['Gen{0}'.format(t)]['Offspring{0}'.format(x)])+", ")
		File.close()
		File = open("Offspring" + str(x)+".txt","a")
		File.write(str(FitnessofCurrentGeneration['Offspring'+str(x)])+" \n")
		File.close()
	File = open("GeneticCodeAnswers.txt","a")
	File.write("\n")
	File.close()
	File = open("GeneticList.txt","a")
	File.write("Generation " + str(t) + "\n")
	print ("Generation " + str(t))
	print(FitnessofCurrentGeneration)
	for x in range (1,6):
		globals()['Fitness{0}'.format(x)] = max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get)
		FitnessofCurrentGeneration.pop(max(FitnessofCurrentGeneration, key=FitnessofCurrentGeneration.get),None)

#Comparer
"""[random.choice(x[0] + y[0]),random.choice(x[1] + y[1]),random.choice(x[2] + y[2]),random.choice(x[3] + y[3]),random.choice(x[4] + y[4]),random.choice(x[5] + y[5]),random.choice(x[6] + y[6]),random.choice(x[7] + y[7]),random.choice(x[8] + y[9])]
x = [10,20,30]
y = [44,55,66]
for z in range(0,3):
	locals()['placeholder{0}'.format(z)] = [x[z],y[z]]
	locals()['placeholder{0}'.format(z)] = random.choice(locals()['placeholder{0}'.format(z)])
xy = [placeholder0,placeholder1,placeholder2]
print (xy)
import random
x = 100
parent = [(placeholder0 + [lambda:0,lambda:(random.randint(1,3))][random.randint(1,10)%MutationChance == 0]()),(x + [lambda:0,lambda:(random.randint(1,3))][random.randint(1,10)%MutationChance == 0]()),(x + [lambda:0,lambda:(random.randint(1,3))][random.randint(1,10)%MutationChance == 0]()),(x + [lambda:0,lambda:(random.randint(1,3))][random.randint(1,10)%MutationChance == 0]())]
print (parent)"""
