from flask import Flask
from flask import request
from joblib import load
from flask import render_template,flash, request
# import numpy as np
# from numpy import asarray
# from PIL import Image

app = Flask(__name__)
model_path = "svm_gamma=0.0002_C=5.joblib"
model = load(model_path)


@app.route("/mydocker")
def hello_world():
    return '''<!-- hello --> <b> Hello, Pallav!</b>
    <br><b> This App running on docker</b></br>'''


@app.route("/predict", methods=['POST'])
def predict_digit():
    image1 = request.json['image1']
    image2 = request.json['image2']
    print("done loading both image")
    predicted1 = model.predict([image1])
    predicted2 = model.predict([image2])

    if predicted1==predicted1:
        issame="Yes"
    else:
        issame="No"
    #return {"Image 1 was: { }".format ((int(predicted1[0]))) }
    my_result = "Image 1 digit: " + (str(predicted1[0]) + " and Image 2 digit: " +str (predicted2[0]) + " Predict image digit are same: " + str (issame))
    return {"Result":str(my_result)}


@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

# IMAGE_FOLDER='static/'
# app.config['UPLOAD_FOLDER']=IMAGE_FOLDER
@app.route('/predictweb',methods=['GET','POST'])
def predict_digit_web():
    # f1=Image.open(r"/Users/pallavprince/Documents/ppmtech/mlops-22/api/static/5.jpg")
    # full_filename = os.path.join("/Users/pallavprince/Documents/ppmtech/mlops-22/api/static/5.jpg",f1.filename)
    # f2=Image.open(r"/Users/pallavprince/Documents/ppmtech/mlops-22/api/static/5.png")
    # # img1=asarray(f1)
    # # img2=asarray(f2)
    # #if request.method=='POST':
    # f1.save(os.path.join(app.config['UPLOAD_FOLDER'], f1.filename))
    # f2.save(os.path.join(app.config['UPLOAD_FOLDER'], f2.filename))
    
    # full_filename1 = os.path.join(app.config['UPLOAD_FOLDER'],f1.filename)
    # full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'],f2.filename)
    # img1=asarray(full_filename1)
    # img1=asarray(full_filename2)
    # img1.resize((28, 28))
    # img2.resize((28, 28))
    # gray_img1 = img1.convert("L")
    # gray_img2= img2.convert("L")
    # gray_img1=gray_img1/255
    # ray_img2=gray_img2/255
    # for y in range(28):
    #     for z in range(28):
    #         if gray_img1[y][z][0]==1:
    #             gray_img1[y][z][0]=0
    #             gray_img2[y][z][0]=0
    #         else:
    #             gray_img1[y][z][0]= 1-gray_img1[y][z][0]
    #             gray_img2[y][z][0]= 1-gray_img2[y][z][0]

    # gray_img1=np.expand_dims(gray_img1,axis=0)
    # gray_img2=np.expand_dims(gray_img2,axis=0)
    # # predicted1 = model.predict([gray_img1])
    # # predicted2 = model.predict([gray_img2])
    predicted1="5"
    predicted2="5"
    my_result= "YES"

    return render_template('predict.html', prediction1=predicted1, prediction2=predicted2, predictResult=my_result)
   

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)