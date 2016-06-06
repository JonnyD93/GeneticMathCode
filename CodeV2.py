import random
import operator
from collections import defaultdict
Questions = {}
Answers = {}
answerhigh = 500
NumberofParents = 15
MutationChance = 5 #1 = 100%, 2 = 50%, 3 = 30%, 4-5 = 20%, 6-7-8-9-10 = 10%
lowest = -(answerhigh + answerhigh)
highest = answerhigh + answerhigh

for x in range(1,(10+1)):
	y = random.randint(-answerhigh,answerhigh)
	z = random.randint(-answerhigh,answerhigh)
	Answers[x] = z + y
	Questions[x] = str(z) + " + "  + str(y) + " = "
MinimumMutation = -answerhigh
MaximumMutation = answerhigh
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
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 100
		elif int(checker)-1 == Answers[x] or int(checker)+1 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 75
		elif int(checker)-2 == Answers[x] or int(checker)+2 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 50
		elif int(checker)-3 == Answers[x] or int(checker)+3 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 25
		elif int(checker)-4 == Answers[x] or int(checker)+4 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] + 0
		elif int(checker)-5 == Answers[x] or int(checker)+5 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 25
		elif int(checker)-6 == Answers[x] or int(checker)+6 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 50
		elif int(checker)-7 == Answers[x] or int(checker)+7 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 75
		elif int(checker)-8 == Answers[x] or int(checker)+8 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 100
		elif int(checker)-9 == Answers[x] or int(checker)+9 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 125
		elif int(checker)-10 == Answers[x] or int(checker)+10 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 150
		elif int(checker)-11 == Answers[x] or int(checker)+11 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 175
		elif int(checker)-12 == Answers[x] or int(checker)+12 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 200
		elif int(checker)-13 == Answers[x] or int(checker)+13 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 225
		elif int(checker)-14 == Answers[x] or int(checker)+14 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 250
		elif int(checker)-15 == Answers[x] or int(checker)+15 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 275
		elif int(checker)-16 == Answers[x] or int(checker)+16 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 300
		elif int(checker)-17 == Answers[x] or int(checker)+17 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 325
		elif int(checker)-18 == Answers[x] or int(checker)+18 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 350
		elif int(checker)-19 == Answers[x] or int(checker)+19 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 375
		elif int(checker)-20 == Answers[x] or int(checker)+20 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 400
		elif int(checker)-21 == Answers[x] or int(checker)+21 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 425
		elif int(checker)-22 == Answers[x] or int(checker)+22 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 450
		elif int(checker)-23 == Answers[x] or int(checker)+23 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 475
		elif int(checker)-24 == Answers[x] or int(checker)+24 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 500
		elif int(checker)-25 == Answers[x] or int(checker)+25 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 525
		elif int(checker)-26 == Answers[x] or int(checker)+26 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 550
		elif int(checker)-27 == Answers[x] or int(checker)+27 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 575
		elif int(checker)-28 == Answers[x] or int(checker)+28 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 600
		elif int(checker)-29 == Answers[x] or int(checker)+29 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 625
		elif int(checker)-30 == Answers[x] or int(checker)+30 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 650
		elif int(checker)-31 == Answers[x] or int(checker)+31 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 675
		elif int(checker)-32 == Answers[x] or int(checker)+32 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 700
		elif int(checker)-33 == Answers[x] or int(checker)+33 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 725
		elif int(checker)-34 == Answers[x] or int(checker)+34 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 750
		elif int(checker)-35 == Answers[x] or int(checker)+35 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 775
		elif int(checker)-36 == Answers[x] or int(checker)+36 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 800
		elif int(checker)-37 == Answers[x] or int(checker)+37 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 825
		elif int(checker)-38 == Answers[x] or int(checker)+38 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 850
		elif int(checker)-39 == Answers[x] or int(checker)+39 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 875
		elif int(checker)-40 == Answers[x] or int(checker)+40 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 900
		elif int(checker)-41 == Answers[x] or int(checker)+41 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 925
		elif int(checker)-42 == Answers[x] or int(checker)+42 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 950
		elif int(checker)-43 == Answers[x] or int(checker)+43 == Answers[x]:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 975
		else:
			FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] = FitnessofCurrentGeneration['Offspring'+str(ParentNumber)] - 1000

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
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(3)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness4][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(4)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness5][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(5)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(6)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness5][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(7)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z]),(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness4][z])]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(8)] = [(placeholder0 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder1 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder2 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder3 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder4 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder5 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder6 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder7 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder8 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]()),(placeholder9 + [lambda:0,lambda:(random.randint(MinimumMutation,MaximumMutation))][random.randint(1,10)%MutationChance == 0]())]
	placeholderRando = randomizer(range1,range2)
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),placeholderRando[z]]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(9)] = [placeholder0,placeholder1 ,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	placeholderRando = randomizer(range1,range2)
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness1][z]),placeholderRando[z]]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(10)] = [placeholder0,placeholder1 ,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	placeholderRando = randomizer(range1,range2)
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness2][z]),placeholderRando[z]]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(11)] = [placeholder0,placeholder1 ,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	placeholderRando = randomizer(range1,range2)
	for z in range(0,10):
		globals()['placeholder{0}'.format(z)] = [(globals()['Gen{0}'.format(GenerationNumber-1)][Fitness3][z]),placeholderRando[z]]
		globals()['placeholder{0}'.format(z)] = random.choice(globals()['placeholder{0}'.format(z)])
	(globals()['Gen{0}'.format(GenerationNumber)])['Offspring{0}'.format(12)] = [placeholder0,placeholder1 ,placeholder2,placeholder3,placeholder4,placeholder5,placeholder6,placeholder7,placeholder8,placeholder9]
	for x in range(13, (numberofparents+1)):
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
for GenerationNumber in range(1,10001):
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
