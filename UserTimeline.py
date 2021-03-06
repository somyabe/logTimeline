import csv
import re
import os
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from concurrent.futures import ThreadPoolExecutor
import time
import matplotlib.pyplot as plt
from keypress import keyDict
import traceback

def getMarkers(epoch1,epoch2,file_name):
    with open('strings_receiver.csv', 'r') as csv_file:
        text = csv.reader(csv_file)

        markerDict = []

        for line in text:
            line1 = " ".join(line)
            # print(line1)
            try:
                markerDict.append(line1)
            except:
                print("Failed to get markerDict!")
                pass
        print(markerDict)
    mainlist=[]
    count=0

    
    new_path = file_name
    print(new_path)

    def walk_through_files():
        for (dirpath, dirnames, filenames) in os.walk(new_path):

            for filename in filenames:
                #print(filename)

                if 'receiver' in filename:
                    #print(filename)
                    yield os.path.join(dirpath, filename)

    for fname in walk_through_files():
        #print(fname)
        a=open(fname ,'r',encoding="cp850")
        b=a.readlines()
        for word in markerDict:
            for line in b:
                if word in line:
                    st = re.compile(r'\d\d\d\d\s[a-zA-Z][a-zA-Z][a-zA-Z]\s\d\d\s\d\d.\d\d.\d\d.\d\d\d\d\d\d')
                    result = st.findall(line)
                    #print(line)
                    date = " ".join(result)
                    #print(date)
                    pattern = '%Y %b %d %H:%M:%S.%f'
                    try:
                        epoch3 = int(time.mktime(time.strptime(date, pattern)))
                        #print(epoch3)
                        #count=count+1
                        if epoch3>=epoch1 and epoch3<=epoch2:
                            #print(date)
                            #count=count+1
                            
                                
                                
                            
                            regex2 = re.compile('%s.+' %word)
                            result2=regex2.findall(line)
                            #print(result2)
                            mark = " ".join(result2)

                            list = []
                            list.append(date)
                            list.append(mark)
                            # list.append(x)
                            mainlist.append(list)
                            count=count+1
                            #print(mainlist)
                    #date = " ".join(result)
                    except:
                        pass

    return mainlist


def getPlaybackmode(mainlist):
    #for lines in mainlist:
    finalist = []
    for line in mainlist:
        try:
            if "playbackmode" in line[1]:
                if "tune request" in line[1]:

                    #print("request url")
                    if("ocap" in line[1]):

                        #line[1] = "Qam Linear"
                        word = "ocap://"
                        reg = re.compile('%s.+&res' % word)
                        result = reg.findall(line[1])
                        line[1] = "QAM Linear requested"
                        line.append(''.join(result)[7:-4])
                        line.append("Video")
                        line.append("blue")
                        line.append("triangle")
                        line.append("8")

                        #finalist.append(line)

                    elif("[VOD]" in line[1]):

                        if "HOST" in line[1]:
                            word="live"
                            reg = re.compile('%s.+&res' % word)
                            result = reg.findall(line[1])
                            line[1] = "VOD URL "
                            line.append(''.join(result)[4:-4])
                            line.append("Video")
                            line.append("blue")
                            line.append("triangle")
                            line.append("8")



                        else:

                            word = "net/"
                            reg = re.compile('%s.+/movie' % word)
                            result = reg.findall(line[1])
                            line[1] = "VOD URL"
                            line.append(''.join(result)[3:-6])
                            line.append("Video")
                            line.append("blue")
                            line.append("triangle")
                            line.append("8")

                        #finalist.append(line)

                    elif ("DVR" in line[1]):

                        if "recordingId" in line[1]:

                            word = "recordingId="
                            reg = re.compile('%s.+&seg' % word)
                            result = reg.findall(line[1])
                            line[1] = "DVR recording id= "
                            line.append(''.join(result)[12:-4])
                            line.append("Video")
                            line.append("blue")
                            line.append("triangle")
                            line.append("8")



                        else:
                            word = "cdvr-"
                            reg = re.compile('%s.+xcr' % word)
                            result = reg.findall(line[1])
                            line[1] = "DVR URL"
                            line.append(''.join(result)[5:-4])
                            line.append("Video")
                            line.append("blue")
                            line.append("triangle")
                            line.append("8")



                        #finalist.append(line)

                    elif("m3u8" in line[1]):
                        #line[1] = "Ip linear"
                        if '.net%2F' in line[1]:
                            word = ".net%2F"
                        elif '.com%2F' in line[1]:
                            word = ".com%2F"
                        reg = re.compile('%s.+?_' % word)
                        result = reg.findall(line[1])
                        line[1] = "IP Linear requested "
                        line.append(''.join(result)[7:-1])
                        line.append("Video")
                        line.append("blue")
                        line.append("triangle")
                        line.append("8")

                    else:
                        #print("no url")
                        continue


                    finalist.append(line)

                elif "succeeded" in line[1]:
                    line[1] = "Video Tune Succeeded"
                    line.append(" ")
                    line.append("Video")
                    line.append("green")
                    line.append("square")
                    line.append("8")
                    finalist.append(line)

                    #print("success url")
                elif "failed" in line[1]:
                    line[1] = "Video Failed"
                    line.append(" ")
                    line.append("Video")
                    line.append("red")
                    line.append("circle")
                    line.append("8")
                    finalist.append(line)

                elif "aborted" in line[1]:
                    if "http" in line[1]:
                        line[1] = "Video Aborted"
                        line.append(" ")
                        line.append("Video")
                        line.append("red")
                        line.append("circle")
                        line.append("8")
                        finalist.append(line)



            #elif "K E D" in line[1]:
                #finalist.append(line)
                #pass
            elif "HTML5 video" in line[1]:
                word = "mediasourceblob:"
                reg = re.compile('%s.+' % word)
                result = reg.findall(line[1])
                if "Loading" in line[1]:
                    line[1] = "Loading "
                    line.append(''.join(result)[16:-1])
                    line.append("Video")
                    line.append("blue")
                    line.append("triangle")
                    line.append("8")
                    finalist.append(line)

                elif "Pause" in line[1]:
                    line[1] = "Pause "
                    line.append(''.join(result)[16:-1])
                    line.append("Video")
                    line.append("blue")
                    line.append("triangle")
                    line.append("8")
                    finalist.append(line)
                elif "Playback started" in line[1]:
                    line[1] = "Playback started "
                    line.append(''.join(result)[16:-1])
                    line.append("Video")
                    line.append("blue")
                    line.append("triangle")
                    line.append("8")
                    finalist.append(line)

                elif "Playback terminated" in line[1]:
                    line[1] = "Playback terminated "
                    line.append(''.join(result)[16:-1])
                    line.append("Video")
                    line.append("red")
                    line.append("circle")
                    line.append("8")
                    finalist.append(line)
                    #finalist.append("receiver.log")
                elif "Play " in line[1]:
                    line[1] = "Play "
                    line.append(''.join(result)[16:-1])
                    line.append("Video")
                    line.append("blue")
                    line.append("triangle")
                    line.append("8")
                    finalist.append(line)

                else:
                    pass

            elif "Gibbon" in line[1]:
                if "GibbonOEM_Init" in line[1]:
                    line[1] = "Netflix initiated"
                    line.append(" ")
                    line.append("Video")
                    line.append("blue")
                    line.append("triangle")
                    line.append("8")
                    finalist.append(line)

                elif "Gibbon_Start" or "Gibbon_Started" in line[1]:
                    line[1]="Netflix started"
                    line.append(" ")
                    line.append("Video")
                    line.append("blue")
                    line.append("triangle")
                    line.append("8")
                    finalist.append(line)
            else:
                pass
        except:
            traceback.print_exc()
            pass

    return finalist

