from bs4 import BeautifulSoup
import requests


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
        found_images = soup.findAll("div", itemtype="http://schema.org/ImageObject")
        images_codes = [found_image.get("id") for found_image in found_images]
        direct_links = [cls.img_url_template.format(code) for code in images_codes]
        return direct_links


def verify_link(url):
    import re
    re_url_pattern = "^https://imgur.com/(a|gallery)/[a-zA-Z0-9]{5,7}$"
    if re.match(re_url_pattern, url):
        return True
    return False


def build_post_response(request):
    link_list = ""
    message = ""
    imgur_url = request.form['imgur_url_field']

    if not verify_link(imgur_url):
        return {'message': "no valid imgur url found"}

    try:
        link_list = Grabber.get_direct_links(imgur_url)
        link_list = [link + "\n" for link in link_list]
    except Exception as e:
        message = "an unexpected error occurred " + str(e)
    return {'link_list': link_list, 'message': message, 'imgur_url': imgur_url}
