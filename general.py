import downloader
import htmlthrower
from parser import ImageFinder
import re


def get_file_name(url):
    if not url:
        return None
    fname = re.findall('filename=(.+)', url)
    if len(fname) <= 0:
        return None
    return fname[0]

def download(comic_name, page_url):
    start = 0
    html = htmlthrower.gather_download_links(page_url)
    parsed_html = ImageFinder()
    parsed_html.feed(html)
    download_links = parsed_html.__dict__
    print(download_links['image_links'])

    for pages in (download_links['image_links']):
        print('downloading ...' + str(start+1))
        start = start + 1
        downloader.downloader(pages, comic_name+'\\' + (str(start)+'.jpg'))
