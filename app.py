from flask import Flask, render_template, request
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    if request.method == 'POST':
        if "audio_data" in request.files:
            audio_file = request.files["audio_data"]
            os.makedirs("uploads", exist_ok=True)
            file_path = os.path.join("uploads", audio_file.filename)
            audio_file.save(file_path)

            # Only WAV files supported
            r = sr.Recognizer()
            try:
                with sr.AudioFile(file_path) as source:
                    audio = r.record(source)
                    text = r.recognize_google(audio)
            except sr.UnknownValueError:
                text = "Sorry, could not understand the audio."
            except sr.RequestError:
                text = "Sorry, speech service is not available."
            except:
                text = "An error occurred."

    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
