# demo/image/urls.py. File urls bạn tự tạo ra nhé :)
from rest_framework.routers import DefaultRouter
from image.views import ImageViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet, basename='image')
urlpatterns = router.urls


