from django.shortcuts import render
from django.http import HttpResponse
import requests
import isodate

YOUTUBE_API_KEY = 'ENTER YOUR_API_KEY'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3'

def calculate_duration(request):
    if request.method == 'POST':
        playlist_url = request.POST.get('playlist_id', '').strip()
        
        # Check if the URL is valid
        if not playlist_url or "list=" not in playlist_url:
            return render(request, 'myapp/index.html', {'error': 'Please provide a valid YouTube playlist URL.'})

        # Extract the playlist ID from the URL
        playlist_id = playlist_url.split("list=")[-1]
        
        # YouTube API URL to fetch playlist items
        api_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={playlist_id}&key={YOUTUBE_API_KEY}"
        
        total_seconds = 0
        while api_url:
            response = requests.get(api_url)
            if response.status_code != 200:
                return render(request, 'myapp/index.html', {'error': 'Failed to fetch playlist data. Please check the playlist URL or try again later.'})

            data = response.json()
            
            # Extract the video IDs from the playlist
            video_ids = [item['contentDetails']['videoId'] for item in data.get('items', [])]
            
            # Fetch video details using the video IDs
            video_url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={','.join(video_ids)}&key={YOUTUBE_API_KEY}"
            video_response = requests.get(video_url)

            if video_response.status_code != 200:
                return render(request, 'myapp/index.html', {'error': 'Failed to fetch video details. Please try again later.'})
            
            video_data = video_response.json()
            
            # Calculate total duration
            for video in video_data.get('items', []):
                duration = video['contentDetails']['duration']
                total_seconds += parse_duration(duration)
            
            # Check for next page of results
            api_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={playlist_id}&key={YOUTUBE_API_KEY}&pageToken={data.get('nextPageToken', '')}" if 'nextPageToken' in data else None

        # Convert total seconds to hours, minutes, and seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return render(request, 'myapp/index.html', {
            'hours': int(hours),
            'minutes': int(minutes),
            'seconds': int(seconds)
        })

    return render(request, 'myapp/index.html')

def parse_duration(duration):
    parsed_duration = isodate.parse_duration(duration)
    return int(parsed_duration.total_seconds())