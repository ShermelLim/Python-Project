#Title : Python Project
#Name : Shermel Lim
#Class : PN2004L
#Date : 13 Feb 2021
#Group Name : JAS

#import pandas
import pandas as pd 

#Class Function
class DataAnalysis:
  def __init__(self):
    MonthlyVisitors()

#Main Function
def MonthlyVisitors():
  df = pd.read_csv('MonthlyVisitors.csv')
  print(df.columns)
  #Picking out sperific range of countries and years
  years = df[['Year', 'Month',' Japan ',' Hong Kong ',' China ',' Taiwan ',' Korea, Republic Of ']][216:348]
  print(years)
  #Picking out sperific range of countries
  countries = df[[' Japan ',' Hong Kong ',' China ',' Taiwan ',' Korea, Republic Of ']][216:348]

  #Adding up the total sum of visitors
  TotalVisitors = countries.sum(axis=0)
  print(TotalVisitors)

  # arranging it by desecending order
  Top5 = TotalVisitors.sort_values(ascending=False)
  
  # Display the Top 3 countries visited
  print("These are the Top 3 coutries with the most visiotrs visting Singapore")
  print(Top5.head(3))

#Main code
if __name__=='__main__':
  DataAnalysis()

