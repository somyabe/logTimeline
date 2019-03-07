import csv
import re
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from matplotlib.widgets import Slider
import time
from keypress import keyDict


def getMarkers():
        with open('strings_receiver.csv', 'r') as csv_file:
            text = csv.reader(csv_file)
            markerDict = {}
            markerDict[args.inputfile] = []
            for line in text:
                try:
                    #if line[1] not in markerDict.keys():
                    #markerDict[args.inputfile] = []
                    markerDict[args.inputfile].append(line[0])
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
            if "tune request" in line[1]:
                #print("request url")
                if("ocap" in line[1]):
                    #line[1] = "Qam Linear"
                    word = "ocap://"
                    reg = re.compile('%s.+&res' % word)
                    result = reg.findall(line[1])
                    line[1] = "QAM Linear"
                    line.append(''.join(result)[7:-4])
                    line.append("receiverlog")

                    finalist.append(line)

                elif("VOD" in line[1]):
                    word = "net/"
                    reg = re.compile('%s.+/movie' % word)
                    result = reg.findall(line[1])
                    line[1] = "VOD URL"
                    line.append(''.join(result)[3:-6])
                    line.append("receiverlog")

                    finalist.append(line)

                elif ("DVR" in line[1]):
                    word = "cdvr-"
                    reg = re.compile('%s.+xcr' % word)
                    result = reg.findall(line[1])
                    line[1] = "DVR URL"
                    line.append(''.join(result)[5:-4])
                    line.append("receiverlog")

                    finalist.append(line)

                elif("m3u8" in line[1]):
                    #line[1] = "Ip linear"
                    word = "m%2F"
                    reg = re.compile('%s.+_RG' % word)
                    result = reg.findall(line[1])
                    line[1] = "IP Linear"
                    line.append(''.join(result)[4:-6])
                    line.append("receiverlog")

                    finalist.append(line)

            elif "succeeded" in line[1]:
                line[1] = "Video Tune Succeeded"
                line.append(" ")
                line.append("receiverlog")
                finalist.append(line)

                #print("success url")
            elif "failed" in line[1]:
                line[1] = "Video Failed"
                line.append(" ")
                line.append("receiverlog")
                finalist.append(line)


        elif "K E D" in line[1]:
            #finalist.append(line)
            pass
        elif "HTML5 video" in line[1]:
            word = "mediasourceblob:"
            reg = re.compile('%s.+' % word)
            result = reg.findall(line[1])
            if "Loading" in line[1]:
                line[1] = "Loading"
                line.append(''.join(result)[16:-1])
                line.append("receiverlog")
                finalist.append(line)

            elif "Pause" in line[1]:
                line[1] = "Pause"
                line.append(''.join(result)[16:-1])
                line.append("receiverlog")
                finalist.append(line)
            elif "Playback started" in line[1]:
                line[1] = "Playback started"
                line.append(''.join(result)[16:-1])
                line.append("receiverlog")
                finalist.append(line)

            elif "Playback terminated" in line[1]:
                line[1] = "Playback terminated"
                line.append(''.join(result)[16:-1])
                line.append("receiverlog")
                finalist.append(line)
                #finalist.append("receiver.log")
            elif "Play " in line[1]:
                line[1] = "Play"
                line.append(''.join(result)[16:-1])
                line.append("receiverlog")
                finalist.append(line)

            else:
                pass

        elif "Gibbon" in line[1]:
            if "GibbonOEM_Init" in line[1]:
                line[1] = "Netflix initiated"
                line.append(" ")
                line.append("receiverlog")
                finalist.append(line)

            elif "Gibbon_Start" or "Gibbon_Started" in line[1]:
                line[1]="Netflix started"
                line.append(" ")
                line.append("receiverlog")
                finalist.append(line)
        else:
            pass


    return finalist

def getSettings(mainlist):
    finalist = []
    for line in mainlist:
        if "closedcaptions" in line[1]:

            line[1] = "closed captions"
            line.append(" ")

            line.append("receiverlog")
            finalist.append(line)

        elif "SAP" in line[1]:
            word = "SAP"
            reg = re.compile('%s.+' % word)
            result = reg.findall(line[1])
            result = " ".join(result)

            line[1] = result
            line.append(" ")
            line.append("receiverlog")
            finalist.append(line)

        else:
            pass

    return finalist

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--time',dest='time',type=str, help='input time')
    parser.add_argument('--span', dest='span',type=str, help='input duration')
    parser.add_argument('--inputfile', dest='inputfile',type=str, help='input file')
    args = parser.parse_args()

    #with open('time.csv', 'r') as e:
        #text = csv.reader(e)
        #for line in text:
    pattern = '%Y %b %d %H:%M:%S.%f'
    epoch1 = int(time.mktime(time.strptime(args.time, pattern)))
    int_dur=int(args.span)
    int_dur=int_dur*3600
    epoch2 = epoch1+int_dur
    #print(epoch1)
    #print(epoch2)

    mainlist = getMarkers()
    #print(mainlist)

    mlist = getPlaybackmode(mainlist)
    print(mlist)
    nlist=getSettings(mainlist)
    print(nlist)

    #olist=mlist+nlist


    try:
        df = pd.DataFrame(mlist)
        df1=pd.DataFrame(nlist)
        df.columns = ['dates', 'col1', 'col2','col3']
        df1.columns=['dates', 'col1', 'col2','col3']
        df = df.sort_values(by='dates')
        df1 = df1.sort_values(by='dates')
        #df1=df1.head(3)

        #ax = df.plot(kind='scatter', x='a', y='b',color = 'DarkBlue', label = 'Group 1')
        #for x in 'col3':

        #pt.scatter(df1['dates'],df1['col3'], color='DarkBlue')
        #pt.show()
        #df.plot(kind='scatter', x='dates', y='col3')
        #df = df.cumsum()



        df.to_csv('pro1.csv', index=False)
        df1.to_csv('pro.csv', index=False)

        df1["marker"] = df1["col1"] + df1["col2"]
        df["marker"] = df["col1"] + df["col2"]
        datelistdf1=list(df1.dates)
        datelistdf = list(df.dates)



        markerlistdf1=list(df1.marker)
        markerlistdf = list(df.marker)


        col3listdf1=list(df1.col3)
        col3listdf = list(df.col3)


        fig, ax = plt.subplots()
        ax.scatter(col3listdf, datelistdf)


        for i, txt in enumerate(markerlistdf):
            ax.annotate(txt, (col3listdf[i],datelistdf[i]))
        plt.show()

        fig, ax = plt.subplots()
        ax.scatter(col3listdf1, datelistdf1)

        for j, txt in enumerate(markerlistdf1):
            ax.annotate(txt, (col3listdf1[j],datelistdf1[j]))

        plt.show()
    except:
        print("Dataframe failed")




