# Face-detection-
Smart attendance system using face detection 

**Overview**
The Smart Attendance System uses face detection technology to automate the attendance process. This project eliminates the need for traditional roll calls or manual attendance records, ensuring an efficient and secure way to track attendance. By leveraging advanced face detection, it registers and recognizes individuals, storing attendance records with timestamps.

**Features**
>Face Registration: Capture and register faces with user details.
>Face Detection: Detect faces in real-time and mark attendance.
>Attendance Log: Save attendance records with date and time in a CSV file.
>User Interface: Easy-to-use interface for registration and attendance marking.
>Secure and Efficient: Reduces manual errors and prevents proxy attendance.

**smart-attendance-system/**
├── README.md
├── main.py                 # Your uploaded Python script
├── requirements.txt        # Python dependencies
├── students.csv            # CSV file for student details
├── attendance.csv          # CSV file for attendance logs
├── registered_images/      # Directory for storing registered face images
└── LICENSE                 # License file (MIT or as preferred)

**requirements.txt: Generate a list of Python dependencies required for your project:**
plaintext
Copy
Edit
opencv-python
numpy
pandas
pillow
tk
students.csv and attendance.csv: Add empty sample files for reference, ensuring the headers are pre-written.
Images Folder: Add an empty registered_images/ folder for storing face images.

**How It Works**
**Registration:**
Users register their details (e.g., name) along with their face image.
The system stores the face encodings and user data in a CSV file.

**Attendance:**

The system uses the camera to detect and recognize faces in real-time.
Matches the detected face with registered faces.
Marks attendance with a timestamp in the attendance.csv file.

**No Face Alert:**
If no faces are detected for more than a predefined threshold (e.g., 5 seconds), the system alerts the user or shuts down the camera.

**Logs:**
Attendance logs are saved in the attendance.csv file and can be exported for reporting.

**Future Enhancements**
Face Mask Detection: Enhance the system to recognize faces with masks.
Multi-Camera Support: Extend to support multiple cameras for large-scale use.
Cloud Integration: Store data securely in the cloud for centralized access.
Mobile App: Develop a companion mobile application for attendance marking.
Biometric Authentication: Add multi-factor authentication for higher security.
Analytics Dashboard: Add a feature to visualize attendance trends and generate reports.


