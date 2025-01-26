import cv2
import time
import os
import csv
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize the CSV files for students and attendance
if not os.path.exists("students.csv"):
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "ImagePath"])

if not os.path.exists("attendance.csv"):
    with open("attendance.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Timestamp", "Status"])  # Added "Status" for "In" or "Out"

# Dictionary to track the last status ("In" or "Out") of each student
student_status = {}

# Function to check if the student is registered
def is_registered(name):
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            if row[0] == name:
                return row[1]
    return None

# Function to register a new student
def register_student(name):
    img_path = f"registered_images/{name}.jpg"
    cv2.imwrite(img_path, frame)  # Save the student's image
    
    # Save the student data in the CSV file
    with open("students.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, img_path])
    messagebox.showinfo("Registration", f"Student {name} registered successfully.")

# Function to take attendance (logs "In" or "Out")
def log_attendance(name, status):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("attendance.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, timestamp, status])
    messagebox.showinfo("Attendance", f"{status} recorded for {name}.")

# GUI setup with tkinter
root = tk.Tk()
root.title("Smart Attendance System")
root.geometry("500x300")

# Webcam setup
video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# No face timer and threshold
no_face_start_time = None
NO_FACE_THRESHOLD = 5  # Seconds

# Functions for the GUI actions
def show_frame():
    global frame, no_face_start_time
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture video")
        root.after(10, show_frame)
        return
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check for faces in the frame
    if len(faces) == 0:
        if no_face_start_time is None:
            no_face_start_time = time.time()
        elif time.time() - no_face_start_time > NO_FACE_THRESHOLD:
            messagebox.showwarning("Warning", "No faces detected for more than 5 seconds! Shutting down.")
            shutdown_camera()
            return
    else:
        no_face_start_time = None  # Reset if a face is detected

    # Draw rectangles around faces and process attendance
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image=img)
    lbl_video.imgtk = img
    lbl_video.configure(image=img)
    lbl_video.after(10, show_frame)

def register():
    name = entry_name.get()
    if not name:
        messagebox.showwarning("Registration", "Please enter a name.")
        return
    
    if is_registered(name):
        messagebox.showwarning("Registration", f"{name} is already registered.")
        return
    
    register_student(name)

def check_in_out():
    name = entry_name.get()
    if not name:
        messagebox.showwarning("Attendance", "Please enter a name.")
        return
    
    img_path = is_registered(name)
    if img_path:
        # Check student's last status and log the opposite
        if student_status.get(name) == "In":
            log_attendance(name, "Out")
            student_status[name] = "Out"
        else:
            log_attendance(name, "In")
            student_status[name] = "In"
    else:
        messagebox.showwarning("Attendance", f"{name} is not registered. Please register first.")

def shutdown_camera():
    # Release the camera and destroy all windows
    video_capture.release()
    cv2.destroyAllWindows()
    root.destroy()  # Close the Tkinter window

# GUI components
lbl_video = tk.Label(root)
lbl_video.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack()

tk.Label(frame_buttons, text="Enter Student Name:").grid(row=0, column=0)
entry_name = tk.Entry(frame_buttons, width=20)
entry_name.grid(row=0, column=1)

btn_register = tk.Button(frame_buttons, text="Register", command=register)
btn_register.grid(row=1, column=0, pady=10)
btn_check_in_out = tk.Button(frame_buttons, text="Check In/Out", command=check_in_out)
btn_check_in_out.grid(row=1, column=1, pady=10)

# Start video feed display
show_frame()

# Start the GUI loop
root.mainloop()
