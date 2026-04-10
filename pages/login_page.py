class LoginPageClass:
    def LoginPageSelectors(self,page):
        self.page=page
        self.loginfield='//a[text()="Log in"]'
        self.username='//input[@id="loginusername"]'
        self.password='//input[@id="loginpassword"]'
        self.loginBtn='//button[text()="Log in"]'

    def loginFn(self,username, password)
        self.page.click(self.loginfield)
        self.page.fill(self.username)
        self.page.fill(self.password)
        self.page.click(self.loginBtn)

        
        
        