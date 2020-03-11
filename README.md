# Demo:
![image](https://github.com/manbobo2002/serverless-votting/blob/master/demo.gif)  

# Technologies used:  
AWS Lambda, AWS API Gateway, AWS DynamoDB, AWS S3, Python 3.7, html, javascript, CSS3

# How to use:  
When we click on the support button, then the vote of the person will be added as one. If we click the Refresh button, then it will show the diagram of the trend for those 3 candidates.  

# Proposed system architecture:
![image](https://github.com/manbobo2002/serverless-votting/blob/master/Architecture.PNG)  
The reasons why I deiced to use lambda are as below:  
1. Faster Development with serverless architecture  
Only need to care about the code without handling the server.  
2. HA  
Avaliable for 7x24 and will not stop suddenly.
3. Easier Operational Management  
No need to have system administration.    

# How to setup:  
1. put the index.html into S3 and set it public for static hosting.  
2. put the lambda_function.py into AWS lambda function and choose python 3.7 as environment.  
3. set the post method in AWS API gateway and test the function works or not. If work, just copy the API url into the code.  
