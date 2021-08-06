# YouTubeToMP3
# This program allows you to download audio files from YouTube links
# A program by Tyler Serio
# Programming started circa August 2021
# Python > 3.9
# Tutorial from https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/

# Import packages
import pytube
from pytube import YouTube
import os
import time

try:
    os.makedirs("downloads")
    print("Directory for downloads created.")
    print("")
except FileExistsError:
    print("Directory for downloads exists.")

on = 1
while on == 1:
    # Get the URL from the user
    test_url = 1
    while test_url == 1:
        url_getting = 1

        # Check to see if the URL is valid
        while url_getting == 1:
            try:
                yt = YouTube(str(input("Enter the URL of the audio that you want to download from YouTube: \n>> ")))
                url_getting = 0
            except pytube.exceptions.RegexMatchError:
                print("That is not a valid YouTube link.")

        # Let the user know that something is happening
        print("Please wait...")
        
        # Extract only the audio
        # Check to see if the video is restricted
        try:
            video = yt.streams.filter(only_audio = True).first()
            url_getting = 0
            test_url = 0
        except pytube.exceptions.AgeRestrictedError:
            print("This video is age restricted and cannot be downloaded without logging in.")

    # Check for destination to save file
    print("Enter the directory where you would like to save the file (leave blank for current directory)")
    destination = str(input(">> ")) or "downloads"

    # Let the user know that something is happening
    print("Please wait...")

    # Download the file
    try:
        out_file = video.download(output_path=destination)
        time.sleep(4)
    except OSError:
        print("Something is wrong with that directory path. Defaulting to current directory.")
        destination = "."
        out_file = video.download(output_path=destination)
        time.sleep(4)

    # Save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    try:
        os.rename(out_file, new_file)
    except FileExistsError:
        os.replace(out_file, new_file)

    # Result
    os.system("cls")
    print(yt.title + " has been successfully downloaded.")
    print("")
