# SchoolLoop for Python
A Python module for accessing SchoolLoop!

To use, run `python3 setup.py install`. 
Then, open a Python console (`python3` in your terminal)
1. Type `import sl, getpass`.
2. Then type `loop = sl.SchoolLoopConnector(SCHOOLLOOP_SUBDOMAIN, SCHOOLLOOP_USERNAME, getpass.getpass())`. 

There are two functions (that can be called) in the `SchoolLoopConnector` class:
* `grades()`: Gets your grades. Returns LIST `[PERIOD_NUM, CLASS_NAME, TEACHER_NAME, GRADE, GRADE_LETTER]`
* `homework()`: Gets your homework. Returns LIST `[ASSIGNMENT, CLASS_NAME, DUE_DATE (DATETIME), DUE_TODAY (see __doc__), DUE_DATE (STR)]`