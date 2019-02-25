def feld():
	print("-------")
	print("|" + pos[0] + "|" + pos[1] + "|" + pos[2] + "|")
	print("-------")
	print("|" + pos[3] + "|" + pos[4] + "|" + pos[5] + "|")	#Spielfeld
	print("-------")
	print("|" + pos[6] + "|" + pos[7] + "|" + pos[8] + "|")
	print("-------")
win=0
v=1
pos= [" ", " ", " ", " ", " ", " ", " ", " ", " "]

print("-------")
print("|" + "1" + "|" + "2" + "|" + "3" + "|")
print("-------")
print("|" + "4" + "|" + "5" + "|" + "6" + "|")	#Positionenübersicht
print("-------")
print("|" + "7" + "|" + "8" + "|" + "9" + "|")
print("-------")

while(win==0):
	while True:
		auswahlp1=int(input("Bitte geben Sie ihre Position Spieler 1: "))
		if pos[auswahlp1-1]!=" ":
			print("Ne, da ist schon.")
		else:
			pos[auswahlp1-1]="x"
			feld()
			for i in range (1):
				if pos[0:3]==["x","x","x"]:
					win=1
				elif pos[3:6]==["x","x","x"]:
					win=1									
				elif pos[6:9]==["x","x","x"]:
					win=1
				elif pos[0:7:3]==["x","x","x"]:
					win=1
				elif pos[1:8:3]==["x","x","x"]:
					win=1
				elif pos[2:9:3]==["x","x","x"]:
					win=1
				elif pos[0:9:4]==["x","x","x"]:
					win=1
				elif pos[2:7:2]==["x","x","x"]:
					win=1	
			break
	while (win!=1):
		auswahlp2=int(input("Bitte geben Sie ihre Position Spieler 2: "))
		if pos[auswahlp2-1]!=" ":
			print("Ne, da ist schon.")
		else:
			pos[auswahlp2-1]="o"
			feld()
			for i in range (1):
				if pos[0:3]==["o","o","o"]:
					win=2
				elif pos[3:6]==["o","o","o"]:
					win=2									
				elif pos[6:9]==["o","o","o"]:
					win=2
				elif pos[0:7:3]==["o","o","o"]:
					win=2
				elif pos[1:8:3]==["o","o","o"]:
					win=2
				elif pos[2:9:3]==["o","o","o"]:
					win=2
				elif pos[0:9:4]==["o","o","o"]:
					win=2
				elif pos[2:7:2]==["o","o","o"]:
					win=2
			break
if win==1:
	print("Spieler 1 hat gewonnen!")
elif win==2:
	print("Spieler 2 hat gewonnen!")