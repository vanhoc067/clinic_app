from django.contrib import admin
from django.template.response import TemplateResponse
from django.views import View
from django.utils.html import mark_safe
from .models import User, medicine, receipt_medicine, receipt_medicine_detail, category_medicine, patient, bill, \
    examination_schedule, regulation
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from django.db.models import Sum
from datetime import datetime
from django.db.models.functions import Extract

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

    list_display = ['patient', 'id', 'symptom', 'diagnostic', 'medicines']
    list_filter = ['id', 'patient']
    search_fields = ['id']


class medicine_Form(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        models = medicine
        fields = '__all__'


class medicine_Admin(admin.ModelAdmin):
    form = medicine_Form
    readonly_fields = ['image_view']

    list_display = ['id', 'name', 'quantity', 'price', 'description']
    list_filter = ['id', 'name']
    search_fields = ['name']

    def image_view(self, Lesson):
        if Lesson:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=Lesson.image.name))



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
    list_display = ['examination_schedule_patient', 'date_examination', 'authentication']
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


class regulation_Admin(admin.ModelAdmin):
    list_display = ['maximum', 'minimum', 'active']


class ClinicAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG DANG KY KHAM CHUA BENH'
    site_title = 'PM-OU'

    def get_urls(self):
        return [
                   path('sales_stats/', self.sales_stats),
                   path('patient_stats/', self.patient_stats)
               ] + super().get_urls()

    def sales_stats(self, request, month=None, year=None):
        bills = bill.objects.select_related('bill_receipt_medicine').all()
        stats = []
        money = 0

        for detail in bills:
            money= money+int(detail.amount_of_money)
            stats.append([detail.id, detail.bill_receipt_medicine.patient, detail.created_date, detail.amount_of_money,
                         detail.active])

        if month and year:
            if type(month) is not int and month is not None:
                month = int(month)
            if type(year) is not int and year is not None:
                year = int(year)
            # stats = stats.filter(stats[0] == 1)
                                 # extract('date', stats[2]) == date, \
                                 # extract('month', bill.create_date) == month, \
                                 # extract('year', stats[2]) == year)
        return TemplateResponse(request, 'admin/sales_stats.html', {
            'stats': stats,
            'money': money,
        })


    def patient_stats(self, request, month=None, year=None, date=None):
        current_user = request.user
        patients = patient.objects.raw(
                     'SELECT id, created_date, COUNT(id) AS count FROM clinicapp_patient GROUP BY created_date'
                )

        if date and month and year:
            if type(date) is not int and month is not None:
                date = int(date)
            if type(month) is not int and month is not None:
                month = int(month)
            if type(year) is not int and year is not None:
                year = int(year)
            patients = patients.filter(Extract('date', patients.created_date) == date, \
                                        Extract('month', patients.create_date) == month, \
                                        Extract('year', patients.created_date) == year)

        # experiment = patients.objects.annotate(
        #      d = Extract('created_date', 'date')).get()

        return TemplateResponse(request, 'admin/patient_stats.html', {
            'patients': patients,
        })

    def is_accessible(self):
        return current_user.is_authenticated

admin_site = ClinicAppAdminSite(name="My Clinic")


admin_site.register(medicine, medicine_Admin)
admin_site.register(receipt_medicine, receipt_medicine_Admin)
admin_site.register(receipt_medicine_detail, receipt_medicine_detail_Admin)
admin_site.register(User)
admin_site.register(category_medicine, category_medicine_Admin)
admin_site.register(patient, patientAdmin)
admin_site.register(bill, bill_Admin)
admin_site.register(examination_schedule, examination_schedule_Admin)
admin_site.register(regulation, regulation_Admin)


admin.site.register(medicine, medicine_Admin)
admin.site.register(receipt_medicine, receipt_medicine_Admin)
admin.site.register(receipt_medicine_detail, receipt_medicine_detail_Admin)
admin.site.register(User)
admin.site.register(category_medicine, category_medicine_Admin)
admin.site.register(patient, patientAdmin)
admin.site.register(bill, bill_Admin)
admin.site.register(examination_schedule, examination_schedule_Admin)
admin.site.register(regulation, regulation_Admin)




