from rest_framework import views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import EmployeeSerializer, CategorySerializer, GetCategorySerializer,GetSubCategorySerializer,\
    SubCategorySerializer,ItemSerializer,GetItemSerializer, LastUpdatedItemSerializer,ItemPostSerializer,\
    CategoryBackupSerializer,ItemBackupViewSerializer,SubCategoryBackupSerializer
from .models import Employee, Category, SubCategory, Item
from django.http import JsonResponse

from datetime import datetime
# Create your views here.


class CategoryView(views.APIView):

    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        '''
        Register
        ---
        parameters:
            - name: employee_id
              required: True
              type: number
            - name: first_name
              required: True
              type: string
            - name: last_name
              required: True
              type: string
            - name: password
              required: True
              type: string
        '''
        serializer = CategorySerializer(data=request.data)
     #   print (serializer.initial_data)
        if not serializer.is_valid():
            res = {
                'code': 2,
            }
            for key, val in serializer.errors.items():
                res['message'] = key + ": " + val[0]
            return JsonResponse(res)

        serializer.save()
        res = {
            'code': 0,
            'message': 'Category Registration Successful'
        }
        return JsonResponse(res)

    def get(self, request):
        """
        This API fetches all Categories .
        """
        categories  = Category.objects.filter(is_deleted=False).order_by('order_number')
        serializer = GetCategorySerializer(categories, many=True)
        res = {
            'error': 0,
            'detail': '',
            'response': serializer.data
        }
        return Response(data=res, status=status.HTTP_200_OK)
        



