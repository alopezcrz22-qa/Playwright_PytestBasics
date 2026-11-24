from playwright.sync_api import expect


class ConfirmationPage:
    def __init__(self, page):
        self.page = page

    def confirmPage(self):
        #expect(self.page.locator("h1[class='hero-primary']")).to_have_text(' Thankyou for the order. ')
        messageConfirm = self.page.locator("h1[class='hero-primary']")
        return messageConfirm