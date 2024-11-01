# YouTube Downloader

This project is a web application built as the CS50 final project that allows users to download YouTube videos and maintain a personal download history. It’s built using Flask, SQLite, and uses `yt-dlp` for video processing.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)

## Features
- **User Authentication**: Sign-up and login to keep track of download history.
- **Download Videos**: Allows users to paste a YouTube URL and download videos in various formats.
- **Download History**: Stores download history for each user using SQLite.
- **User-Friendly Interface**: Built with Bootstrap for responsive design and Font Awesome for icons.

## Technologies
- **Backend**: Flask, CS50 SQL library
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite3
- **Video Processing**: yt-dlp (a YouTube video downloader library)
- **Authentication**: Custom session management in Flask

## Installation
### Prerequisites
- Python 3.x
- `pip` (Python package installer)
- Termux (if installing and running on Android)
  
### Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```
2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Database Setup**: Run the following to set up the SQLite database:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```
5. **Start the Application**:
    ```bash
    flask run
    ```
6. Open a web browser and go to http://localhost:5000.

## Usage
1. **Register an Account**: New users can sign up to track their downloads.
2. **Log In**: Users can log in to access their download history.
Download a Video: Paste a YouTube URL, select the format, and download.
3. **View Download History**: See previously downloaded videos, format, and date of download.

## Project Structure
```
youtube-downloader/
├── app/
│   ├── static/                # Static files (CSS, JS)
│   ├── templates/             # HTML templates
│   ├── __init__.py            # Initializes Flask app
│   ├── auth.py                # User authentication routes
│   ├── database.py            # Database connection and models
│   ├── downloader.py          # Download processing with yt-dlp
│   └── views.py               # Main routes for downloading videos
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── run.py                     # Runs the Flask app
```

## Future Improvements
- **Video Conversion**: Add options to convert videos to other formats (e.g., MP3).
- **Multiple Resolutions**: Allow users to select specific video resolutions.
- **Progress Bar**: Display download progress for better user experience.
- **Enhanced Error Handling**: Improve handling for invalid URLs or download failures.


## Acknowledgments
- **CS50 Team**: For providing the foundational knowledge and support.
- **yt-dlp**: A great tool that made handling YouTube downloads easy.
- **Bootstrap and Font Awesome**: For helping create a responsive and visually appealing interface.

## License
This project is licensed under the MIT License.

---


