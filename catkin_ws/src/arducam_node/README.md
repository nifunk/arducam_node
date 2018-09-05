# Installing

First You have to implement the normal steps which are also required for the normal version of ArduCAm

Then you can build the packacke via "catkin_make"

When using a different camera than MT9J001 change the config file in the launch folder!!!

# Launching
There are some issues due to the sudo command which is necesarry to read out the usb ports, therefore before you will be able to launch the following commands are necessary:

sudo -s

source /opt/ros/kinetic/setup.bash 

source devel/setup.bash 

To exit this root mode you can simply use "su "YOUR NORMAL USERNAME""

Other variant: make sure to have passwordless sudo and then you can simply source the "root_setup.sh" file,...

Then in the root mode simply type: roslaunch arducam_node arducam_node.launch 

ATTENTION: ONLY USE THIS SUDO MODE FOR LAUNCHING THE STUFF BUT NEVER FOR BUILDING ETC.

# Description
This is a further development of the ArduCAM USB Camera Shield which should yield to a ROS integrated version. Due to time issues, this is done here locally in our aroma repository. 

# Writing and Reading REGISTERS:

In addition I implemented a first way on how the value of some registers can be read out or actually written to:

WRITING (can be achieved by typing this command in another terminal):

rostopic pub /change_reg std_msgs/String "RegisterAdressToBeChanged ValueThatYouWant"

e.g.: rostopic pub /change_reg std_msgs/String "0x3012 0x00FF"

READING (can be achieved via this command:)

rostopic pub /read_reg std_msgs/String "'RegisterToBeReadOut'"

e.g.: rostopic pub /read_reg std_msgs/String "'0x3012'"

# Overview
ArduCAM USB Camera Shield is a general purpose USB camera controller board that can accommodate wide range of CMOS camera module from 0.3MP ~ 14MP.
By using provided SDK library and demo source code, user can design their own applications.
More info can be found from [arducam website](http://www.arducam.com/arducam-usb-camera-shield-released/)

## Now Supported Cameras
-	OV7670		0.3MP
-	OV7675		0.3MP
-	OV7725		0.3MP
-	MT9V034		0.36MP (global shutter)
-	MT9M112		1.3MP	
-	MT9M001		1.3MP (Monochrome/Color)	
-	AR0134		1.2MP (global shutter)
-	OV2640		2MP	
-	OV5642		5MP	
-	OV5640		5MP 
-	MT9P001   5MP
-	MT9N001		9MP
-	MT9J001		10MP (Monochrome)
-	MT9J003   10MP (Color)
-	MT9F002		14MP

## Support OS 
- Windows
- Linux Ubuntu
- Raspbian

## Limitations
The new USB2.0 camera shield now has onboard frame buffer, it won't have the limitation like before.