class SubCategoryView(APIView):
    """
    Get all Categories 
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
        if 'category_id' in request.GET:
            id = request.GET['category_id']
            if id is not None and id != '':
                id = int(id)
                subcategories  = SubCategory.objects.filter(category_id = id, is_deleted=False).order_by('order_number')
                serializer = GetSubCategorySerializer(subcategories, many=True)
                res = {
                    'error': 0,
                    'detail': '',
                    'response': serializer.data
                }
                return Response(data=res, status=status.HTTP_200_OK)
        else:
            res = {
                'error': 1,
                'detail': 'Category Id is missing',
                'response': ""
            }
            return Response(data=res, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        '''
        Register
        ---
        parameters:
            - name: employee_id
              required: True
              type: number
            - name: name
              required: True
              type: string
            - name: type
              required: True
              type: string
            - name: logo
              required: True
              type: string
        '''
        serializer = SubCategorySerializer(data=request.data)
     #   print (serializer.initial_data)
        if not serializer.is_valid():
            res = {
                'code': 2,
            }
            for key, val in serializer.errors.items():
                res['message'] = key + ": " + val[0]
            return JsonResponse(res)

        serializer.save()
        res = {
            'code': 0,
            'message': 'Category Registration Successful'
        }
        return JsonResponse(res)



class ItemView(APIView):
    """
    Get all Categories 
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
     
        category_id = ''
        sub_category_id = ''
        last_update = ''

        if 'last_update' in request.GET:
            last_update = datetime.strptime(request.GET.get('last_update'),"%Y-%m-%dT%H:%M:%S.%fZ")
        if 'category_id' in request.GET:
            category_id = int(request.GET.get('category_id'))
        if 'sub_category_id' in request.GET:
            sub_category_id = int(request.GET.get('sub_category_id'))

        if last_update != '':
            items = Item.objects.filter(created_time__gt=last_update, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)
        if category_id != '' and sub_category_id == '':
            items  = Item.objects.filter(category_id = category_id, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)
        if category_id == '' and sub_category_id != '':
            items  = Item.objects.filter(sub_category_id = sub_category_id, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        if category_id != '' and sub_category_id != '':
            items  = Item.objects.filter(category_id = category_id, sub_category_id = sub_category_id, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        else:
            res = {
                'error': 1,
                'detail': 'Category Id or Subcategory Id is missing',
                'response': ""
            }
            return Response(data=res, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        '''
        Register
        ---
        parameters:
            - name: employee_id
              required: True
              type: number
            - name: name
              required: True
              type: string
            - name: type
              required: True
              type: string
            - name: logo
              required: True
              type: string
        '''
        # serializer = ItemSerializer(data=request.data)
        # serializer = GetItemSerializer(data=request.data, many=True)
        serializer = ItemPostSerializer(data=request.data, many=True)
     #   print (serializer.initial_data)
        if not serializer.is_valid():
            res = {
                'code': 2,
            }
            for key, val in serializer.errors.items():
                res['message'] = key + ": " + val[0]
            return JsonResponse(res)

        serializer.save()
        res = {
            'code': 0,
            'message': 'Item Registration Successful'
        }
        return JsonResponse(res)
        


    


class RegisterView(views.APIView):

    permission_classes = [AllowAny, ]

    def post(self, request, format=None):
        '''
        Register
        ---
        parameters:
            - name: employee_id
              required: True
              type: number
            - name: first_name
              required: True
              type: string
            - name: last_name
              required: True
              type: string
            - name: password
              required: True
              type: string
        '''
        serializer = EmployeeSerializer(data=request.data)
     #   print (serializer.initial_data)
        if not serializer.is_valid():
            res = {
                'code': 2,
            }
            for key, val in serializer.errors.items():
                res['message'] = key + ": " + val[0]
            return JsonResponse(res)

        serializer.save()
        res = {
            'code': 0,
            'message': 'Employee Registration Successful'
        }
        return JsonResponse(res)

    def put(self, request, format=None):
        '''
        Register
        ---
        parameters:
            - name: employee_id
              required: True
              type: number
        '''
        try:
            emp = Employee.objects.get(employee_id=request.data.get('employee_id'))
        except:
            res = {
                'code': 1,
                'message': 'No Employee exist for entered Employee ID',
            }
            return JsonResponse(res)

        emp.is_admin = True
        emp.save()
        res = {
            'code': 0,
            'message': 'Changed to Admin'
        }
        return JsonResponse(res)

class CategoryBackupView(views.APIView):

    permission_classes = [AllowAny, ]
    def get(self, request):
        """
        This API fetches all Categories .
        """
        categories  = Category.objects.all().order_by('-created_time')
        serializer = CategoryBackupSerializer(categories, many=True)
        res = {
            'error': 0,
            'detail': '',
            'response': serializer.data
        }
        return Response(data=res, status=status.HTTP_200_OK)

class SubCategoryBackupView(APIView):
    """
    Get all Categories
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        subcategories = SubCategory.objects.all().order_by('-created_time')
        serializer = SubCategoryBackupSerializer(subcategories, many=True)
        res = {
            'error': 0,
            'detail': '',
            'response': serializer.data
        }
        return Response(data=res, status=status.HTTP_200_OK)

class ItemBackupView(APIView):
    """
    Get all Categories
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        items = Item.objects.all().order_by('-created_time')
        serializer = ItemBackupViewSerializer(items, many=True)
        res = {
            'error': 0,
            'detail': '',
            'response': serializer.data
            }
        return Response(data=res, status=status.HTTP_200_OK)

class LastUpdateItemView(APIView):
    """
    Get last update time of item
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches last update time of item .
        """
        items = Item.objects.latest('created_time')
        serializer = LastUpdatedItemSerializer(items)
        res = {
            'error': 0,
            'detail': '',
            'response': serializer.data
        }
        return Response(data=res, status=status.HTTP_200_OK)

class NewsView(APIView):
    """
    Get all Categories
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
        last_update = ''

        if 'last_update' in request.GET:
            last_update = datetime.strptime(request.GET.get('last_update'), "%Y-%m-%dT%H:%M:%S.%fZ")

        if last_update != '':
            items = Item.objects.filter(category_id = 2, created_time__gt=last_update, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        if last_update == '':
            items = Item.objects.filter(category_id = 2, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        else:
            res = {
                'error': 1,
                'detail': 'No news found',
                'response': ""
            }
            return Response(data=res, status=status.HTTP_200_OK)

class FlashNewsView(APIView):
    """
    Get all Categories
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
        items = Item.objects.filter(category_id = 2, is_deleted=False).order_by('-created_time')[:20]
        serializer = GetItemSerializer(items, many=True)
        res = {
            'error': 0,
            'detail': '',
            'response': serializer.data
        }
        return Response(data=res, status=status.HTTP_200_OK)

class ViharUpdateView(APIView):
    """
    Get all Categories
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
        last_update = ''

        if 'last_update' in request.GET:
            last_update = datetime.strptime(request.GET.get('last_update'), "%Y-%m-%dT%H:%M:%S.%fZ")

        if last_update != '':
            items = Item.objects.filter(category_id = 13, created_time__gt=last_update, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        if last_update == '':
            items = Item.objects.filter(category_id = 13, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        else:
            res = {
                'error': 1,
                'detail': 'No news found',
                'response': ""
            }
            return Response(data=res, status=status.HTTP_200_OK)

class AalekhView(APIView):
    """
    Get all Categories
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
        last_update = ''

        if 'last_update' in request.GET:
            last_update = datetime.strptime(request.GET.get('last_update'), "%Y-%m-%dT%H:%M:%S.%fZ")

        if last_update != '':
            items = Item.objects.filter(category_id = 15, created_time__gt=last_update, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        if last_update == '':
            items = Item.objects.filter(category_id = 15, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        else:
            res = {
                'error': 1,
                'detail': 'No news found',
                'response': ""
            }
            return Response(data=res, status=status.HTTP_200_OK)

class VideoView(APIView):
    """
    Get all Categories
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
        last_update = ''

        if 'last_update' in request.GET:
            last_update = datetime.strptime(request.GET.get('last_update'), "%Y-%m-%dT%H:%M:%S.%fZ")

        if last_update != '':
            items = Item.objects.filter(category_id = 11, created_time__gt=last_update, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        if last_update == '':
            items = Item.objects.filter(category_id = 11, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        else:
            res = {
                'error': 1,
                'detail': 'No news found',
                'response': ""
            }
            return Response(data=res, status=status.HTTP_200_OK)

class PhotoView(APIView):
    """
    Get all Categories
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        """
        This API fetches all Categories .
        """
        last_update = ''

        if 'last_update' in request.GET:
            last_update = datetime.strptime(request.GET.get('last_update'), "%Y-%m-%dT%H:%M:%S.%fZ")

        if last_update != '':
            items = Item.objects.filter(category_id = 10, created_time__gt=last_update, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        if last_update == '':
            items = Item.objects.filter(category_id = 10, is_deleted=False).order_by('order_number','-created_time')
            serializer = GetItemSerializer(items, many=True)
            res = {
                'error': 0,
                'detail': '',
                'response': serializer.data
            }
            return Response(data=res, status=status.HTTP_200_OK)

        else:
            res = {
                'error': 1,
                'detail': 'No news found',
                'response': ""
            }
            return Response(data=res, status=status.HTTP_200_OK)
