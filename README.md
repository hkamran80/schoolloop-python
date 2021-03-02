# SchoolLoop for Python
![Version](https://img.shields.io/badge/version-1.0.1-green?style=for-the-badge)
![Version](https://img.shields.io/badge/language-python%203-green?style=for-the-badge)   
A Python module for accessing SchoolLoop!

## NOTE: This module is no longer supported by the developer and has been archived.

To use, run `python3 setup.py install`. 
Then, open a Python console (`python3` in your terminal)
1. Type `import sl, getpass`.
2. Then type `loop = sl.SchoolLoopConnector(SCHOOLLOOP_SUBDOMAIN, SCHOOLLOOP_USERNAME, getpass.getpass())`. 

There are two functions (that can be called) in the `SchoolLoopConnector` class:
* `grades()`: Gets your grades. Returns LIST `[PERIOD_NUM, CLASS_NAME, TEACHER_NAME, GRADE, GRADE_LETTER]`
* `homework()`: Gets your homework. Returns LIST `[ASSIGNMENT, CLASS_NAME, DUE_DATE (DATETIME), DUE_TODAY (see __doc__), DUE_DATE (STR)]`
