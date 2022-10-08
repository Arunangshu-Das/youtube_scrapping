import re
from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests

app = Flask(__name__)

api_key='AIzaSyDPSuuv5S7uJntDCCOBxs8CrRjYkSWZLc4'
channel_id='UCnz-ZXXER4jOvuED5trXfEA'
# channel_ids = ['UCnz-ZXXER4jOvuED5trXfEA', # techTFQ
#                'UCLLw7jmFsvfIVaUFsLs8mlQ', # Luke Barousse 
#                'UCiT9RITQ9PW6BhXK0y2jaeg', # Ken Jee
#                'UC7cs8q-gJRlGwj4A8OmCmXg', # Alex the analyst
#                'UC2UXDak6o7rBm23k3Vv5dww' # Tina Huang
#               ]

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def answer():
    channel_id=request.form['exampleInputEmail1']

    api_key='AIzaSyDPSuuv5S7uJntDCCOBxs8CrRjYkSWZLc4'
    youtube=build('youtube','v3',developerKey=api_key)
    def get_channel_stats(youtube,channel_id):
        request=youtube.channels().list(
        part='snippet,contentDetails,statistics',id=channel_id)
        respons=request.execute()
        datas=[]
        
        for i in range(len(respons['items'])):
            data=dict(Channel_name= respons['items'][i]['snippet']['title'],
                    Subscribers= respons['items'][i]['statistics']['subscriberCount'],
                    views=respons['items'][i]['statistics']['viewCount'],
                    Total_videos=respons['items'][i]['statistics']['videoCount'],
                    playlist_id = respons['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
            datas.append(data)
        return datas
    channel_stat=get_channel_stats(youtube,channel_id)
    channel_data=pd.DataFrame(channel_stat)
    channel_data['Subscribers']=pd.to_numeric(channel_data['Subscribers'])
    channel_data['views']=pd.to_numeric(channel_data['views'])
    channel_data['Total_videos']=pd.to_numeric(channel_data['Total_videos'])
    playlist_id = channel_data['playlist_id'][0]
    def get_video_ids(youtube, playlist_id):
        
        request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId = playlist_id,
                    maxResults = 50)
        response = request.execute()
        
        video_ids = []
        
        for i in range(len(response['items'])):
            video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
        next_page_token = response.get('nextPageToken')
        more_pages = True
        
        while more_pages:
            if next_page_token is None:
                more_pages = False
            else:
                request = youtube.playlistItems().list(
                            part='contentDetails',
                            playlistId = playlist_id,
                            maxResults = 50,
                            pageToken = next_page_token)
                response = request.execute()
        
                for i in range(len(response['items'])):
                    video_ids.append(response['items'][i]['contentDetails']['videoId'])
                
                next_page_token = response.get('nextPageToken')
            
        return video_ids
    video_ids=get_video_ids(youtube,playlist_id)
    def get_video_details(youtube, video_ids):
        all_video_stats = []
        
        for i in range(0, len(video_ids), 50):
            request = youtube.videos().list(
                        part='snippet,statistics',
                        id=','.join(video_ids[i:i+50]))
            response = request.execute()
            
            for video in response['items']:
                video_stats = dict(Title = video['snippet']['title'],
                                Published_date = video['snippet']['publishedAt'],
                                Views = video['statistics']['viewCount'],
                                Likes = video['statistics']['likeCount'],
                                thumbnails = video['snippet']['thumbnails']['high']['url'],
                                Comments = video['statistics']['commentCount']
                                )
                all_video_stats.append(video_stats)
        
        return all_video_stats
    video_details=get_video_details(youtube,video_ids)
    # ans=dict( videoId=video_ids,
    #     videoDetails=video_details
    # )
    ans=[]
    for i in range(len(video_ids)):
        aa={"videoId":"https://www.youtube.com/watch?v="+video_ids[i],"videoDetails":video_details[i]}
        ans.append(aa)
    print(ans)
    return render_template("results.html",aa=ans)
    # return jsonify(str(ans))

if __name__=='__main__':
    app.run()