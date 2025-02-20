import mysql.connector
import requests
import time
from tabulate import tabulate

connection = mysql.connector.connect(host='138.68.140.83', database='dbPavithra', user='Pavithra', password='Chinni@123')
cursor = connection.cursor()

city = 'Anakapalle'

while True:
	response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=22f184280a9ddcd5b223ce0f7475520e&units=metric" % city);
	report =eval(response.text)
	print(report)
	weather = report['weather'][0]
	data = (weather["id"], report["coord"]["lon"], report["coord"]["lat"], weather["description"], report["main"]["temp"], report["main"]["humidity"], report["sys"]["country"], report["name"])
	cursor.execute(f"INSERT INTO weatherData values(%s, %s, %s, %s, %s, %s, %s, %s)", data);
	connection.commit()
	print(f"The temperature in {data[7]} is {data[4]}")
	time.sleep(1500)

cursor.close()
connection.close()

# create table weatherData(
#  weatherId int not null,
#  longitute int not null,
#  latitude int not null,
#  Description varchar(15) not null,
#  Temperature int not null,
#  humidity int not null,
#  Country varchar(10) not null,
#  City varchar(15) not null
#  );