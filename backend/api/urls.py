from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    CountryList,
    CountryDetail,
    CityList,
    CityDetail,
    CountryViewSet,
    CityViewSet,
    CategoryViewSet,
    SubcategoryViewSet,
    AdViewSet,
    ImageViewSet,
    TagViewSet,
    CategoryList,
    CategoryDetail,
    SubcategoryList,
    SubcategoryDetail,
    AdList,
    AdDetail,
    ImageList,
    ImageDetail,
    TagList,
    TagDetail,
)

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'cities', CityViewSet, basename='city')
router.register(r'subcategories', SubcategoryViewSet, basename='subcategory')
router.register(r'ads', AdViewSet, basename='ad')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    # URLs for views without viewsets
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('subcategories/', SubcategoryList.as_view(), name='subcategory-list'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory-detail'),
    path('ads/', AdList.as_view(), name='ad-list'),
    path('ads/<int:pk>/', AdDetail.as_view(), name='ad-detail'),
    path('images/', ImageList.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
    path('countries/', CountryList.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),
    path('cities/', CityList.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetail.as_view(), name='city-detail'),
]

# Include the router URLs
urlpatterns += router.urls
