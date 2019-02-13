import csv
import re
import pandas as pd
import matplotlib.pyplot as pt
from datetime import datetime , timedelta
with open('pro.csv', 'w') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['datetime','markers','filename'])
    markerDict = {}
    def getMarkers():
            with open('strings.csv', 'r') as csv_file:
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

                            st = re.compile(r'\d\d\d\d\s[a-zA-Z][a-zA-Z][a-zA-Z]\s\d\d\s\d\d.\d\d.\d\d.\d\d\d\d\d\d')
                            result = st.findall(line)
                            date = " ".join(result)
                            #l1.append(result)
                            #print(date,word,x)
                            list=[]
                            list.append(date)
                            list.append(word)
                            list.append(x)
                            mainlist.append(list)
                            count=count+1

            df = pd.DataFrame(mainlist)

            df.columns = ['datest', 'markers','filename']
            print(df)
            df.to_csv('pro.csv',  index=False)
            pt.scatter(df['datest'], df['markers'])
            pt.show()
#


    if __name__ == "__main__":
        getMarkers()
