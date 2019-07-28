import requests
import json
import csv

t_stamp = 1454351400
url = f"YOUR API KEY"
itr = 1000
filetowrite = 'data2.csv'


def fetch_data(url, itr, t_stamp, filetowrite):
    i = 0
    weather_data = open(filetowrite, 'w+')
    csvwriter = csv.writer(weather_data)
    while (i <= itr):
        r = requests.get(url)
        data = json.loads(r.text)
        w_data = data['daily']['data'][0]
        # To decrease day by day
        t_stamp -= 86400
        i += 1
        # Write Rows To Excel File
        csvwriter.writerow(w_data.values())
    weather_data.close()
