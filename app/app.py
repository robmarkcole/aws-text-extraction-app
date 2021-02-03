import streamlit as st
from PIL import Image
import io
import os
import numpy as np

DEFAULT_REGION = "us-east-1"
DEMO_IMAGE = "smart_meter.jpg"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", DEFAULT_REGION)

