from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Country, City, Category, Subcategory, Ad, Image, Tag
from .serializers import (
    CountrySerializer,
    CitySerializer,
    CategorySerializer,
    SubcategorySerializer,
    AdSerializer,
    ImageSerializer,
    TagSerializer,
)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(detail=True, methods=['put'])
    def soft_delete(self, request, pk=None):
        country = self.get_object()
        country.is_deleted = True
        country.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(detail=True, methods=['put'])
    def soft_delete(self, request, pk=None):
        city = self.get_object()
        city.is_deleted = True
        city.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_deleted=False, is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user_id=user.id)

    @action(detail=True, methods=['put'])
    def soft_delete(self, request, pk=None):
        category = self.get_object()
        category.is_deleted = True
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.filter(is_deleted=False, is_active=True)
    serializer_class = SubcategorySerializer

    @action(detail=True, methods=['put'])
    def soft_delete(self, request, pk=None):
        subcategory = self.get_object()
        subcategory.is_deleted = True
        subcategory.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.filter(is_deleted=False, is_active=True)
    serializer_class = AdSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'subcategory']

    @action(detail=True, methods=['put'])
    def soft_delete(self, request, pk=None):
        ad = self.get_object()
        ad.is_deleted = True
        ad.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @action(detail=True, methods=['put'])
    def soft_delete(self, request, pk=None):
        image = self.get_object()
        image.is_deleted = True
        image.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.filter(is_deleted=False, is_active=True)
    serializer_class = TagSerializer

    @action(detail=True, methods=['put'])
    def soft_delete(self, request, pk=None):
        tag = self.get_object()
        tag.is_deleted = True
        tag.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.filter(is_deleted=False, is_active=True)
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.filter(is_deleted=False, is_active=True)
    serializer_class = CategorySerializer


class SubcategoryList(generics.ListCreateAPIView):
    queryset = Subcategory.objects.filter(is_deleted=False, is_active=True)
    serializer_class = SubcategorySerializer


class SubcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.filter(is_deleted=False, is_active=True)
    serializer_class = SubcategorySerializer


class AdList(generics.ListCreateAPIView):
    queryset = Ad.objects.filter(is_deleted=False, is_active=True)
    serializer_class = AdSerializer


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.filter(is_deleted=False, is_active=True)
    serializer_class = AdSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.filter(is_deleted=False, is_active=True)
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.filter(is_deleted=False, is_active=True)
    serializer_class = TagSerializer
