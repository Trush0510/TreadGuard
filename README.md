# TreadGuard
TreadGuard is an innovative pothole detection system designed to improve road safety and maintenance. It combines real-time camera-based detection using YOLOv11 and accelerometer/gyroscope data analysis to provide accurate identification and reporting of potholes. The solution can be embedded into vehicles for continuous monitoring and reporting of road conditions.

Features

Real-Time Detection:

Uses a camera-based system with YOLOv11 to identify potholes.

Employs accelerometer and gyroscope data for enhanced detection accuracy.

Data Reporting:

Provides detailed reports of detected potholes, including location and severity.

Displays pothole data on a web-based dashboard for better accessibility and analysis.

Vehicle Integration:

Can be embedded into vehicles for automated road condition monitoring.

User-Friendly App:

Android app to view real-time detection results and send data to the server.

Integrated with Roboflow for a seamless front-end experience.

Technology Stack

Frontend:

Roboflow: Used for camera-based pothole detection.

Web Interface: Displays pothole reports and visual data.

Backend:

YOLOv11: Core object detection model for identifying potholes.

Custom Neural Network: Processes accelerometer and gyroscope data.

Tools:

Android Studio: For app development.

Python: Backend development and data processing.

TensorFlow Lite: Optimized model deployment on mobile devices.

