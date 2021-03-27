# SCAVE-CPS
This is the Github Repo for SCAVE-CPS project

## dev , folder with class for OS, Perception , Path planning , Control
## doc , Documentation folder + github repo instructions
## examples , CARLA examples

## Test , CARLA code test
Environments, CNN models and carla source code and docs are in the share folder

### Full stack AV basic test, in Folder dev/src_Python/Basic/AV
** Mark AV dir as source route, so you have the can import carla from AV

Create environment with Python 3.6 (Install requirements.txt) , or source  your carla8x env

1- In CarlaAV folder Run sh ./CarlaUE4.sh /Game/Maps/Course4 -windowed -carla-server -benchmark -fps=30

2- Run run_pipeline.py

###  Perception test, lane detection, object detection, object segmentation

Install carla 9.8 in your system 

Create environment with Python 3.7 (Install requirements.txt) , or source  your carla9x env

1- In carla-simulator 9.8 run sh ./CarlaUE4.sh

2- Inside Test/Perception_Tests run Perception_Tests.py
* Uncomment the code that you want to test
* Test lane detections ,object detection based on SSD, Yolo and Semantic Segmentation
    * lines,size_im= lane_detectionv3(RGB_Camera_im)
    * lines,size_im=object_detection_SSD(RGB_Camera_im)
    * lines, size_im = object_detection_Yolo(RGB_Camera_im)
    * lines, size_im = object_detection_mask(RGB_Camera_im)
    * lines, size_im = lane_detectionv2(RGB_Camera_im)

## Project shared folder Files and doc link
https://knightsucfedu39751-my.sharepoint.com/:f:/g/personal/rvalienter90_knights_ucf_edu/EnBKOPTb5gFMsWf_pvImJCoBMebJWPN_2dbETdzPGeuNHQ?e=gF1dAX
