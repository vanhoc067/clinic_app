from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import medicine, receipt_medicine, receipt_medicine_detail, category_medicine
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path



class receipt_medicine_Form(forms.ModelForm):
    symptom = forms.CharField(widget=CKEditorUploadingWidget)
    diagnostic = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        models = receipt_medicine
        fields = '__all__'


class receipt_medicine_Admin(admin.ModelAdmin):
    form = receipt_medicine_Form
    # class Media:
    #     css = {
    #         'all': ('/static/css/donthuoc.css',)
    #     }


class medicine_Form(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        models = medicine
        fields = '__all__'


class medicine_Admin(admin.ModelAdmin):
    form = medicine_Form


class receipt_medicine_detail_Form(forms.ModelForm):
    use = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        models = receipt_medicine_detail
        fields = '__all__'


class receipt_medicine_detail_Admin(admin.ModelAdmin):
    form = receipt_medicine_detail_Form

#
# class ThuocAdmin(admin.ModelAdmin):
#     class Media:
#         css = {
#             'all': ('/static/css/main.css',)
#         }
#     list_display = ["id","tenThuoc","giaTien","created_date","updated_date"]
#     search_fields = ["tenThuoc","giaTien"]
#     list_filter = ["tenThuoc"]
#     readonly_fields = ["avatar"]
#
#     def avatar(self,thuoc):
#         return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px' />".format(img_url=thuoc.image.name,alt = thuoc.tenThuoc))
#
#
# class DanhMucThuocAdmin(admin.ModelAdmin):
#     list_display = ["id","tenDanhMuc"]
#     search_fields = ["tenDanhMuc","thuoc"]
#     list_filter = ["tenDanhMuc"]
#
#
# class DonThuocInline(admin.StackedInline):
#     model = DonThuoc
#     pk_name = 'hoadon'
#
# class HoaDonAdmin(admin.ModelAdmin):
#     inlines = [DonThuocInline,]
#
#
#
# class MedicalAppAdminSite(admin.AdminSite):
#     site_header = 'HE THONG DANG KY KHAM CHUA BENH'
#
#     def get_urls(self):
#         return [
#             path('medical-stats/', self.medical_stats)
#         ] + super().get_urls()
#
#     def medical_stats(self,request):
#         thuoc_count = Thuoc.objects.count()
#
#         return TemplateResponse(request,'admin/medical-stats.html',{
#             'thuoc_count':thuoc_count
#         })




# admin_site = MedicalAppAdminSite("My Medical")


admin.site.register(medicine,medicine_Admin)
admin.site.register(receipt_medicine, receipt_medicine_Admin)
admin.site.register(receipt_medicine_detail, receipt_medicine_detail_Admin)
# admin.site.register(user)
admin.site.register(category_medicine)
# admin.site.register(HoaDon,HoaDonAdmin)
# admin.site.register(LichKham)

# admin_site.register(Thuoc,ThuocAdmin)
# admin_site.register(DonThuoc)
# admin_site.register(User)
# admin_site.register(DanhMucThuocUong)
# admin_site.register(HoaDon)

