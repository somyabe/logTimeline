import csv
import re
import pandas as pd
import time

from keypress import keyDict


def getMarkers():
        with open('strings_receiver.csv', 'r') as csv_file:
            text = csv.reader(csv_file)
            markerDict = {}
            for line in text:
                try:
                    if line[1] not in markerDict.keys():
                        markerDict[line[1]] = []
                    markerDict[line[1]].append(line[0])
                except:
                    print("Got markerDict!")
                    pass
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
                        #print(result)
                        date = " ".join(result)
                        #print(date)
                        pattern = '%Y %b %d %H:%M:%S.%f'
                        epoch3 = int(time.mktime(time.strptime(date, pattern)))
                        #print(epoch3)
                        #count=count+1
                        if epoch3>=epoch1 and epoch3<=epoch2:
                            #print(date)
                            #count=count+1
                            if word=="XREKeyPressLog":
                                regex2 = re.compile('%s.+' % word)
                                result2 = regex2.findall(line)
                                split1=result2[0].split(" ")
                                rr=split1[3]
                                #print(rr)
                                if(rr in keyDict):
                                    #print(keyDict[rr])
                                    #count=count+1
                                    mark = " ".join(keyDict[rr])
                                    list = []
                                    list.append(date)
                                    list.append(mark)
                                    # list.append(x)
                                    mainlist.append(list)
                                #print(result2)
                            else:
                                regex2 = re.compile('%s.+' %word)
                                result2=regex2.findall(line)
                                #print(result2)
                                mark = " ".join(result2)
                                count=count+1
                                list = []
                                list.append(date)
                                list.append(mark)
                                # list.append(x)
                                mainlist.append(list)
                        #date = " ".join(result)
        return mainlist

def getPlaybackmode(mainlist):
    #for lines in mainlist:
    finalist = []
    for line in mainlist:
        if "playbackmode" in line[1]:
            if "request" in line[1]:
                #print("request url")
                if("ocap" in line[1]):
                    line[1] = "Qam Linear"
                    finalist.append(line)
                elif("m3u8" in line[1]):
                    line[1]="Ip linear"
                    finalist.append(line)
            elif "succeeded" in line[1]:
                pass
                #print("success url")
        else:
            #finalist.append(line)
            pass
    return finalist

if __name__ == "__main__":
    with open('time.csv', 'r') as e:
        text = csv.reader(e)
        for line in text:
            pattern = '%Y %b %d %H:%M:%S.%f'
            epoch1 = int(time.mktime(time.strptime(line[0], pattern)))
            epoch2 = int(time.mktime(time.strptime(line[1], pattern)))

    mainlist = getMarkers()

    mlist = getPlaybackmode(mainlist)
    print(mlist)
    df = pd.DataFrame(mainlist)
    df.columns = ['datest', 'markers']
    df = df.sort_values(by='datest')
    #print(df)
    df.to_csv('pro.csv', index=False)