import glob
import os
import pandas as pd
import re

## Class Deduple for Initializing and Routing
class DeDuple:
    def __init__(self,path):
        self.path = path
        self.df = pd.DataFrame(index=range(1,10))
        self.MainList = []
        self.LoadDf()
        self.Last5()
        self.Last4()
        self.DelFile()
    
    ## Loading filenames onto a Pandas Dataframe
    def LoadDf(self):
        names = [os.path.basename(x) for x in glob.glob(self.path)]
        if len(names) == 0:
            print("Folder Empty")
            return
        self.names = glob.glob(self.path)
        asd = [i.split("_")[2].replace(".txt","") for i in names] 
        df = pd.DataFrame(asd)
        self.df = df

    ## Function to Grab Last 5 days and Last day of the Month
    def Last5(self):
        if self.df.empty:
            print('DataFrame is empty!')
            return
        df = self.df
        df['Date']=pd.to_datetime(df[0])
        df.sort_values(by=['Date'], inplace=True, ascending=True)
        df["day"] = df['Date'].dt.dayofweek
        df2 = df.loc[df["Date"].dt.is_month_end]
        lastday = df2[0].tolist()
        last5 = df[0].tail(5).tolist()
        self.MainList.extend(last5 + lastday)

    ## Function to grab Last 4 Saturdays
    def Last4(self):
        if self.df.empty:
            print('DataFrame is empty!')
            return
        df = self.df
        df['Date']=pd.to_datetime(df[0])
        df.sort_values(by=['Date'], inplace=True, ascending=True)
        df["day"] = df['Date'].dt.dayofweek
        satDay = df.loc[df['day'] == 5]
        last4 =  satDay.tail(4)[0].tolist()
        self.MainList.extend(last4)

    ## Function to Delete the rest    
    def DelFile(self):
        suffix = self.names[0].split("\\")[1].split("_")[0]
        file_name = [suffix+"_backup_"+i+".txt" for i in self.MainList]
        for filename in self.names:
            if filename.split("\\")[1] not in file_name:
                os.remove(filename)
        
## Provide Path for the Folder
## Example : r"Data backup task/bucket1/*.txt"
Path = r"/*.txt"
DeDuple(Path)
