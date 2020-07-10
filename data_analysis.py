# =============================================================#
import sys
import datetime
import csv

# =============================================================#
print("This is python Data Analysis learning codebase")
print("Python Version = ", sys.version_info.major,
      ".", sys.version_info.minor)
print("Run Date & Time = ", datetime.datetime.now(), "\n")


# =============================================================#
# This is data analysis function for reading covid-19 data from John hopkins data repository on Github repo:
# https://github.com/CSSEGISandData/COVID-19
def learnCSVFileRead():
    try:
        myDataFile = open("../../../Documents/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports_us/"
                          "04-12-2020.csv", "r")
        readCSV = csv.reader(myDataFile, delimiter=',')
        header = next(readCSV, None)
        #print(header[0], "|", header[7], "|", header[8])
        totalActive = 0
        for row in readCSV:
            # Print all the rows in the CSV file
            # print(row)
            # Print all the rows but only coloumn 0, 7 and 8 from the CSV file
            if(row[0] == 'Recovered'):
                continue
            #print(row[0], "|", row[7], "|", row[8])
            totalActive = totalActive + (int)(row[8])
        print("Total active cases =", totalActive)
        # Close the file after reading
        myDataFile.close()
    except:
        print(sys.exc_info())

def learnCSVAverage():
    try:
        myDataFile = open("../../../Documents/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports_us/"
                          "04-12-2020.csv", "r")
        readCSV = csv.reader(myDataFile, delimiter=',')
        header = next(readCSV, None)
        #print(header[0], "|", header[7], "|", header[8])
        totalActive = 0
        numStates = 0
        for row in readCSV:
            # Print all the rows in the CSV file
            # print(row)
            # Print all the rows but only coloumn 0, 7 and 8 from the CSV file
            if(row[0] == 'Recovered'):
                continue
            #print(row[0], "|", row[7], "|", row[8])
            totalActive = totalActive + (int)(row[8])
            numStates = numStates + 1
        print("Total active cases =", totalActive)
        print("Number of states: =", numStates)
        print("Average number of active cases today=", totalActive/numStates)
        averageCSV = totalActive/numStates

        print("Now calculating the average across all states")
        # reset the file handle to start position by using seek
        myDataFile.seek(0)
        # now skip the header
        next(readCSV, None)
        # iterate through the file and compate the average value to column value
        aboveAvgList = []
        belowAvgList = []
        for row in readCSV:
            if((float)(row[8]) > averageCSV):
                #print(row[0], "-> This state is above average")
                aboveAvgList.append(row[0])
            else:
                #print(row[0], "-> This state is below average")
                belowAvgList.append(row[0])

        print("List of Above average states")
        aboveAvgList.sort()
        for i in aboveAvgList:
            print(i)

        print("\n\nList of Below average states")
        belowAvgList.sort()
        for i in belowAvgList:
            print(i)

        # Close the file after reading
        myDataFile.close()
    except:
        print(sys.exc_info())

# =============================================================#

#learnCSVFileRead()
learnCSVAverage()