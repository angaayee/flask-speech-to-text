from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    if request.method == 'POST':
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio_text = r.listen(source)
                text = r.recognize_google(audio_text)
        except Exception as e:
            text = f"Sorry, could not recognize. {str(e)}"
    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)
