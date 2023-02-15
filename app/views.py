from django.shortcuts import render,redirect
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from .models import Attendence

# Create your views here.

def Home(request):
    return render(request,'index.html')



def ViewAttend(request):
    if request.method=="POST":
        studentID=request.POST.get('stdID')
        std=Attendence.objects.filter(std_id=studentID)
        print(std)
        context={
            'student':std
        }
        return render(request,'viewattend.html',context)
    else:
        return render(request,'viewattend.html')

def AddStudent(request):
    if request.method=="POST":
        stdname=request.POST.get('stdID')
        print(stdname)
        try:
            takeimage(stdname)
        except:
            return redirect("/")
    return render(request,'addstd.html')



def takeimage(stdname):
    name = stdname

    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)
    x=True

    while x==True:
        try:

            check, frame = webcam.read()
            # print(check) #prints true as long as the webcam is running
            # print(frame) #prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                # image=cv2.inwrite(filename='{}.jpg'.format(name),img=frame)
                # img=StudentImage(std_id=name,image=cv2.inwrite(filename='{}.jpg'.format(name),img=frame))
                # img.save()

                cv2.imwrite(filename='image/{}.jpg'.format(name), img=frame)
                webcam.release()
                img_new = cv2.imread('image/{}.jpg'.format(name), cv2.IMREAD_GRAYSCALE)
                x=False
                # img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('image/{}.jpg'.format(name), cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                # print("Converted RGB image to grayscale...")
                # print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray, (1920, 1820))
                # print("Resized...")
                # img_resized = cv2.imwrite(filename='E:\\project codes\\111\\dataset\\{}-final.jpg'.format(name), img=img_)
                img_resized = cv2.imwrite(filename='E:\\test\\{}-final.jpg'.format(name), img=img_)
                print("Image saved!")

            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break


def TakeAttendence(request):
