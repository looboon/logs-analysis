#!/usr/bin/env python
import psycopg2


def top_three():
    conn = psycopg2.connect(dbname="news")
    query = """SELECT SUBSTR(path, 10) AS article, COUNT(id) AS views
               FROM log
               GROUP BY 1
               HAVING SUBSTR(path, 10) <> ''
               ORDER BY 2 DESC
               LIMIT 3"""
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    # return results
    final_output = "----- Most popular three articles of all time --------\n"
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        query_result = '{} - {} views\n'.format(title, views)
        final_output += query_result
    return final_output


def most_popular_authors():
    conn = psycopg2.connect(dbname="news")
    query = """SELECT name, COUNT(c.id) AS views
               FROM authors AS a
               INNER JOIN articles AS b ON a.id = b.author
               LEFT JOIN log AS c ON SUBSTR(c.path, 10) = b.slug
               GROUP BY 1
               ORDER BY 2 DESC"""
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    # return results
    final_output = "----- Most popular article authors of all time --------\n"
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        query_result = '{} - {} views\n'.format(title, views)
        final_output += query_result
    return final_output


def error_list():
    conn = psycopg2.connect(dbname="news")
    query = """SELECT DATE(a.time) AS log_date,
               (COUNT(a.status)/AVG(all_count) * 100) AS percent_errors
               FROM log AS a
               INNER JOIN
               (SELECT DATE(time) AS log_date, COUNT(status)
               AS all_count FROM log GROUP BY 1) AS b
               ON DATE(a.time) = b.log_date
               WHERE status = '404 NOT FOUND'
               GROUP BY 1
               HAVING (COUNT(a.status)/AVG(all_count) * 100) > 1"""
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    # return results
    final_output = "----- Days where more than 1% of " \
                   "requests lead to errors --------\n"
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        query_result = "{} - {:.2f}% errors\n".format(title, views)
        final_output += query_result
    return final_output


if __name__ == '__main__':
    print(top_three())
    print(most_popular_authors())
    print(error_list())
