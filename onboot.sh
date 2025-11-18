#!/bin/bash

# wait for USD + audio drivers to initialize
sleep 15

tmux kill-session -t bboyt 2>/dev/null
tmux new-session -d -s bboyt -c /home/pi/Downloads/B.BOYT

tmux send-keys -t bboyt "source ppvenv/bin/activate" C-m
tmux send-keys -t bboyt "python3 main.py" C-m
