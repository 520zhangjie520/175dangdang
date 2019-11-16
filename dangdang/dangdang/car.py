from index.models import TBook, TUser, TShop


#========定义购物车类========
class Car():
    def __init__(self):
        self.car_item=[]
        self.save_price=0
        self.all_price=0
    #---------增加商品-------
    def add(self,id,number=1):
        book=TBook.objects.get(id=id)
        for i in self.car_item:
            if book == i.book:
                print(type(i.number))
                i.number+=int(number)
                break
        else:
            self.car_item.append(Car_i(book,number))
        self.sums()
        # print(222,self.all_price,self.save_price)
    #---------修改商品--------
    def update(self,id,number):
        book=TBook.objects.get(id=id)
        for i in self.car_item:
            print(i.book,book)
            if i.book==book:
                i.number=number
                break
        self.sums()
    #------------删除商品----------
    def dele(self,id):
        for i in self.car_item:
            if i.book.id==int(id):
                self.car_item.remove(i)
                print('删除了')
                break
        self.sums()
    #------------计算总价-----------
    def sums(self):
        self.all_price=0
        self.save_price=0
        print(type(self.car_item))
        for i in self.car_item:
            self.all_price+=i.book.dangdang_price*int(i.number)
            self.save_price+=(float(i.book.real_price)-float(i.book.dangdang_price))*int(i.number)


#========定义商品详情类=======
class Car_i():
    def __init__(self,book,number):
        self.book=book
        self.number=number


#=======定义---数据库de增/删/改=======
class Sql():
    #-----添加------
    def add(self,username,car_inf):
        user = TUser.objects.get(username=username)
        for i in car_inf.car_item:
            shop_inf = TShop.objects.filter(user_id=user.id,book_id=i.book.id)
            if shop_inf:
                shop_inf[0].number=i.number
                shop_inf[0].all_price=car_inf.all_price
                shop_inf[0].save_price=car_inf.save_price
                shop_inf[0].save()
            else:
                TShop.objects.create(user_id=user.id, book_id=i.book.id, number=i.number, save_price=car_inf.save_price,all_price=car_inf.all_price)
    #---------修改-----------
    def update(self,id,number,car,user_id):
        a = TShop.objects.get(book_id=id,user_id=user_id)
        print(number)
        a.number = number
        a.save_price = car.save_price
        a.all_price = car.all_price
        a.save()
    #---------删除----------
    def dele(self,user_id,id):
        a = TShop.objects.get(book_id=id,user_id=user_id)
        a.delete()