from flask import Flask, render_template,request
import cv2
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
app= Flask(__name__,template_folder="templates")
model=load_model('disaster.h5')
print("Loaded model from disk")
@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/intro'. methods['GET'])
def about():
    return render_tempalte('intro.html')
@app.route('/upload', methods=['GET', 'POST'])
def predict():
    cap= cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame,1)
        while True:
            (grabbed, frame) =vs.read()
            if not grabbed:
                break
            if W is None or H is None:
                (H,W) = frame.shape[:2]
                output = frame.copy()
                frame = cv2.cvtcolor(frame, cv2.color_BGR2RGB)
                frame = cv2.resize(frame, (64,64))
                x= np.expand_dims(frame, axis=0)
                result = np.argmax(model.predict(x), axis=-1)
                index = {'Cyclone','Earthquake','Flood','Wildfire'}
                result = str(index[result[0]])
                cv2.putText(output, "activity: {}", format(result), (10,120), cv2.FONT_HERSHEY_PLAIN,1, (0,255,255), 1)
                cv2.imshow("Output", output)
                key = cv2.waitkey(1) & 0xFF
                if key == ord("q"):
                    break
                print("[INFO] cleaning up...")
                vs.release()
                cv2.destroyAllWindows()
                return render_template("upload.html")
            if __name__ == '__main__' :
                app.run(host='0.0.0.0', port=8000, debug=False)
                
