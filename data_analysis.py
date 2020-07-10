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
        # Close the file after reading
        myDataFile.close()
    except:
        print(sys.exc_info())



# =============================================================#

#learnCSVFileRead()
learnCSVAverage()