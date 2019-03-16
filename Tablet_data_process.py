##!/usr/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Sat Dec 22 15:25:44 2018
#
#@author: neeru
#"""
#
#import scipy.io
#startTime = scipy.io.loadmat('startTime.mat')
#gazePts = scipy.io.loadmat('gazePts.mat')
#
#
##import matplotlib.pyplot as plt
#import cv2
#import math
#import os
#
#resultdir = 'Frames'
#a=0
#for path, dirs, files in os.walk('/home/neeru/Neeru/shreya_neeru/Face-master/TabletGaze/videos'):
#    for d in dirs:
#        print(d)
#        if a>2:
#            break
#        else:
#            a+=1
#            b=0
#            subdir = os.path.join(resultdir, d)
#            if not os.path.exists(subdir):
#                os.makedirs(subdir)
#            for p,di,filenames in os.walk(os.path.join(path, d)):
#                for filename in filenames:
#                    if filename.endswith('.mp4'):
#                        b+=1
#                        vidcap = cv2.VideoCapture(os.path.join(path, d,filename))
#                        success,image = vidcap.read()
#                        frame_no = 0
#                        success = True
#                        fps = vidcap.get(cv2.CAP_PROP_FPS)
#                        fps = int(fps)
#                        subject_id = filename[0]
#                        trial_id = filename[2]
#                        pos_id = filename[4]
#
#                        start_time = startTime['startTime'][int(subject_id)-1,int(trial_id)-1,int(pos_id)-1]
#                        frames_to_skip = math.ceil(start_time)*fps
#                        gaze=0
#                        skip_counter=0
#
#                        while success:
#                            if frame_no < frames_to_skip:
#                                success,image = vidcap.read()
#                                frame_no+=1
#                            else:
#                                gaze+=1
#                                if gaze >35:
#                                    break
#                                print(b,gaze)
#                                x = fps*3
#                                copy=0
#                                for i in range (x):
#                                    success,image = vidcap.read()
#                                    if success:
#                                        frame_no+=1
#                                        if i in (int(x/2-10),int(x/2-5),int(x/2),int(x/2+10)):
#                                            cv2.imwrite(subdir+'/'+filename[:-4]+'_'+str(gaze)+'_'+str(copy)+'.jpg',image)
#                                            copy+=1
#
#
#
#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:25:44 2018

@author: neeru
"""

import scipy.io
startTime = scipy.io.loadmat('startTime.mat')
gazePts = scipy.io.loadmat('gazePts.mat')


#import matplotlib.pyplot as plt
import cv2
import math
import os
import dlib

resultdir = 'Frames'
a=0
for path, dirs, files in os.walk('/home/neeru/Neeru/shreya_neeru/Face-master/TabletGaze/videos'):
    for d in dirs:
        print(d)
        if a>2:
            break
        else:
            a+=1
            b=0
            subdir = os.path.join(resultdir, d)
            if not os.path.exists(subdir):
                os.makedirs(subdir)
            for p,di,filenames in os.walk(os.path.join(path, d)):
                for filename in filenames:
                    if filename.endswith('.mp4'):
                        b+=1
                        vidcap = cv2.VideoCapture(os.path.join(path, d,filename))
                        success,image = vidcap.read()
                        frame_no = 0
                        success = True
                        fps = vidcap.get(cv2.CAP_PROP_FPS)
                        fps = int(fps)
                        subject_id = filename[0]
                        trial_id = filename[2]
                        pos_id = filename[4]



                        start_time = startTime['startTime'][int(subject_id)-1,int(trial_id)-1,int(pos_id)-1]
                        frames_to_skip = math.ceil(start_time)*fps
                        gaze=0
                        skip_counter=0

                        while success:
                            if frame_no < frames_to_skip:
                                success,image = vidcap.read()
                                frame_no+=1
                            else:
                                gaze+=1
                                if gaze >35:
                                    break
                                print(b,gaze)
                                x = fps*3
                                copy=0
                                for i in range (x):
                                    success,image = vidcap.read()
                                    if success:
                                        frame_no+=1
                                        if i in (int(x/2-10),int(x/2-5),int(x/2),int(x/2+10)):
                                            facedetector = dlib.get_frontal_face_detector()
                                            faces, scores, types = facedetector.run(image, 0)
                                            if len(faces) == 0:
                                                print("Can not detect face")
                                                direction_pose='Can not detect face'
                    #                            file.write(str(frame_number)+"        "+direction_pose+"\n")
                                                continue

                                            if len(faces)>1:

                                                faces0 = [faces[0]]
                                                face0 = faces0[0]
                                                faces1 = [faces[1]]
                                                face1 = faces1[0]
                                                top0, bottom0, left0, right0 = face0.top(), face0.bottom(), face0.left(), face0.right()
                                                top1, bottom1, left1, right1 = face1.top(), face1.bottom(), face1.left(), face1.right()

                                                width0 = abs(top0-bottom0)
                                                width1 = abs(top1-bottom1)
                                                height0 = abs(right0-left0)
                                                height1 = abs(right1-left1)

                                                area0=width0*height0
                                                area1=width1*height1

                                                if area0>area1:
                                                    face = face0
                                                    top = top0
                                                    bottom = bottom0
                                                    left = left0
                                                    right = right0
                                                else:
                                                    face = face1
                                                    top = top1
                                                    bottom = bottom1
                                                    left = left1
                                                    right = right1
                                            else:
                                                faces = [faces[0]]
                                                face = faces[0]
                                                top, bottom, left, right = face.top(), face.bottom(), face.left(), face.right()

                                            top, bottom, left, right = face.top(), face.bottom(), face.left(), face.right()
                                            face_img=image[face.top():face.bottom(), face.left():face.right()]
                                            cv2.imwrite(subdir+'/face_'+filename[:-4]+'_'+str(gaze)+'_'+str(copy)+'.png',face_img)
                                            copy+=1


