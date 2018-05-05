# SchoolLoop for Python
A Python module for accessing SchoolLoop!

# Documentation
**Login function MUST be declared before running ANY functions**    
**ONLY TESTED WITH STUDENT ACCOUNTS!**

1. Install
* In your terminal:   
  i. `git clone https://github.com/hkamran80/schoolloop-python`
  ii. `cd schoolloop-python`
  iii. `python3 setup.py install`

2. REQUIRED: Logging in
* To login: `s2 = sl.login({YOUR_SCHOOLLOOP_SUBDOMAIN}, {YOUR_SCHOOLLOOP_USERNAME}, {YOUR_SCHOOLLOOP_PASSWORD})`. The variable MUST be `s2` (see [Bug #1](https://github.com/hkamran80/schoolloop-python/issues/1) under [Issues](https://github.com/hkamran80/schoolloop-python/issues)).
* `login` function returns `bs4` HTML
3. Get grades
* `grades = sl.get_grades()`. Variable can be anything
* Returns list: `[Period Number, Class Name, Teacher's Name, Grade (percentage), Grade Letter]`
4. Get homework
* `homework = sl.get_homework()`. Variable can be anything
* Returns list: `[Assignment`, `Class`, `DueDate`, `Due]`. `DueDate` is a STRING formatted: `{YEAR}-{MONTH}-{DAY}`. `Due` is an INTEGER (0 = Not due in next two days, 1 = Due today, 2 = Due tomorrow).

# Examples
1. [Get homework](https://gist.github.com/hkamran80/9d01de3330a618cb9f571e98bf8c17c3)
2. [Get grades](https://gist.github.com/hkamran80/48560245bf111d7c9a86e518cbcf9cf1)
