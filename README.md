# aws-text-extraction-app
Streamlit app to extract text from an image using AWS rekognition [text extraction service](https://docs.aws.amazon.com/rekognition/latest/dg/text-detecting-text-procedure.html). TODO: Regions of interest can be applied to the image and the text within these regions downloaded as json.

**Note** this app requires your [AWS credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) which are passed into the app using [environment variables](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#using-environment-variables).

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
Build and run locally, picking up the required environment variables from your system environment:
```
docker build -t aws-text-extraction-app .
docker run -p 8501:8501 -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY aws-text-extraction-app:latest
```
Alternatively pull the latest release from dockerhub with:
```
docker pull robmarkcole/aws-text-extraction-app:latest
```

## Development
* Create a venv: `python3 -m venv venv` 
* Activate venv: `source venv/bin/activate`
* Install requirements: `pip3 install -r requirements.txt`
* Export required environment variables: `export AWS_ACCESS_KEY_ID=yours` and `export AWS_SECRET_ACCESS_KEY=yours`
* Run from the `app` folder: `streamlit run app.py`
