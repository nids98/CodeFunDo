from flaskext.mysql import MySQL

mysql = MySQL()

conn=None
cursor=None

def init(app):
    mysql.init_app(app)
    conn = mysql.connect()
    cursor= conn.cursor()

def insertTweets(tweet, time, retweetcount):
    cursor.execute("INSERT INTO ngo (tweet,time,retweetcount) VALUES(%s,%s,%s)",(tweet, time, retweetcount))
