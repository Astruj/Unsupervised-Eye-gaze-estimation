1. Each folder contains one subject's data. 
   Each subject contributes to 16 videos, corresponding to 4 rounds of 4 different body postures (sitting, standing, slouching and lying).

2. In each folder, each file is named in the format of "subjectID_trialID_postureID.mp4'. The four body postures are ordered as: sitting - 1, standing - 2, slouching -3 and lying - 4.
   For example, 1_1_1.mp4 represents the video file of subject 1 holding the tablet in sitting posture in the 1st trial.

3. The time stamps when the subjects in the videos started to gaze at the predefined dots on the tablet screen are stored in file 'startTime.mat'.
   The file can be opened in matlab. The array stored in the file has a size of 51*4*4, and it is also stored in the format of (subjectId, trialId, postureId). 

4. The order of the 35 predefined random gaze locations on the tablet screen is stored in file 'gazePts.mat'. 
   In the file, data element 'Y_h' and 'Y_v' stores the numerical number of the 35 gaze locations while data element 'Y_h_reg' and 'Y_v_reg' stores the physical locations (in cm) on the screen. 
   The locations are represented with the top left corner of the screen as origin, and the horizontal direction aligns with the width of the tablet when the tablet is holding on landscape mode and the front camera is on the top of the screen.


