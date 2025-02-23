class CartPage:
    def __init__(self, page):
        self.checkoutBtn = page.get_by_role("link", name="CHECKOUT")
        self.paymentFirstName = page.get_by_test_id("firstName")
        self.paymentLastName = page.get_by_test_id("lastName")
        self.paymentPostalCode = page.get_by_test_id("postalCode")
        self.paymentContinueBtn = page.get_by_role("button", name="CONTINUE")

    def inputPaymentInfo(self, firstName, lastName, postalCode):
        self.paymentFirstName.fill(firstName)
        self.paymentLastName.fill(lastName)
        self.paymentPostalCode.fill(postalCode)
        self.paymentContinueBtn.click()