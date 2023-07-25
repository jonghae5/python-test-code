from main import Store, Product
import requests

class GrabRealStore(Store):
    def __init__(self, url="https://fakestoreapi.com"):
        self._money = 0
        self.name = "GrabMarket"
        self.url = url

    def set_money(self, money:int):
        self._money = money


    def show_product(self, product_id):
        # requests
        res = requests.get(url = f"{self.url}/products/{product_id}")
        product = res.json()

        return Product(name=product['title'], price=product.get('price',None))
    
    def sell_product(self, product_id, money):
        product = self.show_product(product_id)

        if not product:
            raise Exception("상품이 존재하지 않습니다.")

        self._take_money(money=money)

        try:
            _product = self._take_out_product(product_id=product_id)
            return _product
        except Exception as e:
            self._return_money(money)
            raise e 
    

    def _take_money(self, money):
        self._money += money

    def _return_money(self, money):
        self._money -= money

    def _take_out_product(self, product_id):
        res = requests.delete(url = f"{self.url}/products/{product_id}")
        product = res.json()

        return Product(name=product.get('title',None), price=product.get('price',None))


if __name__=="__main__":
    store = GrabRealStore()
    result = store.show_product(product_id=1)
    print(result)