def getSettings(mainlist):
    finalist = []
    for line in mainlist:
        if "closedCaptioningEnabled enabled: true" in line[1]:

            line[1] = "closed captions enabled"
            line.append(" ")

            line.append("Settings")
            line.append("blue")
            line.append("triangle")
            line.append("8")
            finalist.append(line)

        elif "SAP changed" in line[1]:
            

            word = "SAP changed"
            reg = re.compile('%s....' % word)
            result = reg.findall(line[1])
            #result = " ".join(result)

            line[1] = "SAP changed to "
            line.append(" ".join(result)[13:])
            
            line.append("Settings")
            line.append("blue")
            line.append("triangle")
            line.append("8")
            finalist.append(line)
            

        else:
            pass

    return finalist

def getKeypresses(mainlist):
    finalist=[]
    for line in mainlist:

        if "virtualKeyCode" in line[1]:
            if "onKeyUp" in line[1]:


                word = "virtualKeyCode"
                reg = re.compile('%s([^,]+)' % word)
                result = reg.findall(line[1])
                
                line[1]="KEY_"
                line.append(" ".join(result)[3:-1])

                       


                if "ENTER" in line[1] or "GUIDE" in line[1]:



                    

                    line.append("Keypresses")


                    line.append("green")
                    line.append("square")
                    line.append("8")
                    finalist.append(line)

                else:
                    

                    line.append("Keypresses")

                    line.append("blue")
                    line.append("triangle")
                    line.append("8")
                    finalist.append(line)





       
    return finalist
    
def getnotifications(mainlist):
    finalist=[]
    for line in mainlist:
        if "RDK-" in line[1]:


            word = "RDK-"
            reg = re.compile('%s\d\d\d\d\d' % word)
            result = reg.findall(line[1])
            result = " ".join(result)
            if(result):

                line[1] = result
                line.append(" ")
                line.append("Notifications")
                line.append("red")
                line.append("cross")
                line.append("15")
                finalist.append(line)
            else:
                continue


        elif 'XRE_NR_STATUS' in line[1]:

            if 'SHELL' in line[1]:

                word="SHELL_STATUS="

            elif 'GUIDE' in line[1]:
                word = "GUIDE_STATUS="
            elif 'PLAYER' in line[1]:
                word ="PLAYER_STATUS="


            reg=re.compile('%s.+since' % word)
            result=reg.findall(line[1])
            result=" ".join(result)[:-6]


            line[1] = result
            if 'active' in line[1]:

                line.append(" ")
                line.append("Notifications")
                line.append("green")
                line.append("square")
                finalist.append(line)
            else:
                line.append(" ")

                line.append("Notifications")
                line.append("red")
                line.append("circle")
                finalist.append(line)

        elif 'RDKBROWSER_RENDER_PROCESS_CRASHED' in line[1]:
            line[1] = "RDK Browser crashed"
            line.append(" ")
            line.append("Notifications")
            line.append("red")
            line.append("cross")
            line.append("15")
            finalist.append(line)

        

        


        elif 'Pre-caching failed, renderer crashed' in line[1]:
            line[1] = "RENDERER_CRASHED"
            line.append(" ")
            line.append("Notifications")
            line.append("red")
            line.append("cross")
            line.append("15")
            finalist.append(line)

        elif 'core.prog_rtrmfplayer' in line[1]:
            line[1] = "RMFPLAYER_CRASHED"
            line.append(" ")
            line.append("Notifications")
            line.append("red")
            line.append("cross")
            line.append("15")
            finalist.append(line)

    return finalist






