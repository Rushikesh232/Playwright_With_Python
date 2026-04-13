class HomePageClass:
    def HomePageSelectors(self, page):
        self.page=page
        self.phoneList='//div[@id="tbodyid"]'
        phoneList = self.phoneList

    def addToCartFn(self, phoneSelected):
        for phone in self.phoneList:
             if phoneSelected == phone:
                 self.page.click(f"text={phone}")
                 break
            
       
            
             
       

    