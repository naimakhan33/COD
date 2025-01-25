import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

# Get screen dimensions
width = GetSystemMetrics(0) 
height = GetSystemMetrics(1)
dim = (width, height)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec for XVID format
output = cv2.VideoWriter("test.mp4", fourcc, 30.0, dim)

# Set duration (10 seconds)
duration = 10
end_time = time.time() + duration

while True:
    # Take a screenshot
    image = pyautogui.screenshot()
    frame = np.array(image)  # Convert to NumPy array
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert colors to BGR

# Write the frame to the output file
    output.write(frame)
    current_time = time.time()

    if current_time > end_time:
        break

# Release the VideoWriter
output.release()
print("---END---")




