from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_check_onboarding(mobile_management_android):
    with (step("Skip onboarding")):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("The Free Encyclopedia"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("New ways to explore"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("Reading lists with sync"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")).click()

        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(have.text("Data & Privacy"))
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_done_button")).click()

        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView"))[0].should(have.text("Search Wikipedia"))


def test_search_wiki(mobile_management_android):
    with step("Skip onboarding"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with step("Type search"):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(
            have.text("Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Wikipedia")

    with step("Verify content found"):
        results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text("Wikipedia"))
