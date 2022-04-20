from django.http import HttpResponse


def index(request):
    return HttpResponse("e-Clinic App")

#
# from django.shortcuts import render
# from django.http import HttpResponse
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework import viewsets, permissions, status
# from rest_framework.response import Response
# from rest_framework import generics
# from rest_framework.views import APIView
# from django.conf import settings
# from .models import Thuoc,DanhMucThuocUong,User,HoaDon,LichKham
# from .serializers import ThuocSerializer,DanhMucThuocSerializer,UserSerializer,HoaDonSerializer,LichKhamSerializer
# from rest_framework.decorators import action
# from rest_framework.parsers import MultiPartParser
# from .paginators import BasePagination
#
#
# class UserViewSet(viewsets.ViewSet,generics.CreateAPIView,generics.ListAPIView):
#     queryset = User.objects.filter(is_active=True)
#     serializer_class = UserSerializer
#     parser_classes = [MultiPartParser, ]
#
#     def get_permissions(self): # phương thức lấy thông tin người dùng phải ở trạng thái đăng nhập
#         if self.action == 'get_current_user':
#             return [permissions.IsAuthenticated()]
#
#         return [permissions.AllowAny()]
#
#     @action(methods=['get'],detail=False,url_path="current-user") # phương thức lấy thông tin người dùng
#     def get_current_user(self,request):
#         return Response(self.serializer_class(request.user).data,status=status.HTTP_200_OK)
# #
# #
# class AuthInfo(APIView):  # lấy API của người dùng
#     def get(self, request):
#         return Response(settings.OAUTH2_INFO, status=status.HTTP_200_OK)
#
#
# class ThuocViewSet(viewsets.ModelViewSet,generics.ListAPIView):# tạo ra 5 bộ API
#     # list (GET) --> xem danh sách thuốc
#     #... (POST) --> thêm thuốc
#     # detail --> xem chi tiết thuốc
#     #...(PUT) --> cập nhật
#     #...(DELETE) --> xóa thuốc
#     queryset = Thuoc.objects.filter(active=True)
#     serializer_class = ThuocSerializer
#     pagination_class = BasePagination
#
#     @swagger_auto_schema(
#         operation_description='API này dùng để ẩn thuốc từ phía client',
#         responses={
#             status.HTTP_200_OK: ThuocSerializer()
#         }
#     )
#     # permission_classes = [permissions.IsAuthenticated] # tất cả các API phải ở trạng thái đăng nhập mới được truy vấn
#
#     # demo thao tác xem danh sách ( ai cũng xem được ) trừ các hành động còn lại thì k làm dc
#     # def get_permissions(self):
#     #     if self.action == 'list':
#     #         return [permissions.AllowAny()]
#     #
#     #     return [permissions.IsAuthenticated()]
#     # demo thao tác ẩn đi thuốc
#
#     @action(methods=['post'],detail=True,url_path="hide-thuoc",url_name="hide_thuoc")
#     def hide_thuoc(self,request,pk):
#         try: # xử lý ngoại lệ nếu người dùng đưa vào 1 id thuốc không có trong hệ thống thì ném ra ngoại lệ
#             t = Thuoc.objects.get(pk=pk)
#             t.active=False
#             t.save()
#         except Thuoc.DoesNotExits:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#         return Response(data=ThuocSerializer(t,context={'request':request}).data,status=status.HTTP_200_OK)
#
#
# class DanhMucViewSet(viewsets.ModelViewSet,generics.ListAPIView):
#     queryset = DanhMucThuocUong.objects.filter(active=True)
#     serializer_class = DanhMucThuocSerializer
#
#
# class HoaDonViewSet(viewsets.ModelViewSet, generics.CreateAPIView):
#     queryset = HoaDon.objects.filter(active=True)
#     serializer_class = HoaDonSerializer
#
#
# class LichKhamViewSet(viewsets.ModelViewSet,generics.CreateAPIView):
#     queryset = LichKham.objects.filter(active=True)
#     serializer_class = LichKhamSerializer
#
#
#
#
# def index(request):
#     return render(request,template_name='index.html',context = {
#         'name':'Thinh Pham'
#     })
