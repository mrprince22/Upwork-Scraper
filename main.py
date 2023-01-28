import pandas as pd
from upwork import scrape
from time import sleep
from datetime import datetime, timedelta
import csv
from UploadCSV import upload,create_service
from random import randint
from telegram import send_msg
filename = "result.csv"
sheet_name = "Sheet1"
table = {}
with open(filename,"w") as f:
    writer = csv.writer(f)
    writer.writerow(["Job Title","Job Link", "Posted","Budget",
                    #  "Job Description"
                     ])             

def add_row(row: list):
    with open(filename, "a") as file:
        writer = csv.writer(file)
        writer.writerow(row)

def sort_csv():
    df = pd.read_csv(filename)
    df.sort_values(by = ['Posted'], ascending = False, ignore_index = True, inplace = True)
    df.to_csv(filename, index = False)
    

service = create_service()
service.spreadsheets()
n = 10
keywords = ["python", "python scraping", "web scraping", "python tutoring", "coding tutoring"]
# keywords = ["python" for i in range(n)]
def date_to_minutes(date):
    now = datetime.now()
    since = now - date
    return since.total_seconds() // 60


def main(iters = 10, 
         keywords = ["python", "python scraping", "web scraping", "python tutoring", "coding tutoring"],
         wait_time = 0):
    for i in range(iters):
        ret = scrape(k = keywords[i % len(keywords)])
        add = {}
        for key in ret.keys():
            if key in table.keys():
                continue
            table[key] = ret[key]
            add_row(ret[key])
            
            date = ret[key][2]
            mins = date_to_minutes(date)
            if int(mins) <= 10:
                send_msg(ret[key],mins)
        
        sort_csv()
        upload(service,filename, sheet_name)
        print(f"Done iteration {i+1}") 
        sleep(wait_time)

if(__name__ == "__main__"):
    main()