import requests
from bs4 import BeautifulSoup
import pandas as pd

#declare empty list
job=[]
company=[]
location=[]
stipend=[]
jobskills=[]

#scraping data from 3 pages using for loop
for page in range(1,4):
    r=requests.get("https://internshala.com/internships/python-django-internship/page-"+str(page)+"/")
    soup = BeautifulSoup(r.text, "lxml")  #pagination using website url

    #extracting role of a job from website using class name and tag name
    role=soup.find_all("a",class_="job-title-href")
    for i in role:
        r1=i.text.strip()
        job.append(r1)

    #extracting company name from website using class name and tag name
    comp=soup.find_all("p",class_="company-name")
    for i in comp:
       c1=i.text.strip()
       company.append(c1)

    #extracting company location from website using class name and tag name
    loc=soup.find_all("div",class_="row-1-item locations")
    #location=[]
    for i in loc:
       l1=i.text.strip()
       location.append(l1)
    
    #extracting stipend from website using class name and tag name
    sti=soup.find_all("span",class_="stipend")
    for i in sti:
       s1=i.text.strip()
       stipend.append(s1)
    
    #extracting required skills from website using class name and tag name
    skills=soup.find_all("div",class_="job_skills")
    for i in skills:
        js1=i.text.strip()
        jobskills.append(js1)

#creating dataframe using pandas
df=pd.DataFrame({"JOB ROLE":job,
                 "COMPANY NAME":company,
                 "COMPANY LOCATION":location,
                 "INTERSHIP STIPEND":stipend,
                 "REQIRED SKILLS":jobskills })
print(df)
print(len(df))

#saving data into csv file
df.to_csv("scrap_project(Internshala).csv",index=False)