from django.urls import path, include
from .views import index, match_details, today_matchs, tomorrow_matchs, j2_matchs
from rest_framework.routers import DefaultRouter
from .views import DataViewSet, MatchsAVenirViewSet, IframeViewSet

router = DefaultRouter()
router.register('matchs_a_venir', MatchsAVenirViewSet)
router.register('datas', DataViewSet)
router.register('iframes', IframeViewSet)

urlpatterns = [
    path('', index, name="blog-index"),
    path('soccer-bet/', today_matchs, name="blog-today_matchs"),
    path('soccer-bet/tomorrow', tomorrow_matchs, name="blog-tomorrow_matchs"),
    path('soccer-bet/after-tomorrow', j2_matchs, name="blog-j2_matchs"),
    path("match-details/<str:slug>/", match_details, name="blog-match_details"),
    path('api/', include(router.urls)),
    path("dj-rest-auth/", include('dj_rest_auth.urls'))
]
