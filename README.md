# Log-Analysis-Project

## Description

The main idea of this project was to create an internal reporting tool. This tool will collect information and print out reports/logs in plain text from the database. The database contains information about the fictional news website. This reporting tool is designed in Python3 using psycopg2 module. I have imported this module in the python script to print the report of the following three questions:

   1. What are the most popular three articles of all time?
   2. Who are the most popular article authors of all time?
   3. On which days did more than 1% of requests lead to errors?

## Running the Program 

  1. For user's recommendation for this project, make sure a virtual machine is installed. You can download Vagrant and VirtualBox to install and manage your virtual machine.
  2. Once installed, to make sure it is up and running, run vagrant up to make the virtual machine online and later run vagrant ssh to login. 
  3. Download the newsdata.sql file provided by Udacity. Unzip the file and put it inside the vagrant directory. 
  4. To Load the data from database, execute psql -d news -f newsdata.sql.
  5. Connection to the database, execute psql -d news.
  6. If using views (Like I have mentioned below), create them and then exit psql.
  7. Run python3 udacity_log_analysis.py file on the terminal. 
  
## Views Created
    
    CREATE VIEW popular_authors AS
    SELECT articles.title, authors.name
    FROM articles, authors
    WHERE articles.author = authors.id;

    CREATE VIEW author_page AS
    SELECT articles.title, count(log.*) AS viewers
    FROM articles, log
    WHERE log.path = CONCAT('/article/', articles.slug)
    GROUP BY articles.title, articles.author
    ORDER BY viewers desc;

    CREATE VIEW error_view AS
    SELECT date(log.time) AS date, 
           round(100.0*sum(case log.status when '404 NOT FOUND' then 1 else 0 end)/ count(log.status),2) 
    AS Error_Percentage 
    FROM log
    GROUP BY date
    ORDER BY Error_Percentage desc;
