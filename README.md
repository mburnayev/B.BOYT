# B.BOYT
[Beer/Beverage Boy/Bot]
Imagine a boy... or even better, a bot... that serves you beer... or even better, a beverage... \
We bring you a state-of-the-art, portable beverage dispensing robot somewhat shaped like a monolith that comes with an interactive ashtray, perfect for a shady picnic or while lounging around on a relaxing beachfront — the applications are endless.

## Project Overview
This portion of the system is comprised of the following components:
- Raspberry Pi 3B+
- USB Microphone
- USB Speaker
- Piezo element
- Motor

The B.BOYT system starts off by passively listening to its environment, awaiting a user to address it. If the B.BOYT microphone captures audio that sounds like "boy", it will confirm that someone was addressing it by replying "yes father?" Should someone confirm their interaction with the B.BOYT by replying "beer," it will send a signal to actuate a motor inside of itself to rotate a step conveyer and dispense a drink to the user. 

Here is an abstracted visualization of the project that the above text describes:\
<img width="567" height="484" alt="Screenshot 2025-09-23 at 2 01 01 AM" src="https://github.com/user-attachments/assets/81191607-cc8a-4021-9bc4-1c147490db6b" />
<img width="1100" height="636" alt="Screenshot 2025-09-23 at 2 01 13 AM" src="https://github.com/user-attachments/assets/245168dd-d840-4332-957c-68a0933571a0" />

## Technologies Used
- Python
- PyAudio
- PyGame
- PyTorch
- OpenAI Whisper

## Note(s)
<img width="400" height="600" alt="homer-hanma" src="https://github.com/user-attachments/assets/a87a8d43-aedb-42b7-bd3e-fc1fc899250f" />

## Project Timeline and Obstacles Breakdown
Task | Notes | Resolved?
--- | --- | ---
Set up new Raspberry Pi | - | ✅
Set up Python environment | - | ✅
Order new RPi power supply | undervoltage still potentially an issue? at least `dmesg` indicates the voltage gets normalized (like the other one, and that one runs without issue) | ✅
Create system design diagram(s) | design notations my beloved | ✅
Test USB speaker/audio playing | - | ✅
Test USB microphone/audio capture | - | ✅
Figure out what tools to use | might have to go back to revisit this, but I think I have everything | ✅
Test Whisper model performance | in progress | -
Add operation blocking to prevent input during interpretation or output | - | -
Add confirmation voice line | - | -
Figure out how to continuously capture audio | - | -
Test Piezo element/pressure sensing | - | -
Conduct E2E testing | - | -
Create BBOYT prototype | - | -
Probably go back to the drawing board and make revisions | - | -
Create BBOYT v1 | - | -


## Documentation
--- Microphone ---
https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone

--- Speaker ---
https://www.pygame.org/docs/ref/mixer.html#pygame.mixer

--- Whisper ---
https://huggingface.co/openai/whisper-large-v3

--- Misc ---
https://stackoverflow.com/questions/73268630/error-could-not-build-wheels-for-pyaudio-which-is-required-to-install-pyprojec
https://stackoverflow.com/questions/8110310/simple-way-to-query-connected-usb-devices-info-in-python
