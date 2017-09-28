import os
import filecmp
import re
import csv

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.


	fh = open(file)
		
	lst = list()

	for line in fh:
		item = line.split(",")
		new_dic = {}
		new_dic["First"] = item[0]
		new_dic["Last"] = item[1]
		new_dic["Email"] = item[2]
		new_dic["Class"] = item[3]
		new_dic["DOB"] = item[4]
		lst.append(new_dic)
	return (lst[1:])
	

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	new_list = sorted(data, key = lambda x: [x[col]])
	y = new_list[0]
	x = y["First"] + " " + y["Last"]
	
	return x

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	
	class_count = {}
	class_list = list()
	for dic in data:
		if dic["Class"] not in class_count.keys():
			class_count[dic["Class"]] = 1
		else:
			class_count[dic["Class"]] = class_count[dic["Class"]] + 1

	for item in class_count.items():
		class_list.append(item)

	new_list = sorted (class_list, key = lambda x: [x[1]], reverse = True)
	
	return new_list
		


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	day_count = {}
	class_list = list()
	dates = list()
	list_days = list()
	for dic in a:
		dates.append(dic['DOB'])

	for items in dates:
		days = re.findall('[/]([0-9]+)[/]', items)
		list_days.append(days)

	for x in list_days:
		for y in x:
			if y not in day_count.keys():
				day_count[y] = 1
			else:
				day_count[y] += 1
	max_ = 0
	day = 0




	for k in day_count:
		if day_count[k] > max_:
			max_ = day_count[k]
			day = k
	
	return int (day) 


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	list_years = list()
	lst = list()
	dates = list()
	ages = list()
	
	for dic in a:
		dates.append(dic['DOB'])

	for items in dates:
		years = re.findall('[/][0-9]+[/]([0-9]+)', items)
		list_years.append(years)


	count = 0
	for i in list_years:
		for y in i:
			age = 2017 - int (y)
			count = count + 1
			if age < 0:
				age = -(age)		
			ages.append(age)
				
	q = 0			
	for x in ages:
		q = q + x
	average = q / count
		

	





	return int (average)

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	
	tups_list = list()
	new_list = sorted(a, key = lambda x: [x[col]])
	for x in new_list:
		new_tup = (x["First"], x["Last"], x["Email"])
		tups_list.append(new_tup)
	
	
	with open(fileName, "w") as f:
		writer = csv.writer(f)
		#writer.writerow(["First", "Last", "Email"])
		writer.writerows(tups_list)
	
	return
			
		
	
		



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

