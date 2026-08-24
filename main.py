# JEE MAINS KE NUMBER SE PERCENTILE NIKALNE KA TOOL
# student se uske total number (300 me se) puchhna 
marks = int(input("300 me se apne anumanit number dale: "))
# andaje se  percentile nikalne  ka logic (Linear approximation)
if marks >=250:
    percentile = 99.95

elif marks >=200:
    percentile = 99.5 + (marks-200) * 0.018

elif marks >=150:
    percentile = 98.0 + (marks-150) * 0.04

elif marks >=100:
    percentile = 90.0 + (marks-100) * 0.14

elif marks >=70:
    percentile = 80.0 + (marks-70) * 0.33

else:
    percentile = (marks / 70) * 80

# parinam ko screen par dikhana (round karke)
print("aapka anumanit percentile hai:", round(percentile, 2), "%")
