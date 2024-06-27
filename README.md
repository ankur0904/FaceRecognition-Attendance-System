

https://github.com/ankur0904/FaceRecognition-Attendance-System/assets/98346896/21b6edeb-7577-43d0-9c04-c35cc46c8016

# FaceRecognition Attendance System

This project is an automatic attendance system that uses facial recognition technology to mark attendance in real-time. The system captures images from a webcam, detects and recognizes faces, and logs attendance details in a CSV file.

## Features

- Real-time face detection and recognition
- Automatic attendance marking
- High accuracy of 99.38%
- Easy to use and deploy

## Technologies Used

- **Programming Language**: Python
- **Computer Vision Library**: OpenCV
- **Facial Recognition Library**: face_recognition
- **Data Handling**: CSV
- **Date and Time Management**: datetime module
- **Image Processing and Analysis**: NumPy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/facerecognition-attendance-system.git
    cd facerecognition-attendance-system
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have a folder named `images` in the project directory. Add images of individuals (one image per person) with filenames as their names (e.g., `john.jpg`).

## Usage

1. Run the script:
    ```bash
    python attendance.py
    ```

2. The system will start capturing video from your webcam. It will detect and recognize faces, then log the attendance in `attendance.csv`.

## How It Works

- The system reads images from the `images` directory and encodes the faces.
- It captures video frames from the webcam and detects faces in each frame.
- It compares the detected faces with the encoded faces to find matches.
- If a match is found, it marks the attendance with the person's name and the current date and time in `attendance.csv`.

## Acknowledgments

- This project uses the [face_recognition](https://github.com/ageitgey/face_recognition) library by Adam Geitgey.
- The OpenCV library is used for image processing tasks.

## License

This project is licensed under the MIT License.
