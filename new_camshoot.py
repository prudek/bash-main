import os
import schedule
import time
import datetime
#import numpy as np
#from SimpleCV import Image

previous = ""
current = ""

def takePicture():
    print("Taking picture...")
    dirDay = ('%04i.' % datetime.date.today().year)+('%02i.' % datetime.date.today().month)+('%02i' % datetime.date.today().day)
    dirMonth = ('%04i.' % datetime.date.today().year)+('%02i' % datetime.date.today().month)

    now = datetime.datetime.now() #+ datetime.timedelta(hours=2)
    fileName = time.strftime('%Hh%Mm%Ss.jpg', now.timetuple())

    #fileName = time.strftime('%Hh%Mm%Ss.jpg')
  
    if not os.path.exists('/mnt/var/www/webcam/' + dirMonth):
        print os.makedirs('/mnt/var/www/webcam/' + dirMonth)

    if not os.path.exists('/mnt/var/www/webcam/' + dirMonth + '/' + dirDay):
        print os.makedirs('/mnt/var/www/webcam/' + dirMonth + '/' + dirDay)

    os.system('wget -O /mnt/var/www/webcam/' + dirMonth  + '/' + dirDay  + '/' + fileName + ' http://admin:slonykapturek137@192.168.0.9/Streaming/channels/1/picture')	
    #global previous
    #global current
    #previous = current
    #current = '/mnt/var/www/webcam/' + dirMonth  + '/' + dirDay  + '/' + fileName	
   
 
    #if len(previous) > 0:
    #  sourceimg = Image(previous) 
    #  targetimg = Image(current)
    #  diffimg = sourceimg - targetimg
    #
    #  matrix = diffimg.getNumpy()
    #  flat = matrix.flatten()
    #  numchange = np.count_nonzero(flat)
    #  percentchange = 100 * float(numchange) / float(len(flat))
    # 
    #  with open('/mnt/var/www/webcam/' + dirMonth  + '/' + dirDay  + '/' + 'statystyka.txt', 'a') as myfile:
    #    myfile.write(current + '   '  + str(percentchange) + '%  \n')

schedule.every(6).minutes.do(takePicture)

while True:
    schedule.run_pending()
    time.sleep(1)
