from PIL import Image
import cv2
import os
from yolo_files import detect2
from gan_files import test, gan_utils
#from SOURCE.vgg_finetuned_model import vgg_verify
import shutil
import glob

MEDIA_ROOT = '..\\testing_images\docs_to_test'
SIGNATURE_ROOT = 'media/UserSignaturesSquare/'
YOLO_RESULT = '\yolo_files\\results'
YOLO_CROP = '\yolo_files\cropped'
YOLO_OP = 'crops/DLSignature/'
GAN_IPS = 'results/gan/gan_signdata_kaggle/gan_ips/testB'
GAN_OP = 'results/gan/gan_signdata_kaggle/test_latest/images/'
GAN_OP_RESIZED = 'results/gan/gan_signdata_kaggle/test_latest/images/'




def signature_detection():
    ''' Performs signature detection and returns the results folder. '''

    # call YOLOv8 detection fn on all images in the document folder.

    #detect2.detect(MEDIA_ROOT + '\\test1.jpg')

    # get the path where last detected results are stored.
    #latest_detection = max(glob.glob(os.path.join(YOLO_RESULT, '*/')), key=os.path.getmtime)
    # resize and add top and bottom padding to detected sigantures. 
    # gan model expects ips in that particular format.
    #gan_utils.resize_images(os.path.join(latest_detection, YOLO_CROP))
    gan_utils.resize_images('D:\work\kaggle\signature-detection-verification\streamlit_app\yolo_files\cropped\\0') #  !!! problems with relative path so hardcoded absolute

    # selects and display the detections of the document which the user selected.
    return YOLO_CROP # return the yolo op folder


def copy_and_overwrite(from_path, to_path):
    '''
    Copy files from results/yolo_ops/ to results/gan/gan_signdata_kaggle/gan_ips
    CycleGAN model requires ip files to be present in results/gan/gan_signdata_kaggle/gan_ips
    '''
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


def signature_cleaning():
    ''' Performs signature cleaning and displays the cleaned signatures '''
    # copy files from results/yolo_ops/ to results/gan/gan_signdata_kaggle/gan_ips
    copy_and_overwrite(YOLO_CROP, GAN_IPS)
    test.clean() # performs cleaning

    #cleaned images are selected and displayed
    #cleaned_image = select_cleaned_image(selection)


def main():
    image_doc_path = 'D:\work\kaggle\signature-detection-verification\streamlit_app\yolo_files\\test1.jpg'
    signature_detection()
    return

main()

