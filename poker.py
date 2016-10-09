#poker tracker - reads and writes all my poker data to a database
import sqlite3

def getdata():
	connection = sqlite3.connect('poker.db') 
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM pokerdata")
	data = cursor.fetchall()
	return(data)

def updateHrs(oldHrs):
	sessionHrs = int(input("Session hours: "))
	newHrs = sessionHrs + oldHrs
	return(newHrs) 
	
def updateEarnings(oldEarnings):
	sessionEarnings = int(input("Session earnings: "))
	newEarnings = sessionEarnings + oldEarnings
	return(newEarnings) 

def winrateCalc(newEarnings, newHrs):
	winrate = newEarnings/newHrs
	return(winrate)

def savedata(newHrs, newEarnings):
	connection = sqlite3.connect('poker.db') 
	cursor = connection.cursor()
	#Hours = newHrs 
	#Earnings = newEarnings
	sqlStatement = "UPDATE pokerdata SET Hours=" +str(newHrs)+",Earnings=" +str(newEarnings)
	cursor.execute(sqlStatement)
	connection.commit()
	connection.close()

data = getdata()

oldHrs = data[0][1]
oldEarnings = data[0][2]

newHrs = updateHrs(oldHrs)
newEarnings = updateEarnings(oldEarnings)
winrate = winrateCalc(newEarnings, newHrs)

savedata(newHrs, newEarnings)

print("You played " + str(newHrs) + " hours")
print("You earned " + str(newEarnings) + " dollars")
print("Your winrate is " + str(winrate) + " dollars/hr")



