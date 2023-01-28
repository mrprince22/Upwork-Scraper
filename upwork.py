from datetime import datetime, timedelta
from bs4 import BeautifulSoup as BS
import pandas as pd
from getHtml import gethtml
def to_list(result):
    ret = {}
    n = len(result['Job Title'])
    for i in range(n):
        key = result['Job Title'][i] + result['Job Link'][i].split("~")[-1]
        val = []
        for k in result.keys():
            val.append(result[k][i])
        ret[key] = val
    return ret
    
def scrape(k = "python"):
    html = gethtml(k)
    doc = BS(html, "html.parser")

    def toDate(time,type):
        def toMinutes(time, type)-> int : 
            time = int(time)
            if "month" in type:
                return time * 30 * 24 * 60
                
            elif "day" in type:
                return time * 24 * 60
                
            elif "hour" in type:
                return time  * 60
            
            elif "minute" in type:
                return time
            
            elif "second" in type:
                return time / 60
            
            return "ERROR" + "  " + str(time) + "  " + str(type)
        mins = toMinutes(time,type)
        d = datetime.today() - timedelta(minutes=mins)
        return d
        
        
    result = {
        "Job Title" : [],
        "Job Link": [], 
        "Posted" : [],
        "Budget" : [], 
        }

    jobsTitle = doc.find_all("h3",{"class" : "my-0 p-sm-right job-tile-title"})
    for job in jobsTitle:
        jobTitle = job.text
        result["Job Title"].append(jobTitle)
        
        link = job
        link = link.find("a", href = True)
        link = link['href']
        link = "https://upwork.com" + link
        result["Job Link"].append(link)
        

    postTimes = doc.find_all("span",{"data-test":"posted-on"})
    for postTime in postTimes:
        time = postTime.text
        time,type = time.split()[:2]
        time = toDate(time,type)
        result["Posted"].append(time)
        
        
    budgets = doc.find_all("strong",{"data-test":"job-type"})
    for budget in budgets:
        budget = budget.text
        result['Budget'].append(budget)
        
    # do later: fixed budget
    # salary = doc.find_all("span",{"data-itemprop" : "baseSalary"})[0]
    # print(salary.text)

    return to_list(result)

