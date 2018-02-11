import comicname
import general
import os


def make_directory(name):
    os.chdir('comics')
    if not os.path.exists(name):
        print('creating new directory : ' + name)
        os.makedirs(name)


comic_url = 'http://somewebsite.net/comicname'
comic_name = comicname.comic_name(comic_url)
make_directory(comic_name)
general.download(comic_name, comic_url)
