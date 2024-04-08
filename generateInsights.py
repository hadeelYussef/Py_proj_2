
import pandas as pd, numpy as np

#--------------------------------------------
def readData(dataFile):
    if "csv" in dataFile:
        df = pd.read_csv(dataFile)
        print("csv file has been read successfully" )
        
    elif "json" in dataFile:
         df = pd.read_json(dataFile)
         print("json file has been read successfully" )
            
    elif "xlsx" in dataFile:
         df = pd.read_xlsx(dataFile)
         print("xlsx file has been read successfully" )
            
    elif "xml" in dataFile:
         df = pd.read_xml(dataFile)
         print("xml file has been read successfully" )
            
    elif "html" in dataFile:
         df = pd.read_html(dataFile)
         print("html file has been read successfully" )
            
    elif "excel" in dataFile:
         df = pd.read_excel(dataFile)
         print("excel file has been read successfully" )
        
    else:
        return "file format is not supported!"
            
    return df   

#--------------------------------------------
def getStaisticalData(carDataFrame):

    maxPricePerMake_df= carDataFrame.groupby("make", group_keys=True)[['sellingprice']].max()
    minPricePerMake_df= carDataFrame.groupby("make", group_keys=True)[['sellingprice']].min()
    firstManfYear=carDataFrame['year'].min()
    lastManfYear= carDataFrame['year'].max()
    #mean_price = carDataFrame.groupby(["make"]).mean()
    print("\n Here  is the minimum price list per manfcaturing company is: ", minPricePerMake_df)
    print("\n Here  is the maximum price list per manfcaturing company is: ", maxPricePerMake_df)
    print("\n Do you know that the first car was manfactured at : ", firstManfYear)
    print("\n and the last car was manfactured at : ", lastManfYear)
    return 1 # return True

#--------------------------------------------
def getDataForCertainYear(_year):
       
    #try:
    dataOftheYear=carDataFrame[carDataFrame['year']== _year ]
    print("the following data is filtered by your input year .. \n",dataOftheYear)
   #  except:
      # print( "the year you entered is not correct!")*/
    return 

#--------------------------------------------
def handleMissingValue(carDataFrame, typeOfHandling, replacedValue):
    
    if (typeOfHandling ==1):
        carDataFrame.fillna(replacedValue)
        print(" Missing values are successfully replace with  " , replacedValue, " \n")
    else :
        carDataFrame.dropna()
        print(" Missing values are successfully deleted \n")
    
    return carDataFrame

#--------------------------------------------
def encodeCategoricalDate(carDataFrame):
    makeList= carDataFrame['make'].value_counts()
    SUVCars=carDataFrame[ (carDataFrame["make"]== "Kia") | (carDataFrame["body"] == "SUV") ]
    yearseries= carDataFrame[carDataFrame['year']<1990]
    return makeList, SUVCars, yearseries
    
