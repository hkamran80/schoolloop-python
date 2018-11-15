# SchoolLoop Connector for Python 3 -- UNOFFICIAL
# Written by H. Kamran (@hkamran80)

from bs4 import BeautifulSoup as bs
import requests
import getpass
import datetime
import time

args = []

def get_date():
  day = ""
  tmr_day = ""
  
  if int(time.strftime("%d")) < 10: 
    day = "0" + str(int(time.strftime("%d")))
   
  if int(time.strftime("%d"))+1 < 10:
    tmr_day = "0" + str(int(time.strftime("%d"))+1)

  current_day = time.strftime("%m") + "/" + str(day) + "/" + time.strftime("%Y")
  next_day = time.strftime("%m") + "/" + str(tmr_day) + "/" + time.strftime("%Y")
  
  return [current_day, next_day]

def login(subdomain, username, password):
  global args

  args.append(subdomain)
  args.append(username)
  args.append(password)

  r1 = requests.get(("https://" + args[0] + ".schoolloop.com/portal/guest_home?d=x"))
  s1 = bs(r1.text, "html.parser")

  form_data_id = s1.find("input", {"id": "form_data_id"})["value"]
  cookies_sent = {"JSESSIONID": r1.cookies["JSESSIONID"], "slid": r1.cookies["slid"]}
  payload = {"login_name": args[1], 'password': args[2], 'event_override': 'login', 'form_data_id': form_data_id}

  r2 = requests.post(("https://" + args[0] + ".schoolloop.com/portal/guest_home?etarget=login_form"), cookies=cookies_sent, data=payload)
  return bs(r2.text, "html.parser")

def get_grades():
  global s2
  
  grades = []
  
  for row in s2.find_all("table", {"class": "student_row"}):
    period = int(row.find("td", {"class":"period"}).string)
    class_name = str(row.find("td", {"class": "course"}).a.text)
    
    teacher_name = str(row.find("td", {"class": "teacher co-teacher"}).a.text).strip().split(", ")[1] + " " + str(row.find("td", {"class": "teacher co-teacher"}).a.text).strip().split(", ")[0]

    try:
      grade = float(row.find("div", {"class": "percent"}).text.replace("%", ""))
    except AttributeError:
      grade = "No grades published by teacher"
      
    try:
      grade_letter = str(row.find("div", {"class":"float_l grade"}).string)
    except AttributeError:
      grade_letter = ""

    grades.append([period, class_name, teacher_name, grade, grade_letter])
    
  return grades

def get_homework():
  global s2, current_day, next_day
  
  hw_list = []
  
  for hw in s2.find_all("table", {"class":"table_basic"}):
    hw_assignment = str(hw.find("td", {"class":"column padding_5 item_title"}).span.string).strip()
    hw_class = str(hw.find("td", {"class":"column padding_5"}).string).strip()

    hw_duedate = str(hw.find_all("td", {"class":"column padding_5 no_wrap"})[int(len(hw.find_all("td", {"class":"column padding_5 no_wrap"})))-1].string).strip()[5:]
    hw_dd = datetime.date(int(datetime.datetime.now().year), int(hw_duedate.split("/")[0]), int(hw_duedate.split("/")[1]))

    if h2[1] + "/" + h2[2] + "/" + h2[0] == current_day:
      hw_dt = 1
    elif h2[1] + "/" + h2[2] + "/" + h2[0] == next_day:
      hw_dt = 2
    else:
      hw_dt = 0
    
    hw_list.append([hw_assignment, hw_class, hw_dd, hw_dt])
    
  return hw_list
