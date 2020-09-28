from bs4 import BeautifulSoup
import requests

class Grabber:
    header = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, "
                          "like Gecko) Chrome/57.0.2987.98 Safari/537.36"}
    link_template = "https://i.imgur.com/{}.jpg"

    @classmethod
    def get_direct_links(cls, url):
        session = requests.Session()
        response = session.post(url, headers=cls.header) # Todo, check page status

        soup = BeautifulSoup(response.text, "html.parser")
        found_images = soup.findAll("div", itemtype="http://schema.org/ImageObject")
        images_codes = [found_image.get("id") for found_image in found_images]
        direct_links = [cls.link_template.format(code) for code in images_codes]
        return direct_links