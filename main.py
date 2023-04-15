from flask import Flask, jsonify, request, app
import base64
import cv2
import numpy as np
class SD():
    def __init__(self):
        pass
    def forward(self):
        pass

sd_process = SD()
app = Flask(__name__)
@app.route(('/sd'),methods=['POST'])
def main():
    #接受上传数据
    formdict = request.form.to_dict()
    img_post = formdict.get('image',None)
    if not img_post:
        result = {"result": ''}
        return jsonify(result)
    image = base64.b64decode(img_post)
    image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR).astype(np.uint8)
    #推理代码  返回image
    image = np.ones((256,256))
    #编码为base64stringd
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
    _, result = cv2.imencode('.jpg', image, encode_param)
    result = base64.b64encode(result)
    result = str(result, encoding='utf-8')
    response = {'result':result}
    return jsonify(response)
    
if __name__=="__main__":
    app.run(host='0.0.0.0', post=6001,debug=True)    