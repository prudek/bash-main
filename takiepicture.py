from PIL import Image,ImageEnhance,ImageDraw, ImageFont
import os
import time
import datetime
import schedule

basewidth = 1920

def takePicture():
    print("Taking picture...")

    os.system('raspistill -o /var/log/image.jpg')

    im = Image.open("/var/log/image.jpg")

    now = datetime.datetime.now()
    width, height = im.size

    draw = ImageDraw.Draw(im)
    now = datetime.datetime.now() + datetime.timedelta(hours=2)
    text = time.strftime('%H:%M:%S', now.timetuple())

    font = ImageFont.truetype("/opt/vc/src/hello_pi/hello_font/Vera.ttf", 72)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 5
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)

    enhancer = ImageEnhance.Sharpness(im)
    enhanced_im = enhancer.enhance(5.0)

    wpercent = (basewidth / float(enhanced_im.size[0]))
    hsize = int((float(enhanced_im.size[1]) * float(wpercent)))
    img = enhanced_im.resize((basewidth, hsize), Image.ANTIALIAS)

    img.save("/var/log/image_new.jpg", quality=50, optimize=True, progressive=True)


    dirDay = ('%04i.' % datetime.date.today().year)+('%02i.' % datetime.date.today().month)+('%02i' % datetime.date.today().day)
    dirMonth = ('%04i.' % datetime.date.today().year)+('%02i' % datetime.date.today().month)
    fileName = time.strftime('%Hh%Mm%Ss.jpg', now.timetuple())

    path_plus_filename = '/kamera2/' + dirMonth  + '/' + dirDay  + '/' + fileName

    file_size  = os.path.getsize('/var/log/image_new.jpg')
    print('file_size: ' + str(file_size))   

    if (file_size > 50000):
       os.system('/home/pi/dropbox_uploader.sh upload /var/log/image_new.jpg ' + path_plus_filename)


schedule.every(2).minutes.do(takePicture)

while True:
    schedule.run_pending()
    time.sleep(1)
