import microphone
import speaker

def main():
    print("Main active")
    m1 = microphone.Microphone()
    m1_stats = m1.toString()
    print(m1_stats)

    s1 = speaker.Speaker()
    s1.play("vline_Bender.mp3")

if __name__ == "__main__":
    main()