from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, pagination
from .models import patient, examination_schedule, receipt_medicine, medicine, receipt_medicine_detail, category_medicine, bill, Comment, User, regulation

class PatientSerializer(ModelSerializer):
    class Meta:
        model = patient
        fields = ['id', 'name', 'gender', 'phone', 'user']


class ExaminationScheduleSerializer(ModelSerializer):
    class Meta:
        model = examination_schedule
        fields = ['id', 'date_examination', 'examination_schedule_patient']


class ReceiptMedicineSerializer(ModelSerializer):
    class Meta:
        model = receipt_medicine
        fields = ['id', 'symptom', 'diagnostic', 'patient', 'medicines']


class MedicineSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, obj):
        request = self.context['request']
        if obj.image and not obj.image.name.startswith('/static'):
            path = '/static/%s' % obj.image.name

            return request.build_absolute_uri(path)

    class Meta:
        model = medicine
        fields = ['name', 'quantity', 'price', 'image']


class MedicineDetailSerializer(MedicineSerializer):
    like = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    def get_like(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            return obj.like_set.filter(user=request.user,
                                       active=True).exists()  # phương thức exists trả về đối tượng true/false

    def get_rating(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            return obj.rating_set.filter(user=request.user,
                                       active=True).exists()  # phương thức exists trả về đối tượng true/false

    class Meta:
        model = MedicineSerializer.Meta.model
        fields = MedicineSerializer.Meta.fields + ['description', 'like', 'rating']


class MedicinCateSerializer(ModelSerializer):
    class Meta:
        model = medicine
        fields = ['name']


class CategoryMedicineSerializer(ModelSerializer):
    medicine = MedicinCateSerializer(many=True)

    class Meta:
        model = category_medicine
        fields = ['id', 'name', 'medicine']


class ReceiptMedicineDetailSerializer(ModelSerializer):
    class Meta:
        model = receipt_medicine_detail
        fields = ['id', 'quantity', 'use', 'receipt_medicine', 'medicine']


class BillSerializer(ModelSerializer):
    class Meta:
        model = bill
        fields = ['id', 'amount_of_money', 'bill_receipt_medicine']


class UserSerializer(serializers.ModelSerializer):
    avatar_path = serializers.SerializerMethodField(source='avatar')

    def get_avatar_path(self, obj):
        request = self.context['request']
        if obj.avatar and not obj.avatar.name.startswith('/static'):
            path = '/static/%s' % obj.avatar.name

            return request.build_absolute_uri(path)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'password', 'avatar_path']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'avatar_path': {
                'read_only': True
            },
            'avatar': {
                'write_only': True
                }

        }

    def create(self, validated_date):
        data = validated_date.copy()

        u = User(**data)
        u.set_password(u.password)
        u.save()

        return u


class CreateCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'user', 'medicine']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        exclude = ['active']


class RegulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = regulation
        exclude = ['maximum', 'minimum', 'active']