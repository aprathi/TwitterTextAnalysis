# TwitterTextCaptureAndAnalysis
Download Python from https://www.python.org/downloads/
Steps:
1) Open the Python shell. 
2) Click on Open and select the script file “twitter.py”
3) Now in the opened twitter file window select Run -> Run module or press F5 to run the script.
4) Provide the required inputs
5) The output txt file gets generated and is saved in the same location as the twitter.py file.

Challenges:	
1) Now write a program to read the file generated. Your program should get the value of n (the number of records to be displayed) from the user and generate the following output and write them into separate files.
  a. The top n users who have tweeted the most for the entire timeline.
  b. The top n users who have tweeted the most for every hour.
  c. The top n users who have the maximum followers.
  d. The top n tweets which have the maximum retweet count.

1) The script file twitter_analysis.py is created for the above challenges. To run the script, open the Python Shell and open the “twitter_analysis.py” script.
2) To find top n users who have tweeted the most for the entire timeline, we need to run the topTweeters() method.
  a. Provide the location of the input data file (instagram.txt)
  b. Provide the location for the output data file for storing the top n users data
  c. Provide the value of n (The requirement was to find the top 10 users, so we input 10. The script can handle any value for n, so it is not always 10 users)
  d. Once the script is run, the output file gets created in the same location as the script file.
3) To find The top n users who have tweeted the most for every hour, we need to run the topTweetersPerHour() method.
4) To find the top n users who have the maximum followers, we need to run the topFollowers() method.
5) To find the top n tweets which have the maximum retweet count, we need to run the topRetweets() method.
