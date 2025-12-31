from vvv import ask_gemini
from voice import listen, speak

def main():
    speak("VoxAssist is online. How can I help you?")

    while True:
        user_input = listen()

        if user_input.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break

        response = ask_gemini(user_input)
        print("🤖 VoxAssist:", response)
        speak(response)

if __name__ == "__main__":
    main()
