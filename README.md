<h1>Project 3: Logs Analysis Project</h1>

Project submission for Udacity's Full Stack Web Development Nanodegree.

The aim of this project is to run a python script using psycopg2 library to connect to a PostgreSQL database and run queries to answer some questions. The questions are:

1. What are the most popular three articles of all time? Which articles have been accessed the most? 
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views?
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

<h3>Setup</h3>

<h4>Requirements</h4>

You will need python 2.x to run this code. You will need PostgreSQL 9.5 with the "news" database inside it to query from. You will also need the psycopg2 library installed.

<h4>News data</h4>

Download and unzip newsdata.zip from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Then run in the command line:
```
psql -d news -f newsdata.sql
```
to build the news database.

<h4>Running the code</h4>

cd into the project folder where newsdata.sql is located and run the logs_analysis.py code by typing into the command line:
```
python logs_analysis.py
```
The terminal will then output the results of the three queries which would output the answers for the three questions above.
