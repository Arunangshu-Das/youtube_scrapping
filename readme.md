# YouTube Channel Analyzer

The YouTube Channel Analyzer is a web application that allows users to retrieve and analyze data from YouTube channels. It provides insights into channel statistics, video details, and more. This project is built using Flask, the YouTube Data API, and various Python libraries.

## Features

- Retrieve channel statistics, including the channel name, subscriber count, total views, and total videos.
- Fetch video details, such as the title, publication date, view count, like count, comment count, and thumbnail URL.
- Display the results in a user-friendly web interface.
- Search for data from any YouTube channel by providing the channel ID.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.x
- Flask
- Google API client library

## Getting Started

To get started with the YouTube Channel Analyzer, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Arunangshu-Das/youtube_scrapping.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain a YouTube Data API key:

   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project (if you haven't already).
   - Enable the YouTube Data API for your project.
   - Create an API key and copy it.

4. Update the API key and channel ID:

   - Open the `app.py` file in a text editor.
   - Replace `'YOUR_API_KEY'` with your API key obtained in step 3.
   - Replace `'YOUR_CHANNEL_ID'` with the desired YouTube channel ID.

5. Start the Flask development server:

   ```bash
   python app.py
   ```

6. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. Enter the YouTube channel ID in the input field on the home page and click the "Submit" button.

2. The application will retrieve the channel statistics and video details for the specified channel.

3. The results will be displayed on the results page, showing the video title, publication date, view count, like count, comment count, and thumbnail image.

4. You can analyze multiple channels by repeating steps 1-3 with different channel IDs.

## Screenshots

![**Project video**](https://youtu.be/hhwddJ9RNCw)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
