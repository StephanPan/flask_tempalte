import requests
import json
import base64
import cv2
import numpy as np


post_url = "0.0.0.0:6001/sd"
image = np.ones((256,256,3))
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
_, image = cv2.imencode('.jpg', image, encode_param)
image = base64.b64encode(image)
files = {"image": image}
response = requests.post(post_url, data=files)
result_dict = json.loads(response.text)
result_image = result_dict['result']
result_image = base64.b64decode(result_image)
result_image = cv2.imdecode(np.frombuffer(result_image, np.uint8), 1)
cv2.imwrite('result_image.jpg', result_image)