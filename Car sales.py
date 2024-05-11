import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def Project():
    print(" WELCOME ")
    print(" TO ")
    print(" CAR SALES ANALYSIS SYSTEM")
    print(" =============================== ")
print("=========================================================")
print("")
print("Choose one choice: ")
print("1: For checking the data.")
print("2: Reading complete file without index.")
print(" ")
print("3: Line Chart")
print(" Press 1 to Display the Car Sales for the year 2019.")
print(" Press 2 to Display the Car Sales for the Year 2020.")
print(" Press 3 to Display the Car Sales for the Year 2021.")
print(" Press 4 to Display the Car Sales for the Year 2022")
print(" Press 5 to Display Overall Car Sales from 2019-2022")
print(" ")
print("4: Bar Graph")
print(" Press 1 to Display the Car Sales for the year 2019.")
print(" Press 2 to Display the Car Sales for the Year 2020.")
print(" Press 3 to Display the Car Sales for the Year 2021.")
print(" Press 4 to Display the Car Sales for the Year 2022")
print(" Press 5 to Display Overall Car Sales from 2019-2022")
print(" Press 6 to Display the Analysis in form of multi bar chart")
print(" ")
print("5: For Exit")
print("================================================================")
def Read_CSV():
   print("The Data")
   df=pd.read_csv('C:\\Users\\lavan\\Desktop\\coding\\Car sales project\\Data.csv')
   print(df)
def No_Index():
   print("Reading the file without index")
   df=pd.read_csv('C:\\Users\\lavan\\Desktop\\coding\\Car sales project\\Data.csv', index_col=0)
   print(df)

#FOR LINE CHART:)
def line_plot():
    df=pd.read_csv('C:\\Users\\lavan\\Desktop\\coding\\Car sales project\\Data.csv')
    df['COMPANY NAME'] = ['SKD','HYN','TATA','KIA','TOY','VW','FORD','REN','NIS']
    COMPANY=df["COMPANY NAME"]
    Y2019=df["2019"]
    Y2020=df["2020"]
    Y2021=df["2021"]
    Y2022=df["2022"]
    plt.xlabel("COMPANY")
    YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
    if YC == 1:
           plt.ylabel("Car Sales for the Year 2019")
           plt.title("Car Sales for the Year 2019")
           plt.plot(COMPANY, Y2019, color='b')
           plt.show()
    elif YC == 2:
          plt.ylabel("Car Sales for the Year 2020")
          plt.title("Car Sales for the Year 2020")
          plt.plot(COMPANY, Y2020, color='g')
          plt.show()
    elif YC == 3:
          plt.ylabel("Car Sales for the Year 2021")
          plt.title("Car Sales for the Year 2021")
          plt.plot(COMPANY, Y2021, color='r')
          plt.show()
    elif YC == 4:
          plt.title("Car Sales for the Year 2022")
          plt.plot(COMPANY, Y2022, color='c')
          plt.show()
    elif YC == 5:
          plt.ylabel("Summary of Car Sales from 2019 - 2022")
          plt.plot(COMPANY, Y2019, color='b', label = "Year 2019")
          plt.plot(COMPANY, Y2020, color='g', label = "Year 2020")
          plt.plot(COMPANY, Y2021, color='r', label = "Year 2021")
          plt.plot(COMPANY, Y2022, color='c', label = "Year 2022")
          plt.legend()
          plt.show()
    else:
          print("Enter valid input")
#FOR BAR GRAPH:)
def bar_plot():
    df = pd.read_csv('C:\\Users\\lavan\\Desktop\\coding\\Car sales project\\Data.csv')
    df['COMPANY NAME'] = ['SKD','HYN','TATA','KIA','TOY','VW','FORD','REN','NIS']
    COMPANY=df["COMPANY NAME"]
    Y2019=df["2019"]
    Y2020=df["2020"]
    Y2021=df["2021"]
    Y2022=df["2022"]
    plt.xlabel("COMPANY")
    YC = int(input("Enter the number representing your preferred bar graph from the above choices:"))
    if YC == 1:
            plt.ylabel("Car Sales for the Year 2019")
            plt.title("Car Sales for the Year 2019")
            plt.bar(COMPANY, Y2019, color='b', width = 0.5)
            plt.show()
    elif YC == 2:
            plt.ylabel("Car Sales for the Year 2020")
            plt.title("Car Sales for the Year 2020")
            plt.bar(COMPANY, Y2020, color='g', width = 0.5)
            plt.show()
    elif YC == 3:
            plt.ylabel("Car Sales for the Year 2021")
            plt.title("Car Sales for the Year 2021")
            plt.bar(COMPANY, Y2021, color='r', width = 0.5)
            plt.show()
    elif YC == 4:
            plt.ylabel("Car Sales for the Year 2022")
            plt.title("Car Sales for the Year 2022")
            plt.bar(COMPANY, Y2022, color='c', width = 0.5)
            plt.show()
    elif YC == 5:
            plt.bar(COMPANY, Y2019, color='b', width = 0.5, label = "Year 2019")
            plt.bar(COMPANY, Y2020, color='g', width = 0.5, label = "Year 2020")
            plt.bar(COMPANY, Y2021, color='r', width = 0.5, label = "Year 2021")
            plt.bar(COMPANY, Y2022, color='c',width = 0.5, label = "Year 2022")
            plt.legend()
            plt.show()
    elif YC == 6:
            D=np.arange(len(COMPANY))
            width=0.25
            plt.bar(D,Y2019, width, color='b', label = "Year 2019")
            plt.bar(D+0.25, Y2020, width, color='g', label = "Year 2020")
            plt.bar(D+0.50, Y2021, width, color='r', label = "Year 2021")
            plt.bar(D+0.75, Y2022 ,width, color='c', label = "Year 2022")
            plt.legend()
            plt.show()
    else:
            print("Enter valid input")
Project()
YC = int(input("Enter Your Choice: "))
while YC in [1, 2, 3, 4, 5]:
    if YC == 1:
       Read_CSV()
       break
    elif YC == 2:
       No_Index()
       break
    elif YC == 3:
       line_plot()
       break
    elif YC == 4:
       bar_plot()
       break
    elif YC == 5:
       print("Thank You for using...")
       break
    else:
       print("Enter valid input")
       break
    
print(" THANK YOU ")
