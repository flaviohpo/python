import requests
import json

response = requests.get('https://api.spotify.com/v1/recommendations?limit=10&market=ES&seed_artists=4NHQUGzhtTLFvgF5SZesLK&seed_genres=classical%2Ccountry&seed_tracks=0c6xIDDpzE81m2q797ordA', 
                        headers={'Accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer BQAYzMxZxKG507Yo4gfLhp62vjgdy8qo05CgJ3Os4s_HIFujYi2LsB_QbeAr3TnRbLds_7z8Ft3NA_KypNFFriZeFhOlof0RJp55q32FR7E8lMbyERycgN_ttLlAuewq67ADnQB36gQdlUblLn-h27rhd2rZZuv2Y42eyLjeVSaIfoXD2NjTmKYz6911NM0XAR9OYOi-gg'
                        })

print(response.json())
#Unauthorized - The request requires user authentication or, 
# if the request included authorization credentials, authorization 
# has been refused for those credentials.

