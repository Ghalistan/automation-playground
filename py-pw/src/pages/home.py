class HomePage:
    def __init__(self, page):
        self.page = page

    def clickItem(self, itemName):
        self.page.get_by_role("link", name=itemName).click()