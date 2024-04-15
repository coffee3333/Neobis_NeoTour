from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from neotour.pagination import CustomPagination
from neotour.models import TourCategory, Tour, Review, TourBook
from neotour.serializers import CategorySerializer, TourSerializer, ReviewSerializer, TourBookSerializer
from neotour.permissions import ReadOnlyOrCreateOnlyAuthenticated



class CategoryList(generics.ListCreateAPIView):
    queryset = TourCategory.objects.all()
    serializer_class = CategorySerializer


class TourListView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    parser_classes = (MultiPartParser, FormParser)
    pagination_class = CustomPagination


    @swagger_auto_schema(
        operation_description="Этот эндпоинт позволяет получить "
        "список туров. Вы можете применить "
        "поиск по заголовку или по id.",
        responses={200: TourSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                "category_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Отфильтровать туры по id категории.",
            ),
            openapi.Parameter(
                "category_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Отфильтровать туры по названию категории.",
            ),
        ],

    )
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Применение фильтров по категориям, начальной и конечной датам
        category_id = request.query_params.get("category_id")
        category_name = request.query_params.get("category_name")

        if category_id and category_name:
                return Response(
                    {"error": "Search via one parametr"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        if category_name:
            queryset = queryset.filter(category__name=category_name)


        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    parser_classes = (MultiPartParser, FormParser)
    pagination_class = CustomPagination
    permission_classes = [ReadOnlyOrCreateOnlyAuthenticated]


    @swagger_auto_schema(
        operation_description="Этот эндпоинт позволяет получить "
        "список комментариев. Вы можете применить "
        "поиск по заголовку или по id.",
        responses={200: TourSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                "tour_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Отфильтровать комментарии по id тура.",
            ),
            openapi.Parameter(
                "tour_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Отфильтровать комментарии по названию тура.",
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Применение фильтров по категориям, начальной и конечной датам
        tour_id = request.query_params.get("tour_id")
        tour_name = request.query_params.get("tour_name")

        if tour_id and tour_name:
                return Response(
                    {"error": "Search via one parametr"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if tour_id:
            queryset = queryset.filter(tour__id=tour_id)
        if tour_name:
            queryset = queryset.filter(tour__name=tour_name)

        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TourBookView(generics.ListCreateAPIView):
    queryset = TourBook.objects.all()
    serializer_class = TourBookSerializer

    def perform_create(self, serializer):
        tour_id = self.request.data.get('tour')
        tour = get_object_or_404(Tour, id=tour_id)
        serializer.save(tour=tour)

