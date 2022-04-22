from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import User, medicine, receipt_medicine, receipt_medicine_detail, category_medicine, patient, bill, \
    examination_schedule
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path


class patientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'phone']
    list_filter = ['id', 'created_date']
    search_fields = ['name']


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

    list_display = ['id', 'name', 'quantity', 'price', 'description']
    list_filter = ['id', 'name']
    search_fields = ['name']


class receipt_medicine_detail_Form(forms.ModelForm):
    use = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        models = receipt_medicine_detail
        fields = '__all__'


class receipt_medicine_detail_Admin(admin.ModelAdmin):
    form = receipt_medicine_detail_Form

    list_display = ['receipt_medicine', 'medicine', 'quantity', 'use']
    list_filter = ['receipt_medicine', 'id']
    search_fields = ['id']


class billAdmin(admin.ModelAdmin):
    list_display = ['amount_of_money']


class receipt_medicine_Admin(admin.ModelAdmin):
    list_display = ['symptom', 'diagnostic', 'patient']
    list_filter = ['id', 'created_date']
    search_fields = ['id']


class examination_schedule_Admin(admin.ModelAdmin):
    list_display = ['examination_schedule_patient', 'date_examination']
    list_filter = ['examination_schedule_patient', 'id']
    search_fields = ['id']


class category_medicine_Admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name', 'id']
    search_fields = ['name', 'id']


class bill_Admin(admin.ModelAdmin):
    list_display = ['bill_receipt_medicine', 'amount_of_money']
    list_filter = ['bill_receipt_medicine', 'id']
    search_fields = ['id']


# class ClinicAppAdminSite(admin.AdminSite):
#     site_header = 'HE THONG DANG KY KHAM CHUA BENH'
#
#     def get_urls(self):
#         return [
#             path('clinic-stats/', self.medical_stats)
#         ] + super().get_urls()
#
#     def medical_stats(self,request):
#         medicine_count = medicine.objects.count()
#
#         return TemplateResponse(request,'admin/medical-stats.html',{
#             'medicine_count':medicine_count
#         })
#
#
# admin_site = ClinicAppAdminSite(name="My Clinic")


admin.site.register(medicine, medicine_Admin)
admin.site.register(receipt_medicine, receipt_medicine_Admin)
admin.site.register(receipt_medicine_detail, receipt_medicine_detail_Admin)
admin.site.register(User)
admin.site.register(category_medicine, category_medicine_Admin)
admin.site.register(patient, patientAdmin)
admin.site.register(bill, bill_Admin)
admin.site.register(examination_schedule, examination_schedule_Admin)


