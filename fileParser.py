import csv
import re
import pandas as pd
import time
import matplotlib.pyplot as pt
from datetime import datetime , timedelta

with open('pro.csv', 'w') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['datetime','markers'])
    markerDict = {}
    def getMarkers():
            with open('strings_receiver.csv', 'r') as csv_file:
                text = csv.reader(csv_file)

                markerDict = {}
                for line in text:
                    if line[1] not in markerDict.keys():
                        markerDict[line[1]] = []
                    markerDict[line[1]].append(line[0])
            #print(markerDict)

            mainlist=[]
            count=0
            for x in markerDict:
                a=open(x ,'r')
                b=a.readlines()
                for word in markerDict[x]:
                    for line in b:
                        if word in line:
                            #print(line)
                            st = re.compile(r'\d\d\d\d\s[a-zA-Z][a-zA-Z][a-zA-Z]\s\d\d\s\d\d.\d\d.\d\d.\d\d\d\d\d\d')
                            result = st.findall(line)
                            #print(result)
                            #print(date)

                            #print(date)
                            count=count+1
                            regex2 = re.compile('%s.+' %word)
                            result2=regex2.findall(line)
                            #print(result2)
                            date = " ".join(result)
                            mark=" ".join(result2)
                            #l1.append(result)
                            #print(date,word,x)
                            list=[]
                            list.append(date)
                            list.append(mark)
                            #list.append(x)
                            mainlist.append(list)

            print(count)
            df = pd.DataFrame(mainlist)
            df.columns = ['datest', 'markers']
            df = df.sort_values(by='datest')
            print(df)
            df.to_csv('pro.csv',  index=False)

#


    if __name__ == "__main__":
        getMarkers()
