# silent_sign
# SilentSign

## AI-Based Zero-Touch Emergency Communication System

SilentSign is a prototype emergency communication system designed to help people send an SOS without speaking or physically touching a device.

The concept uses AI-based computer vision to detect non-verbal emergency signals such as **eye-blink patterns and hand gestures**. After detecting an emergency signal, the system triggers an SOS notification.

The project is based on the SilentSign mini-project concept, which proposes zero-touch emergency detection, AI-based signal recognition, emergency verification, automatic SOS alerts and offline communication.

## Problem Statement

During accidents, strokes or sudden emergencies, a person may be unable to speak, move or physically operate a phone.

Existing emergency systems may require:

* Touching a device
* Pressing an emergency button
* Unlocking a phone
* Speaking a voice command
* Internet or cellular connectivity

SilentSign aims to provide a silent and zero-touch method for requesting emergency assistance.

## Objectives

* Detect non-verbal emergency signals.
* Recognize eye-blink patterns.
* Recognize hand gestures.
* Trigger an SOS automatically.
* Reduce dependence on physical interaction.
* Provide a foundation for offline emergency communication.
* Create a system that can later be extended to smartphones, wearables and smart-home devices.

## Technologies Used

* Python
* OpenCV
* MediaPipe
* Computer Vision
* Eye Blink Detection
* Hand Gesture Detection

## Project Structure

```text
SilentSign/
│
├── silentsign.py
├── requirements.txt
└── README.md
```

## Installation

### Step 1: Install Python

Install Python 3.9 or later.

Check your Python version:

```bash
python --version
```

### Step 2: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/SilentSign.git
```

Go inside the project:

```bash
cd SilentSign
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

Run:

```bash
python silentsign.py
```

The webcam will open automatically.

The system continuously monitors:

1. Face
2. Eye-blink pattern
3. Hand gesture

Press:

```text
Q
```

to close the application.

## How It Works

```text
             Webcam
                |
                v
        +---------------+
        | Image Capture |
        +---------------+
                |
                v
       +------------------+
       | Computer Vision  |
       +------------------+
          /            \
         /              \
        v                v
 Eye Blink Detection   Hand Detection
        |                |
        v                v
 Blink Pattern       Emergency Gesture
        \                /
         \              /
          v            v
        Emergency Verification
                 |
                 v
            SOS Trigger
                 |
                 v
       Emergency Notification
```

## Eye-Blink Detection

The prototype calculates the Eye Aspect Ratio (EAR) from facial landmarks.

If the eye remains closed for a certain number of frames, a blink is detected.

The prototype uses:

```text
3 detected blinks
        ↓
Emergency signal
        ↓
SOS triggered
```

The blink threshold can be modified in `silentsign.py`.

## Hand Gesture Detection

The prototype uses MediaPipe hand landmarks to identify the position of the fingers.

The current demonstration treats an open hand with five raised fingers as an emergency gesture.

This is a basic prototype. A future version can use a trained gesture-recognition model to support personalized emergency gestures.

## SOS Function

The current implementation contains a prototype:

```python
send_sos()
```

The function prints an emergency message to the terminal.

In a complete system, it can be connected to:

* SMS
* GPS location
* Emergency contacts
* Bluetooth
* Mobile notification
* Cloud backend
* Emergency services

## Offline Communication

The SilentSign concept proposes Bluetooth-based nearby communication when internet connectivity is unavailable.

The current Python prototype does not implement Bluetooth communication. Bluetooth can be added later using an appropriate hardware/mobile communication layer.

## Future Enhancements

### 1. Personalized Gestures

Allow users to select their own emergency hand gesture.

### 2. Better Blink Recognition

Use a more robust blink-pattern model instead of a simple threshold.

### 3. GPS Integration

Automatically obtain the user's location when an SOS is triggered.

### 4. SMS Notification

Send an emergency message containing:

```text
SOS ALERT

Emergency detected by SilentSign.

Location:
Latitude: XXXXX
Longitude: XXXXX
```

### 5. Bluetooth Communication

Add nearby-device communication for situations where internet connectivity is unavailable.

### 6. Mobile Application

Convert the Python prototype into an Android application using the smartphone camera and sensors.

### 7. Sensor Verification

Combine camera detection with:

* Accelerometer
* Gyroscope
* GPS
* Other available sensors

This can help reduce false emergency alerts.

### 8. Wearable Integration

The concept can eventually be extended to:

* Smart glasses
* Smart watches
* Wearable safety devices
* Smart-home cameras

## Advantages

* Zero-touch emergency triggering
* Silent communication
* Computer-vision based detection
* Useful for people who cannot speak
* Potential offline communication
* Can be extended to wearable devices
* Can reduce dependence on physical emergency buttons

## Prototype Cost

The project concept estimates a prototype cost of approximately:

**₹2,000 – ₹4,900**

The proposed resources include existing smartphone cameras and sensors, open-source AI/ML libraries, Bluetooth communication, testing equipment and development resources.

## Limitations

This repository is a basic academic prototype.

It currently does not provide:

* Real SMS delivery
* Real emergency-service integration
* GPS transmission
* Bluetooth SOS communication
* Production-grade AI verification
* Medical-grade emergency detection
* Guaranteed false-alarm prevention

The SOS function should therefore be treated as a **demonstration**, not as a replacement for a real emergency service.

## Team

* Lavanya Shri R — CB2328
* Muthamil E — CB2340
* Rubhavashni L R — CB2347

## Project Department

Department of Computer Science and Business Systems (CSBS)

## Project Vision

SilentSign aims to create an inclusive emergency communication system where a person can request help even when speech, movement or physical interaction with a device is difficult.

The long-term concept can expand from a Python/computer-vision prototype to smartphones, smart-home cameras, smart glasses, wearable devices, healthcare systems and emergency services.

> **“When words and movement fail, technology should speak for you.”**
