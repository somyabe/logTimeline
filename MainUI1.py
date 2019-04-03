from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
import time
import UserTimeline1
import traceback
from datetime import datetime, timezone, date
from matplotlib import interactive
import tarfile
import os
import calendar



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(20, 130, 221, 16))
        self.label.setLineWidth(2)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 191, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 211, 16))
        self.label_3.setObjectName("label_3")
        self.datetime = QtWidgets.QLineEdit(self.centralwidget)
        self.datetime.setGeometry(QtCore.QRect(250, 126, 331, 19))
        self.datetime.setText("")
        self.datetime.setObjectName("datetime")
        self.duration_set_button = QtWidgets.QSpinBox(self.centralwidget)
        self.duration_set_button.setEnabled(True)
        self.duration_set_button.setGeometry(QtCore.QRect(250, 190, 33, 19))
        self.duration_set_button.setMouseTracking(False)
        self.duration_set_button.setWrapping(True)
        self.duration_set_button.setReadOnly(False)
        self.duration_set_button.setAccelerated(True)
        self.duration_set_button.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.duration_set_button.setKeyboardTracking(True)
        self.duration_set_button.setMinimum(1)
        #self.duration_set_button.setMaximum(6)
        self.duration_set_button.setSingleStep(1)
        self.duration_set_button.setProperty("value", 1)
        self.duration_set_button.setDisplayIntegerBase(10)
        self.duration_set_button.setObjectName("duration_set_button")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(250, 250, 56, 17))
        self.run_button.setObjectName("run_button")

        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(250, 160, 201, 20))
        self.filename.setObjectName("filename")




        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.run_button.clicked.connect(self.whenpressedrun)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter starting date and time:"))
        self.label_2.setText(_translate("MainWindow", "Enter file name:"))
        self.label_3.setText(_translate("MainWindow", "Duration(in hours):"))
        self.run_button.setText(_translate("MainWindow", "Run"))

    def whenpressedrun(self):
        date_str=self.datetime.text().strip()
        dur_str=self.duration_set_button.text()
        file_name=self.filename.text()
        #print("run pressed!")
        pattern = '%Y %b %d %H:%M:%S.%f'
        epoch1 = int(time.mktime(time.strptime(date_str, pattern)))
        int_dur = int(dur_str)
        int_dur = int_dur * 3600
        epoch2 = epoch1 - int_dur
        mainlist = UserTimeline1.getMarkers(epoch2, epoch1, file_name)
        mlist = UserTimeline1.getPlaybackmode(mainlist)
        print(mlist)

        nlist = UserTimeline1.getSettings(mainlist)
        print(nlist)
        olist=UserTimeline1.getKeypresses(mainlist)
        print(olist)

        qlist=UserTimeline1.getnotifications(mainlist)
        print(qlist)
        plist=mlist+nlist+qlist+olist
        print(plist)

        copy_list=plist.copy()
        #print(copy_list)
        temp_list = []

        try:

            #if(len(mlist)>0):

                #df = pd.DataFrame(mlist)
                #df.columns = ['dates', 'col1', 'col2', 'col3']
                #print(df)
                #df = df.sort_values(by='dates')
                #df["marker"] = df["col1"] + df["col2"]
                #datelistdf = list(df.dates)
                #markerlistdf = list(df.marker)
                #col3listdf = list(df.col3)
                #fig, ax = plt.subplots()

                #ax.scatter(datelistdf, col3listdf)

                #for i, txt in enumerate(markerlistdf):
                    #ax.annotate(txt, (datelistdf[i], col3listdf[i]))

                #if(len(nlist)!=0):

                    #interactive(True)
                #plt.show()

            #else:
                #print("No video records found")


            #if (len(olist) > 0):
                #df = pd.DataFrame(olist)
                #df.columns = ['dates', 'col1', 'col2']
                # print(df)
                #df = df.sort_values(by='dates')
                #df.to_csv('keypresses.csv', index=False)

            if(len(plist)>0):


                df1 = pd.DataFrame(plist)
                #df.columns = ['dates', 'col1', 'col2', 'col3']
                #print(df)
                df1.columns = ['dates', 'col1', 'col2', 'col3']

                #df1["marker"] = df1["col1"] + df1["col2"]
                #df1.columns = ['dates', 'marker', 'col3']
                #df = df.sort_values(by='dates')


                df1 = df1.sort_values(by='dates')
                pattern = '%Y %b %d %H:%M:%S.%f'



                for i in plist:
                    datetimeobj = datetime.strptime(i[0], pattern)
                    datetimeobj1 = datetimeobj.timestamp()*1000

                    temp_list.append(int(datetimeobj1))
                #print(temp_list)


                for i in range(len(temp_list)):
                    copy_list[i][0] = temp_list[i]

                for i in copy_list:
                    if i[3]=='Video':
                        i[3]='1'
                        #i.append("blue")
                    elif i[3]=='Notifications':
                        i[3]='2'
                        #i.append("green")
                    elif i[3]=='Settings':
                        i[3]='3'
                        #i.append("red")

                    elif i[3]=='Keypresses':
                        i[3]='4'
                        #i.append("yellow")



                print(copy_list)






                df1["marker"] = df1["col1"] + df1["col2"]
                del df1['col1']
                del df1['col2']


                #df.to_csv('videoTimeline.csv', index=False)
                df1.to_csv('Timeline.csv', index=False)

                dfgraph = pd.DataFrame(copy_list)
                dfgraph.columns = ['x', 'col1', 'col2', 'y']
                dfgraph["z"] = dfgraph["col1"] + dfgraph["col2"]
                del dfgraph['col1']
                del dfgraph['col2']
                dfgraph = dfgraph.sort_values(by='x')
                dfgraph.to_csv('forchart.csv', index=False, line_terminator=None)



                #df1["marker"] = df1["col1"] + df1["col2"]
                #df["marker"] = df["col1"] + df["col2"]
                datelistdf1 = list(df1.dates)
                #datelistdf = list(df.dates)

                markerlistdf1 = list(df1.marker)
                #markerlistdf1 = markerlistdf1.astype(str)
                #markerlistdf = list(df.marker)

                col3listdf1 = list(df1.col3)
                #col3listdf1 = col3listdf1.astype(str)
                #col3listdf = list(df.col3)
                #interactive(True)
                #self.first_graph(col3listdf,datelistdf,markerlistdf)
                #self.second_graph(col3listdf1,datelistdf1,markerlistdf1)


                fig, ax = plt.subplots()
                ax.scatter(datelistdf1, col3listdf1)

                fig.autofmt_xdate()

                for j, txt in enumerate(markerlistdf1):
                    ax.annotate(txt, (datelistdf1[j], col3listdf1[j]), rotation=10)
                #interactive(False)

                plt.show()
            else:
                print("No records found")



        except:
            print("Dataframe failed")
            traceback.print_exc()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
