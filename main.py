

from abc import ABC, abstractmethod
from dataclasses import dataclass



@dataclass
class Product:
    name: str
    price : int



class Store(ABC):
    
    @abstractmethod
    def __init__(self):
        self._money = 0
        self.name = ""
        self._products = {}

    @abstractmethod
    def show_product(self, product_id):
        pass

    @abstractmethod
    def sell_product(self, product_id):
        pass
        

class GrabStore(Store):
    def __init__(self, products):
        self._money = 0
        self.name = "GrabMarket"
        self._products = products

    def set_money(self, money:int):
        self._money = money


    def set_products(self, products):
        self._products = products

    def show_product(self, product_id):
        return self._products.get(product_id, None)

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
        return self._products.pop(product_id)


class User:
    def __init__(self, money, store:Store):
        self._money = money
        self.store = store
        self.belongs = []

    def get_money(self):
        return self._money

    def get_belongs(self):
        return self.belongs

    def get_store(self):
        return self.get_store

    def see_product(self, product_id):
        product = self.store.show_product(product_id)
        return product

    def purchase_product(self, product_id):
        product  = self.store.show_product(product_id)
        price = product.price

        if self._check_money_enough(price=price):
            self._give_money(money= price)
            try:
                my_product = self.store.sell_product(product_id, money = price)
                self.add_belong(my_product)
                return my_product
            except Exception as e :
                self._take_money(money= price)
                print(f"구매 중 문제가 발생했습니다. {str(e)}")
        else:
            raise Exception("잔돈이 부족합니다.")
        

    def _give_money(self, money):
        if not self._check_money_enough(price = money):
            raise Exception("나는 돈이 없어요 ㅠㅠ.")
        self._money -= money

    def _take_money(self, money):
        self._money += money

    def _check_money_enough(self, price):
        return self._money >= price

    def add_belong(self, product):
        self.belongs.append(product)



if __name__ == "__main__":
    store = GrabStore(
        products = {
            1: Product(name="키보드", price= 30000),
            2: Product(name="냉장고", price= 50000),

        }
    )

    user = User(money = 120000, store = store)

    user.purchase_product(product_id=2)
    print(f"user의 잔돈 : {user.get_money()}")
    print(f"user가 구매한 상품 : {user.get_belongs()}")
    print(f"GrabStore 남은 상품 : {store._products}")