# aws-text-extraction-app
Streamlit app to extract text from an image using AWS rekognition text extraction service. Regions of interest can be applied to the image and the text within these regions downloaded as json. **Note** this app requires your AWS credentials which are passed into the app using [environment variables](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#using-environment-variables).

All environment variables that can be passed are listed below:
```
- AWS_ACCESS_KEY_ID : (required) your key ID, 
- AWS_SECRET_ACCESS_KEY : (required) your key secret
- AWS_DEFAULT_REGION : (optional) your preferred AWS region, default `us-east-1`
```

<p align="center">
<img src="https://github.com/robmarkcole/aws-text-extraction-app/blob/main/docs/usage.png" width="800">
</p>

## Build Dockerfile and run
Build and run locally:
```
docker build -t aws-text-extraction-app .
docker run -e AWS_ACCESS_KEY_ID=yous -e AWS_SECRET_ACCESS_KEY=yours aws-text-extraction-app:latest
```

## Development
* Create a venv: `python3 -m venv venv` 
* Activate venv: `source venv/bin/activate`
* Install requirements: `pip3 install -r requirements.txt`
* Export required environment variables: `export AWS_ACCESS_KEY_ID=yours` and `export AWS_SECRET_ACCESS_KEY=yours`
* Run from the `app` folder: `streamlit run app.py`
