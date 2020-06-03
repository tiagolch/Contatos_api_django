from contatos.views import contatoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', contatoViewSet)
urlpatterns = router.urls



