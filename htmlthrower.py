from urllib import request
from http.client import HTTPResponse


def gather_download_links(page_url):
    html_string = ''
    try:
        response = request.urlopen(page_url)
        html_bytes = HTTPResponse.read(response)
        html_string = str(html_bytes.decode("utf-8"))
    except:
        print("error finding page")
        return ''
    return html_string

