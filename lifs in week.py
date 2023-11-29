age=input("Enter your curretnt age:")

age_as_integer=int(age)

year_remaining=90-age_as_integer
days_remaining=year_remaining*365
weeks_remaining=year_remaining*52
months_remaining=year_remaining*12

message=f"The number of days remaining{days_remaining},The number of weeks remaining{weeks_remaining},The number of months remaining{months_remaining}"
print(message)
