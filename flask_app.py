from flask import Flask, request, render_template, make_response
from io import StringIO
import urllib
import csv
import mainStoryScory

app = Flask(__name__)
requiredInfo=[]

@app.route('/')
@app.route('/scory_story_v1')
def scory_story_v1_search():
    return render_template('/searchScoryStoryV1.html', 
                           css_source='../static/app.css', 
                           activeTab='scory_story_v1')

@app.route('/scory_story_v1_result', methods=['POST'])
def scory_story_v1_result():
    story = request.form['sent']
    classification, songGenre, vidId = mainStoryScory.runProgram(story)
    
    return render_template('/resultScoryStoryV1.html',
                           sent=story, genre=classification, musicGenre=songGenre, youtube_id=vidId, 
                           css_source='../static/app.css', 
                           activeTab='scory_story_v1')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)