from youtube_searc_and_download import YouTubeHandler
 
search_key = 'путин' #keywords
yy = YouTubeHandler(search_key)
yy.download_as_audio =0 # 1- download as audio format, 0 - download as video
yy.set_num_playlist_to_extract(5) # number of playlist to download
 
print ('Get all the playlist')
yy.get_playlist_url_list()
print (yy.playlist_url_list)
 
## Get all the individual video and title from each of the playlist
yy.get_video_link_fr_all_playlist()
for key in  yy.video_link_title_dict.keys():
    print( key, '  ', yy.video_link_title_dict[key])
    print()
print()
 
print ('download video')
yy.download_all_videos(dl_limit =200) #number of videos to download.
