import pandas as pd
from pymysql import MySQLError
import pymysql
import sqlalchemy as sal

# Initialize all global variables here
filePath = "C:/data_analysis_project/netflix_project/datasets/Netflix_Data_new.csv"

# Define all functions here
def loadCSVDataToDataFrame():
    # Load CSV data to data frame
    rawdataframe = pd.read_csv(filePath)

    # Drop unwanted colunms from Raw data frame and load it to different Data Frame and name it as CleanedDataFrame
    cleaneddataframe = rawdataframe.drop(columns=["Sub Genres", "Recommendations"])

    #data types of coloumns
    #print(cleaneddataframe.dtypes)

    # to seperate og audio from each row
    cleaneddataframe['Original Audio']
    #print(cleaneddataframe['Original Audio'])

    #lowercase the capital letters
    cleaneddataframe.columns=cleaneddataframe.columns.str.lower()
    #print( cleaneddataframe.columns)

    # replace space with _
    cleaneddataframe.columns=cleaneddataframe.columns.str.replace(' ','_')
    #print(cleaneddataframe.columns)

    #create a connection to mysql
    engine=sal.create_engine("mysql+pymysql://root:Gayathri_123@localhost/netflix") # type: ignore
    conn=engine.connect()

    #load data to MySQL
    cleaneddataframe.to_sql('netflix_database',con=conn,index=False,if_exists='append')


    # Print Cleaned Data 
    print(cleaneddataframe)

# Call functions here
loadCSVDataToDataFrame()

