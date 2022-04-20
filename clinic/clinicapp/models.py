from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class User(AbstractUser):
    avatar = models.ImageField(null=True, blank=True, upload_to='user/%Y/%m')


class ModelBase(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True #Tạo lớp trường tượng


class receipt_medicine(ModelBase):
    symptom = RichTextField(max_length=255)
    diagnostic = RichTextField(max_length=255)
    medicines = models.ManyToManyField('medicine', through='receipt_medicine_detail', related_name='receipt_madicine', blank=True)
    # ngayKham = models.DateTimeField(auto_now_add=True)
    # bacsi = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    # hoadon = models.ForeignKey('HoaDon', on_delete=models.SET_NULL,null=True,related_name="donthuoc")
    # danhmuc = models.ManyToManyField('DanhMucThuocUong') # 1 đơn thuốc có thể có nhiều danh mục và
    #                                                 # 1 danh mục có thể thuộc nhiều đơn thuốc khác nhau

    def __str__(self):
        return self.id


# class examination_schedule(ModelBase):
#     date_examination = models.DateTimeField()
    # benhnhan = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)


# class patient(ModelBase):
#     pass


class medicine(ModelBase):
    name = models.CharField(max_length=100, null=False, unique=True)
    quantity = models.IntegerField()
    price = models.CharField(max_length=255, null=True)
    description = RichTextField(max_length=255, null=True)
    image = models.ImageField(upload_to="medicine/%Y/%m")

    def __str__(self):
        return self.name



class receipt_medicine_detail(ModelBase):
    receipt_medicine = models.ForeignKey(receipt_medicine, on_delete=models.CASCADE)
    medicine = models.ForeignKey(medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    use = RichTextField(max_length=255)


class category_medicine(ModelBase):
    name = models.CharField(max_length=255)
    medicine = models.ManyToManyField(medicine, related_name='category_medicine', blank=True)


# class bill(ModelBase):
#     amount_of_money = models.CharField(max_length=255)


# class DanhMucThuocUong(ModelBase):
#     tenDanhMuc = models.CharField(max_length=255, unique=True)
#     thuoc = models.ManyToManyField('Thuoc')
#
#     def __str__(self):
#         return self.tenDanhMuc
#
#
# class Thuoc(ModelBase):
#     tenThuoc =models.CharField(max_length=100, null=False, unique=True)
#     giaTien = models.CharField(max_length=100, null=False)
#     congDung = RichTextField(max_length=255)
#     image = models.ImageField(upload_to='medicines/%Y/%m',default=None)
#
#
#     def __str__(self):
#         return self.tenThuoc
#
#
# class HoaDon(ModelBase):
#     chiPhiRaToa = models.IntegerField()
#     tienKham = models.IntegerField()
#
#     def __str__(self):
#         return self.tienKham
