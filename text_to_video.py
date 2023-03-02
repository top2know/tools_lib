from youtubesearchpython import VideosSearch, StreamURLFetcher, Video
from utils import download_file_by_url


def find_videos(text, limit=10, only_links=False):
    videos_search = VideosSearch(text, limit=limit).result()['result']
    if only_links:
        return list(map(lambda x: x['link'], videos_search))
    else:
        return videos_search


def download_video(url, file_to, itag=118):
    # Для ориентира можно смотреть на устаревший, но полезный список
    # https://gist.github.com/sidneys/7095afe4da4ae58694d128b1034e01e2
    # По умолчанию 360p
    fetcher = StreamURLFetcher()
    video = Video.get(url)
    url = fetcher.get(video, itag)

    if url is None:
        streams = fetcher.getAll(video)['streams']
        url = sorted(streams,
                     key=lambda x: x['width'] if 'width' in x else 0)[-1]['url']
    download_file_by_url(url, file_to)
