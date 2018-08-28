# SchoolLoop for Python
A Python module for accessing SchoolLoop!

To use, run `python3 setup.py install`. Then, open a Python console (`python3` in your terminal) and type `import sl_class as sl`. With that imported, you can type `loop = sl.SchoolLoopConnector(SCHOOLLOOP_SUBDOMAIN, SCHOOLLOOP_USERNAME, SCHOOLLOOP_PASSWORD)`. There are three functions in the `SchoolLoopConnector` class:
* `grades()`: Gets your grades. Returns LIST `[PERIOD_NUM, CLASS_NAME, TEACHER_NAME, GRADE, GRADE_LETTER]`
* `homework()`: Gets your homework. Returns LIST `[ASSIGNMENT, CLASS_NAME, DUE_DATE, UNKNOWN, UNKNOWN]`
* `test()`: Shows you the SchoolLoop portal HTML code.
