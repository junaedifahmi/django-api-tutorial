from .views import ViewCommentModel
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', ViewCommentModel, base_name='comment')

urlpatterns = router.urls
