# USAGE
# python simple_request.py

# import the necessary packages
import requests

# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://127.0.0.1:3000/predict"
IMAGE_PATH = "cat.jpeg"

# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# submit the request
request_predict = requests.post(KERAS_REST_API_URL, files=payload).json()
request_get=requests.get('/predictedModel',prediction)

# ensure the request was sucessful
if rrequest_predict["success"]:
	# loop over the predictions and display them
	for (i, result) in enumerate(r["predictions"]):
		print("{}. {}: {:.4f}".format(i + 1, result["label"],
			result["probability"]))

# otherwise, the request failed
else:
	print("API Request Failed")
