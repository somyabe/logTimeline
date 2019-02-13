from datetime import datetime , timedelta
import csv
def find(filename, word, time,dur):
    a = open(filename, 'r')
    b = a.readlines()
    a.close()
    with open('pump.csv' , 'w') as f:
        thewriter=csv.writer(f)
        thewriter.writerow(['datetime'])
        time = '2018 dec 08 18:50'
        time1 = datetime.strptime(time, '%Y %b %d %H:%M')
        hour = time1.hour
        hour1 = str(hour)
        min = time1.minute
        td = timedelta(minutes=2)
        x = time1 - td
        less = x.minute
        for minCount in range(less, min + 1, 1):
            searchString = str(hour1) +":"+ str(minCount)
            result = [m for m in b if searchString in m ]
            if (result):
                print(result)
                thewriter.writerow(result)



if __name__ == "__main__":

    find("receiver.log", "virtualKeyCode", "2018 dec 08 06:48", "2")