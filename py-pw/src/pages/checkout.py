class CheckoutPage:
    def __init__(self, page):
        self.finishBtn = page.get_by_role("link", name="FINISH")