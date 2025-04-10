# Signing in

import time

colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
emojis = ['😎', '❤️', '🔥', '💻', '🧠']

for i in range(20):
    print(f"{colors[i % len(colors)]}Python is fun! {emojis[i % len(emojis)]}")
    time.sleep(0.3)

# Signing off 