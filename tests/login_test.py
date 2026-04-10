from pages.login_page import LoginPageClass

def tcLogin(page):
    page.goto('https://www.demoblaze.com/')

    login=LoginPageClass(page)
    login.loginFn('panvol', 'test@123')
     
    