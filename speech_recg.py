import speech_recognition as sr
import datetime

def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No voice input detected. Please try again.")
            return None

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return None

def execute_command(command):
    if "hello" in command:
        print("Hello! How can I help you?")
    elif "goodbye" in command:
        print("Goodbye! Have a great day!")
        return False
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"The current time is {current_time}")
    elif "name" in command:
        print("Nice to meet you! I'm a simple speech recognition tool.")
    elif "how are you" in command:
        print("I'm functioning well, thank you for asking!")
    else:
        print("I heard you, but I'm not sure how to respond to that. I can only handle simple commands.")
    return True

def main():
    print("Welcome to the Simple Speech Recognition Tool!")
    print("You can say 'hello', 'goodbye', 'time', or ask 'how are you'.")
    
    running = True
    while running:
        command = recognize_speech()
        if command is None:
            continue
        if command:
            running = execute_command(command)

    print("Thank you for using the Simple Speech Recognition Tool!")

if __name__ == "__main__":
    main()