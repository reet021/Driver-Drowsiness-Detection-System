# Driver Drowsiness Detection System 

## Overview

Driver Drowsiness Detection System is a real-time computer vision application that monitors a driver's eye movements through a webcam and detects signs of drowsiness. The system uses facial landmark detection and Eye Aspect Ratio (EAR) analysis to distinguish normal blinking from prolonged eye closure and triggers an alert when drowsiness is detected.

---

## Features

- Real-time webcam monitoring
- Face and eye landmark detection using MediaPipe
- Eye Aspect Ratio (EAR) calculation
- Differentiates normal blinking from drowsiness
- Audio alarm alert for prolonged eye closure
- Real-time visual warning display
- Lightweight and easy to run

---

## Technologies Used

### Programming Language
- Python

### Libraries
- OpenCV
- MediaPipe
- NumPy
- SciPy
- Pygame

---

## Project Workflow

1. Capture video feed from webcam
2. Detect facial landmarks using MediaPipe Face Mesh
3. Extract eye landmark coordinates
4. Calculate Eye Aspect Ratio (EAR)
5. Monitor eye closure duration
6. Trigger visual and audio alerts if eyes remain closed beyond the threshold
7. Stop alert when eyes reopen

---

## How It Works

The system continuously tracks eye landmarks and computes the Eye Aspect Ratio (EAR).

- Normal blinking lasts only a fraction of a second and is ignored.
- If the EAR remains below a predefined threshold for more than 2 seconds, the system identifies the user as drowsy.
- An alarm sound and warning message are generated until the eyes reopen.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Driver-Drowsiness-Detection-System.git
cd Driver-Drowsiness-Detection-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python drowsiness.py
```

---

## Project Structure

```text
Driver-Drowsiness-Detection-System/
│
├── drowsiness.py
├── alarm.wav
├── requirements.txt
├── README.md
└── screenshot.png
```

---

## Applications

- Driver safety systems
- Fatigue monitoring
- Smart vehicle assistance
- Transportation safety solutions

---

## Future Enhancements

- Head pose estimation
- Yawn detection
- Mobile application integration
- Driver attendance monitoring
- Cloud-based alert system

---

## Author

**Avreet**

Computer Science Engineering Student

---

