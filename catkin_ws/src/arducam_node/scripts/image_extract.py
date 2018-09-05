#!/usr/bin/env python

import rosbag, sys, yaml, os, cv2
import numpy as np
import argparse


class ImageConversions():
    # We only instantiate the bridge once
    bridge = None
    
def get_cv_bridge():
    if ImageConversions.bridge is None:
        from cv_bridge import CvBridge  # @UnresolvedImport
        ImageConversions.bridge = CvBridge()
    return ImageConversions.bridge


def rgb_from_imgmsg(msg):
    bridge = get_cv_bridge()
    return bridge.imgmsg_to_cv2(msg, "rgb8")

def bgr_from_imgmsg(msg):
    bridge = get_cv_bridge()
    return bridge.imgmsg_to_cv2(msg, "bgr8")

    
def d8n_image_msg_from_cv_image(cv_image, image_format, same_timestamp_as = None):
    """ 
        Makes an Image message from a CV image. 
    
        if same_timestamp_as is not None, we copy the timestamp
        from that image.
        
        image_format: 'bgr8' or 'mono' or similar
    """
    bridge = get_cv_bridge()
    image_msg_out = bridge.cv2_to_imgmsg(cv_image, image_format)
    if same_timestamp_as is not None:
        image_msg_out.header.stamp = same_timestamp_as.header.stamp
    return image_msg_out
    

def pil_from_CompressedImage(msg):
    from PIL import ImageFile  # @UnresolvedImport
    parser = ImageFile.Parser()
    parser.feed(msg.data)
    res = parser.close()
    return res

def rgb_from_pil(im):
    import numpy as np
    return np.asarray(im).astype(np.uint8)


def rgb_from_ros(msg):
    if 'CompressedImage' in msg.__class__.__name__: 
        return rgb_from_pil(pil_from_CompressedImage(msg))
    else:
        return rgb_from_imgmsg(msg)

numpy_from_ros_compressed = rgb_from_ros

parser = argparse.ArgumentParser()
parser.add_argument("input_bagpath", help="specify link to input bagfile", type=str)
parser.add_argument("topic_tolisten", help="specify the camera topic e.g. /tesla/image_transformer_node/corrected_image", type=str)
parser.add_argument("output_directory", help="specify output directory", type=str)
args=parser.parse_args()
bag = rosbag.Bag(args.input_bagpath)
topic_interest= args.topic_tolisten

dir = args.output_directory
if os.path.exists(dir):
	print "Directory already exists"
	sys.exit(3) 

os.makedirs(dir)
i=0
for topic, msg, t in bag.read_messages(topics=topic_interest):
		im1=rgb_from_ros(msg)
		im1=im1[...,::-1] #::-1 reverses a string!!!
		cv2.imwrite(dir+ '/' + str(i) + '.jpg',im1)
		i+=1
bag.close()