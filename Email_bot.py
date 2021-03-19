import smtplib
import speech_recognition as sr
import pyttsx3 as pt
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("<sender_email_address>", "<password>")
    email = EmailMessage()
    email["From"] = "<sender_email_address>"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)



email_list = {
    "abc" : "abc123@xyz.com",
    "xyz" : "xyz456@abc.com",
    "dude" : "this_is_fab@coolprograms.com"
}

def get_email_info():
    speak("Who is the email addressed to?")
    name = get_info()
    receiver = email_list[name]
    speak("What is the highlight of your communication?")
    subject = get_info()
    speak("Let's get your detailed message..")
    message = get_info()
    send_email(receiver, subject, message)
    speak("Hey lazy boy..the mail is sent")
    speak("Do you want to send more?")
    send_more = get_info()
    if "yes" in send_more:
        get_email_info()
    else:
        speak("Thanks. You were getting on my nerves already")

get_email_info()



