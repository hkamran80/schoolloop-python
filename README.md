# SchoolLoop for Python
A Python module for accessing SchoolLoop!

# Documentation
**Login function MUST be declared before running ANY functions**

1. REQUIRED: Logging in
* To login: `s2 = sl.login({YOUR_SCHOOLLOOP_SUBDOMAIN}, {YOUR_SCHOOLLOOP_USERNAME}, {YOUR_SCHOOLLOOP_PASSWORD})`. The variable MUST be `s2` (see [Bug #1](https://github.com/hkamran80/schoolloop-python/issues/1) under [Issues](https://github.com/hkamran80/schoolloop-python/issues)).
* `login` function returns `bs4` HTML
2. Get your grades
* `grades = sl.get_grades()`. Variable can be anything
* Returns list: `[Period Number, Class Name, Teacher's Name, Grade (percentage), Grade Letter]`
3. Get your homework
* `homework = sl.get_homework()`. Variable can be anything
* Return list: `[Assignment`, `Class`, `DueDate`, `Due]`. `DueDate` is a STRING formatted: `{YEAR}-{MONTH}-{DAY}`. `Due` is an INTEGER (0 = Not due in next two days, 1 = Due today, 2 = Due tomorrow).

# Examples
1. Get your homework
`import sl
from getpass import getpass

schoolloop_subdomain = input("Subdomain: ")
schoolloop_username = input("Username: ")
schoolloop_password = getpass()
s2 = login(schoolloop_subdomain, schoolloop_username, schoolloop_password)

homework = sl.get_homework()
for h in homework:
  if h[4] == 1:
    print(h[0] + " in " + h[1] + " due TODAY!" )
  elif h[4] == 2:
    print(h[0] + " in " + h[1] + " due TOMORROW!")
  elif h[4] == 0:
    print(h[0] + " in " + h[1] + " due " + h[2])
`

2. Get your grades
`import sl
from getpass import getpass

schoolloop_subdomain = input("Subdomain: ")
schoolloop_username = input("Username: ")
schoolloop_password = getpass()
s2 = login(schoolloop_subdomain, schoolloop_username, schoolloop_password)

grades = sl.get_grades()
for g in grades:
   if str(g[3]) == "No grades published by teacher":
      g_letter = ""
   else:
      g_letter = " (" + str(g[4]) + ")"
   print(str(g[0]) + "°: " + str(g[1]) + " (" + str(g[2]) + "): " + str(g[3]) + g_letter)
`
