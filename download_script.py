import sys
import requests

# Check if the user provided a URL as an argument
if len(sys.argv) < 2:
    print("Usage: python3 download_script.py <url>")
    sys.exit(1)

# Get the URL from the command line argument
url = sys.argv[1]

# Define the name of the file to save the download
file_name = 'downloaded_audio.mp3'

def download_file(url, file_name):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url, stream=True)
        
        # If the request is successful, download and save the file
        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"{file_name} has been downloaded successfully.")
        else:
            print(f"Download failed. HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to download the file
download_file(url, file_name)