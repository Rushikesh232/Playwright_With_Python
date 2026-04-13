#TC02 – Verify Product in Cart
from pages.login_page import LoginPageClass
from pages.home_page import HomePageClass

def tcAddToCart(page)
    page.goto('https://www.demoblaze.com/')

    login = LoginPageClass(page)
    login.loginFn('panvol', 'test@123')

    addToCart = HomePageClass(page)
    addToCart.addToCartFn('Nexus 6')
