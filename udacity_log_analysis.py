#!/usr/bin/env python3

import psycopg2

dbname = "news"

# Q1) What are the most popular 3 articles of all time?

query1 = """ Select *
             FROM author_pages
             LIMIT 3; """

#Q2) Who are the most popular article authors of all time?

query2 = """Select popular_authors.name, sum(author_pages.viewer) AS viewers
            FROM popular_authors, author_pages
            WHERE popular_authors.title = author_pages.title
            GROUP BY name
            ORDER BY viewers desc;"""

#Q3) On which days did more than 1% of requests lead to errors?

query3 = """Select *
            FROM error_view
            WHERE error_view.Error_Percentage > 1;"""


#Connect to the database

def connect_db(query):

    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

#Question 1

def popular_three_articles(query):
    results = connect_db(query)
    print ('\n The top three articles are:\n')
    for i in results:
        print('\t' + str(i[0] + '-' + str(i[1]))+ 'viewers')
        print(" ")

#Question 2

def popular_authors(query):
    results = connect_db(query)
    print('\n Popular Authors:\n')
    for i in results:
        print('\t' + str(i[0] + '-' + str(i[1])) + 'viewers')
        print(" ")

#Question 3

def error(query):
    results = connect_db(query)
    print('\n The days on which 1% of requests led to an error are: \n')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%"
        print(date + " -- " + errors)
        print (" ")


if __name__ == '__main__':
#Print Results

    popular_three_articles(query1)
    popular_authors(query2)
    error(query3)
