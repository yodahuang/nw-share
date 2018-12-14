import os
import re
from pathlib import Path

from flask import Flask, request
from flask_restful import Api, Resource
from flask_restful.utils import cors

from pytube import YouTube

app = Flask(__name__)
api = Api(app)

youtube_pattern = re.compile(r'(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+')

outer_dir = Path(os.path.abspath(__file__)).parents[1]
download_dir = outer_dir / 'downloads'
download_dir.mkdir(exist_ok=True)

class GeneralHandler(Resource):
    @cors.crossdomain(origin='*')
    def put(self):
        url = request.form['url']
        is_youtube = re.match(youtube_pattern, url) is not None
        print('Got url: {}'.format(url))
        if is_youtube:
            yt = YouTube(url)
            downloaded_path = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path=str(download_dir))
            file_name = os.path.basename(downloaded_path)
            return file_name
        else:
            return 'Not implemented yet!'

    @cors.crossdomain(origin='*')
    def get(self):
        return "hello world"


api.add_resource(GeneralHandler, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)