from tabulate import tabulate

heading = ["Sr. No.", "Name"]
data = [[1, "John"], [2, "Jack"], [3, "Alice"], [4, "Bob"], [5, "James"]]

print(tabulate(data, headers = heading, tablefmt = "fancy_grid"))

'''
Table Formats:
1. plain
2. simple
3. github
4. grid
5. fancy_grid
6. pipe
7. orgtbl
8. jira
9. presto
10. pretty
11. psql
12. rst
13. mediawiki
14. moinmoin
15. youtrack
16. html
17. unsafehtml
18. latex
19. latex_raw
20. latex_booktabs
21. latex_longtable
22. textile
23. tsv
'''

#https://pypi.org/project/tabulate/
