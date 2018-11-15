# SchoolLoop Connector
# @hkamran80

from bs4 import BeautifulSoup
import requests
import getpass
import datetime
import time

class SchoolLoopConnector:
  def __init__(self, subdomain, username, password):
    global s2, current_day, next_day

    day = ""
    tmr_day = ""

    if int(time.strftime("%d")) < 10:
      day = "0" + str(int(time.strftime("%d")))

    if int(time.strftime("%d"))+1 < 10:
      tmr_day = "0" + str(int(time.strftime("%d"))+1)

    c_day = time.strftime("%m") + "/" + str(day) + "/" + time.strftime("%Y")
    n_day = time.strftime("%m") + "/" + str(tmr_day) + "/" + time.strftime("%Y")

    self.current_day = c_day
    self.next_day = n_day

    self.ses = requests.session()
    r1 = self.ses.get("https://{}.schoolloop.com/portal/guest_home?d=x".format(subdomain))

    s1 = BeautifulSoup(r1.text, "html.parser")
    
    fdi = s1.find("form").find("input", {"id":"form_data_id"})["value"]

    cookies = {"JSESSIONID": r1.cookies["JSESSIONID"], "slid": r1.cookies["slid"]}
    payload = {"login_name": username, 'password': password, 'event_override': 'login', 'form_data_id': fdi}

    r2 = self.ses.post("https://{}.schoolloop.com/portal/guest_home?etarget=login_form".format(subdomain), cookies=cookies, data=payload)
    self.s2 = BeautifulSoup(r2.text, "html.parser")

  def homework(self):
    s2 = self.s2
    current_day = self.current_day
    next_day = self.next_day

    hw_list = []

    for hw in s2.find_all("table", {"class":"table_basic"}):
      hw_assignment = str(hw.find("td", {"class":"column padding_5 item_title"}).span.string).strip()
      hw_class = str(hw.find("td", {"class":"column padding_5"}).string).strip()

      hw_duedate = str(hw.find_all("td", {"class":"column padding_5 no_wrap"})[int(len(hw.find_all("td", {"class":"column padding_5 no_wrap"})))-1].string).strip()[5:]
      hw_dd = datetime.date(int(datetime.datetime.now().year), int(hw_duedate.split("/")[0]), int(hw_duedate.split("/")[1]))
      
      h2 = str(hw_dd).split("-")
      if h2[1] + "/" + h2[2] + "/" + h2[0] == current_day:
        hw_dt = 1
      elif h2[1] + "/" + h2[2] + "/" + h2[0] == next_day:
        hw_dt = 2
      else:
        hw_dt = 0

      hw_ddhro = h2[1] + "/" + h2[2] + "/" + h2[0]  
        
      hw_list.append([hw_assignment, hw_class, hw_dd, hw_dt, hw_ddhro])

    return hw_list

  def test(self):
    return self.s2

  def grades(self):
    s2 = self.s2

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
