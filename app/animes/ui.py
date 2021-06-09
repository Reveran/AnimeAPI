from entrypoint import app
from flask import render_template
import requests

null = ''

@app.route("/")
def anime_ui(id = ''):
    anime = eval(requests.get('http://127.0.0.1:5000/api/anime/' + id).text)
    kitsu = eval(requests.get('https://kitsu.io/api/edge/anime?filter[text]='+anime["slug"]+'&fields[anime]=youtubeVideoId,synopsis,posterImage,coverImage,titles,averageRating&include=categories&fields[categories]=title&page[limit]=1').text)
    details = kitsu['data'][0]['attributes']
    categories = ''
    trailerVisivility = ''
    for cat in kitsu['included']:
        categories += f"<span class='rounded-pill border border-2 m-1 badge border-white'>{cat['attributes']['title']}</span>"

    if details['coverImage'] == '':
        details['coverImage'] = {'original':"https://www.wallpapertip.com/wmimgs/3-37980_anime-minimalist-wallpaper-4k.jpg?2880x1800"}

    if details['posterImage'] == '':
        details['posterImage'] = {'original':"https://ih1.redbubble.net/image.512138487.5983/fposter,small,wall_texture,product,750x1000.u3.jpg"}

    if details['youtubeVideoId'] == '':
        trailerVisivility = 'visually-hidden'

    return render_template('index.html', anime = anime, details = details, categories = categories, trailerVisivility = trailerVisivility)

@app.route("/<id>")
def by_id(id):
    return anime_ui(id)

@app.route("/about")
def about():
    return render_template('about.html')