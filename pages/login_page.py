class LoginPageClass:
    def __init__(self,page):
        self.page=page
        self.loginfield='//a[text()="Log in"]'
        self.username='//input[@id="loginusername"]'
        self.password='//input[@id="loginpassword"]'
        self.loginBtn='//button[text()="Log in"]'

    def loginFn(self,username, password):
        self.page.click(self.loginfield)
        self.page.wait_for_timeout(3000)
        self.page.fill(self.username,username)
        self.page.fill(self.password,password)
        self.page.click(self.loginBtn)
        self.page.wait_for_timeout(3000)

        
        
        