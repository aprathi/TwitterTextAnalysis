import string
import operator
import sys

def topTweeters():
    INPUTFILE = input("Enter the search data file path: ")
    INPUT_FILE_PATH = INPUTFILE + '.txt'

    with open (INPUT_FILE_PATH, encoding='utf-8') as inputFile:
        data=inputFile.readlines()
		
    lines = {}
	
    for i in data:
       
        temp = i.split()
        if temp[0] in lines:
            lines[temp[0]] +=1
        else:
            lines[temp[0]] = 1
			
    lines = sorted(lines.items(), key = operator.itemgetter(1), reverse = True)
	
    OUTPUTFILE = input("Enter the path for the output file for the top n users who have tweeted the most for the entire timeline: ")
    OUTPATH_FILE_PATH = OUTPUTFILE + '.txt'
    outputFile = open(OUTPATH_FILE_PATH, 'w', encoding = "utf-8")
	
    n = input("Enter the number of top users needed who have tweeted the most for the entire timeline: ")
    val = int(n)
    outputFile.write("The top " + n + " users who have tweeted the most for the entire timeline: \n")
	
    for j in range (0,val):
        outputFile.write("The user " + lines[j][0] + " tweeted " + str(lines[j][1]) + " times" + "\n")
        
    outputFile.close
    print("The output file for the top users needed who have tweeted the most for the entire timeline is created")

def topTweetersPerHour():
    INPUTFILE = input("Enter the search data file path: ")
    INPUT_FILE_PATH = INPUTFILE + '.txt'

    with open (INPUT_FILE_PATH, encoding='utf-8') as inputFile:
        data=inputFile.readlines()
		
    lines = {}

    for i in data:
        temp = i.split()
        temp2 = temp[1].split(":")
        temp3 = temp[0] + " " + temp2[1]
        if temp3 in lines:
            lines[temp3]+=1
        else:
            lines[temp3]=1
    lines = sorted(lines.items(), key = operator.itemgetter(1), reverse = True)

    lines2={}
    numPosts = 0
    for i in lines:
        numPosts+=1
        if(i[0].split()[1]) in lines2:
            lines2[i[0].split()[1]]+=1
        else:
            lines2[i[0].split()[1]]=1
    lines2 = sorted(lines2.items(), key = operator.itemgetter(1))

    OUTPUTFILE = input("Enter the path for the output file for the top n users who have tweeted the most for every hour: ")
    OUTPATH_FILE_PATH = OUTPUTFILE + '.txt'
    outputFile = open(OUTPATH_FILE_PATH, 'w', encoding = "utf-8")
	
    n = input("Enter number of top users needed who have tweeted the most for every hour: ")
    val = int(n)
	
    outputFile.write("The top " + n + " users who have tweeted the most for every hour: \n")
    for x in range (0,len(lines2)):
   
        y = val
        
        for z in lines:
            if y == 0:
                break
            if z[0].split()[1] == lines2[x][0]:
                outputFile.write("Username: " + z[0].split()[0] + "\n Hour: " + lines2[x][0] +"\n")
                
                y-=1
    outputFile.close
    print("The output file for the top users who have tweeted the most for every hour is created")
	
def topFollowers():
    INPUTFILE = input("Enter the search data file path: ")
    INPUT_FILE_PATH = INPUTFILE + '.txt'

    with open (INPUT_FILE_PATH, encoding='utf-8') as inputFile:
        data=inputFile.readlines()
		
    lines = {}

    for i in data:
        temp = i.split()
        if temp[0] not in lines:
            lines[temp[0]] = int(temp[-2])

    lines = sorted(lines.items(), key = operator.itemgetter(1), reverse = True)
	
    OUTPUTFILE = input("Enter the path for the output file for the top n users users who have the maximum followers: ")
    OUTPATH_FILE_PATH = OUTPUTFILE + '.txt'
    outputFile = open(OUTPATH_FILE_PATH, 'w', encoding = "utf-8")
	
    n = input("Enter number of top users needed who have the maximum followers: ")
    val = int(n)
    outputFile.write("The top " + n + " users who have the maximum followers: " + "\n")

    for j in range (0, val):
        outputFile.write(str(j+1) + ". Username: " + lines[j][0] + " -> Number of Followers: " + str(lines[j][1]) + "\n")
    outputFile.close
    print("The output file for the top users who have the maximum followers is created")
	
def topRetweets():
    INPUTFILE = input("Enter the search data file path: ")
    INPUT_FILE_PATH = INPUTFILE + '.txt'

    with open (INPUT_FILE_PATH, encoding='utf-8') as inputFile:
        data=inputFile.readlines()
		
    lines = {}

    for i in data:
        temp = i.split()
        j = len(temp) - 2
        tweet = "\""
        for k in range (4, j):
            tweet += temp[k] + " "
        tweet += " ::::;:::: " + temp[0]
  
        if tweet not in lines:
            lines[tweet] = int(temp[-1])
			
    lines = sorted(lines.items(), key = operator.itemgetter(1), reverse = True)		
			
    OUTPUTFILE = input("Enter the path for the output file for the top tweets which have the maximum retweet count: ")
    OUTPATH_FILE_PATH = OUTPUTFILE + '.txt'
    outputFile = open(OUTPATH_FILE_PATH, 'w', encoding = "utf-8")
	
    n = input("Enter number of top tweets which have the maximum retweet count: ")
    val = int(n)
    outputFile.write("The top " + n + " tweets which have the maximum retweet count: " + "\n")		

    for x in range (0, val):
        outputFile.write(str(x+1) + ". Username: " + lines[x][0].split()[-1] + "\n Tweet: " +
                      lines[x][0].split("::::;::::")[0] + "\n No of retweets: " + str(lines[x][1]) + "\n\n")
    outputFile.close	
    print("The output file for the top tweets which have the maximum retweet count is created")
