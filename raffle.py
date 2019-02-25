import random
def create_list(liste):
	f=open(liste,"r")
	return f.readlines()
file=str(input("Which file should be opened?"))
objects=create_list(file)
rndm=random.randint(0,len(objects)-1)
choice=objects[rndm]
print("The choice is: \033[1;31;40m", choice)