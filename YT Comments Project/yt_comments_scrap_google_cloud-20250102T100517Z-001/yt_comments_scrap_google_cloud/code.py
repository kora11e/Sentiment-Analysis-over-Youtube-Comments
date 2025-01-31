from googleapiclient.discovery import build
import pandas as pd

# Function to fetch YouTube comments
def fetch_youtube_comments(video_id, api_key, max_results=100):
    # Initialize the YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # List to store comments data
    comments_data = []

    # API request for comments
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )

    while request:
        response = request.execute()
        
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments_data.append({
                "User": comment["authorDisplayName"],
                "Comment": comment["textDisplay"],
                "Likes": comment["likeCount"],
                "Published At": comment["publishedAt"],
                "Time Ago": comment["updatedAt"]
            })
        
        # Get the next page token, if available
        request = youtube.commentThreads().list_next(request, response)

    return pd.DataFrame(comments_data)

# Usage Example
if __name__ == "__main__":
    # Replace with your API key and video ID
    API_KEY = "AIzaSyCj7RSTCRueH-EEpWqvH7Ny8RJQTuPbjAQ"
    VIDEO_ID = "UXR_bqyAy4E"

    comments_df = fetch_youtube_comments(VIDEO_ID, API_KEY)
    
    # Save to a CSV file
    comments_df.to_csv("bbc-capitol.csv", index=False)
    print("Comments saved to youtube_comments.csv")
