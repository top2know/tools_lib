import requests
from skimage import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# https://github.com/pytube/pytube/issues/526
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


def download_file_by_url(url, file_to):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_to, 'wb') as f:
            for chunk in r.iter_content(256):
                f.write(chunk)
    else:
        raise Exception(f'Запрос завершился некорректно и вернул статус {r.status_code}')


def plot_file_by_url(url):
    # https://www.tutorialspoint.com/how-to-plot-a-remote-image-from-http-url-using-matplotlib
    a = io.imread(url)
    plt.imshow(a)
    plt.axis('off')
    plt.show()


def plot_file_by_path(path):
    # https://stackoverflow.com/questions/35286540/display-an-image-with-python
    img = mpimg.imread(path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
