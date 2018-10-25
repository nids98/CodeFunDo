from flaskext.mysql import MySQL

mysql = MySQL()

conn=None
c=None

def init(app):
    mysql.init_app(app)
    conn = mysql.connect()
    c= conn.cursor()

def insertTweets(tweet, time, retweetcount):
    c.execute("INSERT INTO tweet(tweet, time, retweetcount) VALUES(%s,%s,%s)",(tweet, time, retweetcount))
