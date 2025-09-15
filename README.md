# Kivy Calculator App

A simple calculator application built with Kivy framework.

## Features
- Basic arithmetic operations (+, -, *, /)
- Square root function
- Clear and delete functions
- Parentheses support
- Responsive design

## Running on Desktop
1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
2. Run the app:
   ```
   python main.py
   ```

## Building for Android
There are several ways to build an APK for Android:

### Option 1: Using GitHub Actions (Recommended for Windows users)
1. Create a GitHub repository and push this code to it
2. The GitHub Actions workflow will automatically build the APK
3. Download the APK from the Actions tab

### Option 2: Using WSL (Windows Subsystem for Linux)
1. Install WSL2 with Ubuntu
2. Install the required dependencies:
   ```
   sudo apt update
   sudo apt install -y build-essential git python3 python3-pip python3-venv
   ```
3. Install buildozer:
   ```
   pip3 install buildozer
   ```
4. Build the APK:
   ```
   buildozer android debug
   ```

### Option 3: Using Docker
1. Install Docker Desktop
2. Build the APK using the Kivy official Docker image:
   ```
   docker run --rm -v "$PWD":/home/user/hostcwd kivy/buildozer android debug
   ```

## Files
- `main.py`: Main application code
- `buildozer.spec`: Buildozer configuration for Android
- `requirements.txt`: Python dependencies

## Requirements
- Python 3.7+
- Kivy 2.0+

## License
MIT