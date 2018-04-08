import csv

## steps to get data from a csv file to a list
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData

## accessing the data from the list
exampleData[6][1]

## accessing row by row using a for loop

for row in exampleReader:
print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

## writing data into a csv file

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])

outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])

outputWriter.writerow([1, 2, 3.141592, 4])

outputFile.close()
