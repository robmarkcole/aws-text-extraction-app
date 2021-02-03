import streamlit as st
from PIL import Image
import io
import os
import numpy as np

import boto3
import json

DEFAULT_REGION = "us-east-1"
DEMO_IMAGE = "smart_meter.jpg"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", DEFAULT_REGION)

client = boto3.client("rekognition", region_name=AWS_DEFAULT_REGION)


def pil_image_to_byte_array(image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, "PNG")
    return imgByteArr.getvalue()


@st.cache
def process_image(image_bytes):
    response = client.detect_labels(Image={"Bytes": image_bytes})
    return response


st.title("Extract text with AWS rekogniton text extraction")
img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])


if img_file_buffer is not None:
    image_bytes = pil_image_to_byte_array(Image.open(img_file_buffer))
    image_array = np.array(Image.open(img_file_buffer))

else:
    image_bytes = open(DEMO_IMAGE, "rb")
    image_array = np.array(Image.open(DEMO_IMAGE))

response = process_image(image_bytes)
extracted_text = [t["DetectedText"] for t in response["TextDetections"]]

st.image(
    image_array, use_column_width=True,
)

st.header("Extracted text")
st.write(extracted_text)
