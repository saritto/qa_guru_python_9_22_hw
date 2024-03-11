import allure
import requests
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name="screenshot", attachment_type=AttachmentType.PNG, extension=".png")


def add_xml(browser):
    xml = browser.driver.page_source
    allure.attach(body=xml, name="screen xml dump", attachment_type=allure.attachment_type.XML, extension=".xml")


def attach_bstack_video(session_id, login, password):
    bstack_session = requests.get(f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
                                  auth=(login, password)).json()
    print(bstack_session)
    video_url = bstack_session["automation_session"]["video_url"]

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name="video recording",
        attachment_type=allure.attachment_type.HTML,
    )
