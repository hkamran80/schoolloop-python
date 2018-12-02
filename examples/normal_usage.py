"""
Example SchoolLoop Connector Usage 1
Platform: All
Contributors:
  :: H. Kamran [@hkamran80] (author)

Version: 1.0.0
Last Updated: 2018-12-01, @hkamran80
"""

import getpass
import sl

sl_subdomain = input("SchoolLoop Subdomain: ")
sl_username = input("SchoolLoop Username: ")
sl_password = getpass.getpass(prompt="SchoolLoop Password: ")

loop = sl.SchoolLoopConnector(sl_subdomain, sl_username, sl_password)

print("Grades")
print(loop.grades())

print()

print("Homework")
print(loop.homework())