# Face Tracking Camera Controller

## Description
This projects aim was to create a smart camera system that can detect and track a human face. It uses OpenCV for face detection and RPi.GPIO to control a servo motor using PWM. The system keeps the user's face in the frame by adjusting the camera's position with the servo motor.

## Features
- **Face Detection:** Utilizes the Haar Cascade Frontalface Default model available in OpenCV for real-time face detection.
- **Servo Motor Control:** Uses the RPi.GPIO library to control a servo motor for camera movement.

## Hardware Requirements
- Raspberry Pi 4 (or a compatible model)
- USB Camera or Raspberry Pi Camera Module
- Servo Motor
- Appropriate cables and power supply

## Software Requirements

Requirements.txt file is supplied for easy installation of required packages listed below: 


- Python 3.x
- OpenCV Python Library (`opencv-python`)
- RPi.GPIO Python Library
- Numpy

## Installation

To install and run this project, follow these steps:

1. **Setting up the Raspberry Pi:**
   - Ensure Raspberry Pi is set up with the latest OS and packages.
   - Connect your camera and servo motor to the Raspberry Pi.

2. **Cloning the Repository:**
   - Clone this repository to your Raspberry Pi using: `git clone https://github.com/blakehourigan/Facial-Recognition-and-Tracking-using-OpenCV-Python.git`
   - Navigate to the cloned directory: `cd Facial-Recognition-and-Tracking-using-OpenCV-Python`

3. **Installing Required Libraries:**
   - Open a terminal on your Raspberry Pi.
   - Update the package list: `sudo apt-get update`
   - Install Python3 and pip (if not already installed): `sudo apt-get install python3 python3-pip`
   - Install required dependencies using Pip and supplied requirements.txt: `pip3 install -r requirements.txt`

4. **Running the Script:**
   - Run the main script: `python3 main.py`
   - The script should display the camera feed and begin tracking faces and reporting information about amount of faces tracked.

## Usage
- On starting the script, it will open a feed of a connected camera.
- Once a face is detected in the camera's view, the program will report a face found, and the servo motor will adjust to keep the face centered in the frame.
- Press 'q' anytime to quit the application and close the camera feed.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.

## Contact
For any queries or suggestions, feel free to reach out to the project maintainer at Houriganb@pm.me.
