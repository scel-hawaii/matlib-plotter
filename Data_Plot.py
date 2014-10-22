################################################################################
""" File: Data_Plot.py

This file contains the functions and driver to plot data from .csv file and save graphs as a .png. """
################################################################################

##########Import proper Libraries##########
import csv
import numpy
import operator
import datetime
import itertools
import matplotlib.pyplot as plt

##########Functions##########

#Convert Data String  -> Float
def convert_to_float(row, field):

	#Check if there is data
	if(row[field] == ''):

		#No data = nan
		row[field] = float('nan')
		return row[field]

	else:
	
		#Convert value and return
		row[field] = float(row[field])
		return row[field]

#Pull out the non-date data
def get_data(data, field):

	#Establish a Variable
	value = []

	#Loop through the data
	for row in data:
		
		#Store the seeked data
		value.append(convert_to_float(row, field))
	
	#Return the desired data
	return value

#Convert the date String -> Datetime
def convert_date(data):
	
	#Establish a Variable
	t = []
	field = "db_time"

	#Loop through the data
	for row in data:	

		#Store the date
		t.append(datetime.datetime.strptime(row[field]+"00", "%Y-%m-%d %H:%M:%S.%f%z"))

	#Return
	return t

#Find the index of data
def find_index(InputDate, ConvertedSet):

	#Establish a variable
	index = 0

	#Begin looping
	for row in ConvertedSet:
		
		#Check for a match
		if(InputDate.year == row.year):
			if(InputDate.month == row.month):
				if(InputDate.day == row.day):
					if(InputDate.hour == row.hour):
						if(InputDate.minute == row.minute):
							if(InputDate.second == row.second):
								return index
							else:
								index += 1
						else:
							index += 1
					else:
						index += 1
				else:
					index += 1
			else:
				index += 1
		else:
			index += 1

#Gather the chosen data in the range
def gather_chosen(ChosenData, BeginIndex, EndIndex):
	
	#Establish a storing variable
	chosen = []

	#Esablish a while Loop
	while(BeginIndex >= EndIndex):
	
		#Begin gathering
		chosen.append(ChosenData[BeginIndex])

		#Decrement
		BeginIndex -= 1

	#Return the data
	return chosen

#Gather the Dates for plotting
def gather_dates(ConvertedTime, BeginIndex, EndIndex):
	
	#Establish variables
	range = []
	
	#Establish while loop
	while(BeginIndex >= EndIndex):
		
		#Gather the dates
		range.append(ConvertedTime[BeginIndex])

		#Decrement
		BeginIndex -= 1
	
	#Return the dates
	return range

########## Main ##########

#Establish variables
ChosenData = []
ConvertedTime = []
x = []  #Plot storage for Dates
y = []  #Plot storage for Data
PlotMore = True
color = 'b'
legend_titles = []

#Establish color cycle
colors = itertools.cycle(['r', 'g', 'y', 'c', 'm', 'k', 'b'])

#Open Data File
datafile = open('215_data.csv', 'r')

#Gather the Data
dataorganized = csv.DictReader(datafile)

#Ask for input
field = input('Enter data field: ')
legend_titles.append(field)
BeginDateIn = input('Enter beginning date and time(Y-m-d H:M:S.mS-GMT): ')
EndDateIn = input('Enter end date and time(Y-m-d H:M:S.mS-GMT): ')
print('Please wait...')

#Convert input dates
BeginDate = datetime.datetime.strptime(BeginDateIn + "00", "%Y-%m-%d %H:%M:%S.%f%z")
EndDate = datetime.datetime.strptime(EndDateIn + "00", "%Y-%m-%d %H:%M:%S.%f%z")

#Convert time
ConvertedTime = convert_date(dataorganized)

#Find Index for time
BeginIndex = find_index(BeginDate, ConvertedTime)
EndIndex = find_index(EndDate, ConvertedTime)

#Obtain the dates for plotting
x = gather_dates(ConvertedTime, BeginIndex, EndIndex)

while(PlotMore):

	#Get chosen data
	dataorganized = csv.DictReader(datafile)
	datafile.seek(0) #Reset iterator
	ChosenData = get_data(dataorganized, field)

	#Obtain the chosen data in the specified range
	y = gather_chosen(ChosenData, BeginIndex, EndIndex)

	#Plot the data
	plt.scatter(x, y, c = color, marker='.', edgecolors='none')

	#Plot More?
	response = input('Would you like to plot more data (Y or N)?: ')

	#Check response
	if(response == "Y" or response == "y" or response == "Yes"):

		#Ask for data field
		field = input('Enter data field: ')
		PlotMore = True
		color = next(colors)

		#Save data field in list for legend
		legend_titles.append(field)

	elif(response == "N" or response == "n" or response == "No"):

		#End the loop
		PlotMore = False

	else:
		
		#Error
		print('Invalid Response')

#Plot Format
plt.xlabel('Time')
#plt.ylabel('Solar Irradiance')
plt.title('Weather Box Data')
plt.xlim(BeginDate, EndDate)
plt.legend(legend_titles, loc='best', scatterpoints=1, fontsize=8)

#Save plot as .png
plt.savefig('Solar_Irradiance.png')

#Display plot
plt.show()

#Close file
datafile.close()
