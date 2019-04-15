import pandas as pd
import UserTimeline
import tarfile
import os
import traceback
import time
from datetime import datetime


def startApp(fileName,logPath,issueTime,searchSpan):
    date_str=issueTime
    dur_str=searchSpan
    file_name=fileName
    log_path=logPath
    
    with tarfile.open(file_name, "r:gz") as tar:
        tar.extractall(path=log_path)

    pattern = '%Y %b %d %H:%M:%S.%f'
    epoch1 = int(time.mktime(time.strptime(date_str, pattern)))
    int_dur = int(dur_str)
    int_dur = int_dur * 3600
    epoch2 = epoch1 - int_dur
    mainlist = UserTimeline.getMarkers(epoch2, epoch1, log_path)
    mlist = UserTimeline.getPlaybackmode(mainlist)
    print(mlist)
    nlist = UserTimeline.getSettings(mainlist)
    print(nlist)
    olist=UserTimeline.getKeypresses(mainlist)
    print(olist)
    qlist=UserTimeline.getnotifications(mainlist)
    print(qlist)
    plist=mlist+nlist+qlist+olist
    print(plist)
    copy_list=plist.copy()
    temp_list = []
    try:

        if(len(plist)>0):
            df1 = pd.DataFrame(plist)          
            df1.columns = ['dates', 'col1', 'col2', 'col3', 'color', 'markerType']
            df1 = df1.sort_values(by='dates')
            pattern = '%Y %b %d %H:%M:%S.%f'

            for i in plist:
                datetimeobj = datetime.strptime(i[0], pattern)
                datetimeobj1 = datetimeobj.timestamp()*1000
                temp_list.append(int(datetimeobj1))
            

            for i in range(len(temp_list)):
                copy_list[i][0] = temp_list[i]

            for i in copy_list:
                if i[3]=='Video':
                    i[3]=1
                elif i[3]=='Notifications':
                    i[3]=2
                elif i[3]=='Settings':
                    i[3]=3
                elif i[3]=='Keypresses':
                    i[3]=4
            print(copy_list)
            df1["marker"] = df1["col1"] + df1["col2"]
            del df1['col1']
            del df1['col2']
            
            df1.to_csv('Timeline.csv', index=False)

            dfgraph = pd.DataFrame(copy_list)
            dfgraph.columns = ['x', 'col1', 'col2', 'y', 'color', 'markerType']
            dfgraph["z"] = dfgraph["col1"] + dfgraph["col2"]
            del dfgraph['col1']
            del dfgraph['col2']
            dfgraph = dfgraph.sort_values(by='x')
            columnsTitles = ["x", "y", "z", "color", "markerType"]
            df = dfgraph.reindex(columns=columnsTitles)
            df.to_csv('forchart.csv', index=False, line_terminator=None)
            jsList = df.to_dict('index')
            return jsList

        else:
            print("No records found")
    except:
        print("Dataframe failed")
        traceback.print_exc()
