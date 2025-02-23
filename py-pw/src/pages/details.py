from pages.header import HeaderComponent

class DetailsPage(HeaderComponent):
    def __init__(self, page):
        HeaderComponent.__init__(self, page)
        self.cartBtn = page.get_by_role("button", name="ADD TO CART")