import psycopg2
import random

def pick_text():
	conn = psycopg2.connect("dbname=sample user=postgres password=admin3123")
	cur = conn.cursor()
	cur.execute("SELECT * FROM question;")
	result = cur.fetchall()
	ran = random.choice(result)
	#print(ran[1])
	cur.close()
	conn.close()
	return ran[1]