from urllib.request import urlretrieve


def downloader(url, file_name):
    urlretrieve(url, file_name)
