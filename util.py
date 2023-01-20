import random
import re

import requests
from bs4 import BeautifulSoup


class Grabber:
    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) Chrome/57.0.2987.98 Safari/537.36"}
    img_url_template = "https://i.imgur.com/{}.jpg"

    @classmethod
    def get_direct_links(cls, url):
        session = requests.Session()
        response = session.post(url, headers=cls.header)  # Todo, check page status

        soup = BeautifulSoup(response.text, "html.parser")
        found_images = soup.findAll("div", itemtype="https://schema.org/ImageObject")
        images_codes = [found_image.get("id") for found_image in found_images]
        direct_links = [cls.img_url_template.format(code) for code in images_codes]
        return direct_links


def verify_link(url):
    re_url_pattern = "^https://imgur.com/(a|gallery)/[a-zA-Z0-9]{5,7}$"
    if re.match(re_url_pattern, url):
        return True
    return False


def get_links(request):
    imgur_url = request.form['imgur_url_field']
    message_error = "an unexpected error occurred"
    message_wrong_url = "no valid imgur url found"
    message_no_images = "unable to find images :/"
    if not verify_link(imgur_url):
        return {'message': message_wrong_url}

    try:
        link_list = Grabber.get_direct_links(imgur_url)
        link_list = [link + "\n" for link in link_list]
    except Exception as e:
        return {'message': message_error}

    return {'link_list': link_list, 'message': message_no_images, 'imgur_url': imgur_url}
