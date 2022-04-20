from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import User, medicine, receipt_medicine, receipt_medicine_detail, category_medicine, patient, bill, examination_schedule
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


class billAdmin(admin.ModelAdmin):
    list_display = ['amount_of_money']


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
admin.site.register(User)
admin.site.register(category_medicine)
admin.site.register(patient)
admin.site.register(bill)
admin.site.register(examination_schedule)

# admin_site.register(Thuoc,ThuocAdmin)
# admin_site.register(DonThuoc)
# admin_site.register(User)
# admin_site.register(DanhMucThuocUong)
# admin_site.register(HoaDon)

