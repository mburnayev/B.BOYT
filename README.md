# B.BOYT
[Beer/Beverage Boy/Bot]
Imagine a boy... or even better, a bot... that serves you beer... or even better, a beverage... \
We bring you a state-of-the-art, portable beverage dispensing robot that comes with an interactive ashtray, perfect for a shady picnic or while lounging around on a relaxing beachfront — the applications are endless.

## Project Overview
This portion of the system is comprised of the following components:
- Raspberry Pi 3B
- USB Microphone
- USB Speaker
- FSR element
- Motor

The B.BOYT system starts off by passively listening to its environment, awaiting a user to address it. If the B.BOYT microphone captures audio that sounds like "boy", it will confirm that someone was addressing it by replying "yes father?" Should someone confirm their interaction with the B.BOYT by replying "beer," it will send a signal to actuate a motor inside of itself to rotate a step conveyor and dispense a drink to the user. 

Here is an abstracted visualization of the project that the above text describes:\
<img width="567" height="484" alt="Screenshot 2025-09-23 at 2 01 01 AM" src="https://github.com/user-attachments/assets/81191607-cc8a-4021-9bc4-1c147490db6b" />
<img width="1100" height="636" alt="Screenshot 2025-09-23 at 2 01 13 AM" src="https://github.com/user-attachments/assets/245168dd-d840-4332-957c-68a0933571a0" />

## Technologies Used
- Python
- PyAudio
- PyGame
- Vosk

## Note(s)
<img width="400" height="600" alt="homer-hanma" src="https://github.com/user-attachments/assets/a87a8d43-aedb-42b7-bd3e-fc1fc899250f" />

I genuinely didn't expect to run into as many issues as I did whilst improving speech recognition model performance (SRM) — turns out the solution was much more trivial than I expected.
Despite the SRM obstacles I encountered being secondary to the project itself, I think it'd be a shame to not discuss what I learned in the process of diagnosing the underlying performance issue.
My initial theory as to why the model was performing poorly was due to the program running out of available memory, which I combated by:
- connecting using basic ssh instead of VSCode's ssh (VSC has a somewhat large overhead when connecting)
- stopping and removing unused services (CUPS/CUPS-browsing)
- reducing integrated GPU memory
- booting to console instead of the desktop GUI


After some more investigating, I found that it was actually the CPU that was causing the bottleneck, which I tried to solve by:
- implementing (bad) multithreading
- passing audio bytes directly between classes instead of creating audio files and opening them
- changing scaling governors
- increasing clock speed and adding cooling (thank goodness for `vcgencmd`)
- swapping the SRM to
    - faster-whisper
    - pocketsphinx

Fortunately, I eventually found out you can add your own grammar to Vosk speech recognizers, which dramatically improved computation speeds.

## Project Timeline and Obstacles Breakdown
Task | Notes | Resolved?
--- | --- | ---
Set up new Raspberry Pi | - | ✅
Set up Python environment | - | ✅
Order new RPi power supply | undervoltage still potentially an issue? at least `dmesg` indicates the voltage gets normalized (like the other one, and that one runs without issue) | ✅
Create system design diagram(s) | design notations my beloved | ✅
Test USB speaker/audio playing | - | ✅
Test USB microphone/audio capture | - | ✅
Figure out what tools to use | might have to go back to revisit this (# of revisits: 5), but I think I have everything | ✅
Test Whisper model performance | wouldn't play nicely with PyGame since it wanted to hog the audio drivers, also memory footprint is huge | ❎
Set up Vosk | - | ✅
Test Vosk model performance | success? vosk-model-en-us-0.22-lgraph was too memory intensive, but vosk-model-small-en-us-0.15 did the job  | ✅
Add confirmation voice line | - | ✅
Reclaim RAM for stronger model usage | <li> no more sshing via souped up vscode connection <li> tweaked raspi-config to boot to cmdline instead of desktop <li> removed unnecessary utilities (CUPS) <br> Learned how RAM and swap memory work, discovered other issues in this process | 🆗
Get new microSD card | ONN betrayed me... sold me a 32GB card with 0.5GB storage on it... | ✅
---------- | **Hiatus** | ----------
Install and test faster-whisper model | still slower (more computationally expensive) than the smallest Vosk model | 🆗
Figure out how to [seemingly] continuously capture audio | ~~Might be able to get around this with a faster model~~ nope! just needed to add a grammar | ✅
Retest vosk speech recognition model | - | ✅
Add rc.local job to automatically start BBOYT core script on boot | - | ✅
Multithread program to allow users to interrupt non-dispensing operations | - | ✅
~~Acquire FSR element, set up breadboard, and test pressure sensing~~ | ~~in progress~~ | ❎
Acquire temperature sensing element, set up breadboard, test heat detection | in progress | -
Acquire motor | - | ✅
Solder motor connections | in progress | -
Test motor GPIO functionality | - | -
Create BBOYT prototype | - | -
Conduct E2E testing | - | -
Finish BBOYT v1 | - | -
Finish BBOYT v2 | - | -

## Documentation
--- Microphone --- \
https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone

--- Speaker --- \
https://www.pygame.org/docs/ref/mixer.html#pygame.mixer

--- Speech Recognition --- \
https://huggingface.co/openai/whisper-small <br>
https://huggingface.co/learn/audio-course/en/chapter5/asr_models <br>
https://alphacephei.com/vosk/models <br>
https://github.com/alphacep/vosk-api/issues/1720
https://github.com/SYSTRAN/faster-whisper <br>

--- Misc --- \
https://stackoverflow.com/questions/73268630/error-could-not-build-wheels-for-pyaudio-which-is-required-to-install-pyprojec <br>
https://stackoverflow.com/questions/51464455/how-to-disable-welcome-message-when-importing-pygame <br>
https://forums.raspberrypi.com/viewtopic.php?t=208626 <br>
https://docs.kernel.org/admin-guide/pm/cpufreq.html <br>
https://www.youtube.com/watch?v=Gl9HS7-H0mI <br>
https://docs.python.org/3/library/threading.html <br>

