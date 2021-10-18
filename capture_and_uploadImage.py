import cv2
import random
import dropbox
import time
start_time = time.time()
def screenshot():
    videoCaptureObject = cv2.VideoCapture()
    result = True
    number = random.randint(1,1000)
    while (result):
        ret,frame=videoCaptureObject.read()
        image_name = "img" + str(number) +".png"
        cv2.imwrite(image_name,frame)
        result=False
    return image_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def uploadFile(image):
    file_from= image
    file_to = "/securityFiles/"+image
    access_token ="sl.Amw_q3oaY0wOXKolVIZLKwA2kCKYMstMMrsxhTNA29CK-ePILbN8_OQKdSlH3rHaC5eE9bZzZUj6Y3XWb_ZghTTSsSajEpen2fuGbT-rxN2cjRlzULJ_oGB1TP5Z0WONVm9aNTk"
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as file1:
            dbx.files_upload(file1.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
    print("File Uploaded")
def main():
    while (True):
        if(time.time-start_time>=300):
            name=screenshot()
            uploadFile(name)
main()
