import pandas as pd
from collections import OrderedDict
import datetime

# Preparing naming convention for resulted files , naming convention depends on file name ,date & time when script
# executed .
filename_prefix = "Test-"
Gender_index = "GenderIndex"
Team_index = "TeamIndex"
today_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = str(filename_prefix + str(today_time)).replace(":", "-")
Gender_file_index = str(Gender_index + str(today_time)).replace(":", "-")
Team_file_index = str(Team_index + str(today_time)).replace(":", "-")
# Setting pandas to display all data(rows , columns ) in case to examine the datafram in full scale with print command.
pd.set_option("display.max_rows", None, "display.max_columns", None)
# Reading the given .csv file and transform the data into pandas.
Employees = pd.read_csv("employees.csv")
# Removing the 1st column labeled (First Name) from the dataframe.
Employees = Employees.drop(columns="First Name")
# Creating dictionary from (Teams) column list ,removing duplications and assigning ordered key automatically.
Team_dict = dict(enumerate(list(OrderedDict.fromkeys(Employees["Team"].tolist()))))
# Reversing keys and Values in order to replace items in dataframe with assigned keys.
Team_dict_Rev = {value: key for (key, value) in Team_dict.items()}
# Creating dictionary from (Gender) column list,removing duplications and assigning ordered key automatically.
Gender_dict = dict(enumerate(list(OrderedDict.fromkeys(Employees["Gender"].tolist()))))
# Reversing keys and Values in order to replace items in dataframe with assigned keys.
Gender_dict_Rev = {value: key for (key, value) in Gender_dict.items()}
# Transforming (Teams) , (Gender) dictionaries into dataframe in order to export as csv files for reference.
Genderindex = pd.DataFrame(Gender_dict_Rev.items())
Teamindex = pd.DataFrame(Team_dict_Rev.items())
# Creating new dataframe in order to replace (Teams), (Gender) columns items with keys from previous created
# dictionaries
df = pd.DataFrame(Employees)
df = df.replace({"Gender": Gender_dict_Rev})
df = df.replace({"Team": Team_dict_Rev})
# Calculating the Mean value for (Salary) , (Bonus %) columns .
Salary_mean = df["Salary"].mean()
Bonus_mean = df["Bonus %"].mean()
# Replacing empty values in both columns with their own Mean value
df["Salary"] = df["Salary"].fillna(Salary_mean)
df["Bonus %"] = df["Bonus %"].fillna(Bonus_mean)
# Using naming convention to creat output files ,Test, Gender index , Teams index.
Genderindex.to_csv(("{}.csv".format(Gender_file_index)), header=False, index=False)
Teamindex.to_csv(("{}.csv".format(Team_file_index)), header=False, index=False)
df.to_csv(("{}.csv".format(filename)), header=True, index=True)

print("Thanks")
