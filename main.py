"""
BBOYT core script, handles microphone, speaker, and model interactions, and handles control flow between the aformentioned modules

Written for Python 3.11.2
Author: Misha Burnayev
"""
import os
# Suppress PyGame version and hello messages
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import microphone, speaker, interpreter

def main():
    print("--- Main active ---")
    m1 = microphone.Microphone()
    s1 = speaker.Speaker()
    vosk_path = os.path.expanduser("~/Downloads/B.BOYT/vosk-model-small-en-us-0.15")
    i1 = interpreter.Interpreter(vosk_path)
    confirm_mode = False

    while(1):
        print("--- Recording audio ---")
        m1.record()
        tokens = i1.parse_speech("mic_output.wav")
        print(f"Interpreted speech: {tokens}")
        
        if "boy" in tokens:
            confirm_mode = True
            s1.play("v4_Faith.wav")
            continue

        if confirm_mode == True:
            if "beer" in tokens:
                confirm_mode = False
                print("beer mode")
                # TODO add GPIO output to send activation signal to motor
                # Sleep for the amount of time necessary to dispense beverage
                # time.sleep(10)

            elif "monkey" in tokens:
                print("monkey mode")
                confirm_mode = False
                # TODO play "brass monkey" by the Beastie Boys, maybe not the whole thing though

            elif "music" in tokens:
                confirm_mode = False
                # TODO play 
            
        elif "quit" in tokens:
            break

    print("--- Cleanup ---")
    os.remove("mic_output.wav")
    m1.teardown()
    s1.teardown()
    i1.teardown()
    
    print("--- Program Shutdown ---")

if __name__ == "__main__":
    main()
