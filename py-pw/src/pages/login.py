class LoginPage:
    def __init__(self, page):
        self.username = page.get_by_test_id("username")
        self.password = page.get_by_test_id("password")
        self.loginBtn = page.get_by_role("button", name="LOGIN")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginBtn.click()