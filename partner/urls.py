from rest_framework.routers import DefaultRouter
from django.urls import include, path
from partner.views import AllPartnerView, PartnerDetailsView, PartnerView

router = DefaultRouter()
router.register("partner_detail", PartnerDetailsView, basename="course_detail")
router.register("partner_list", AllPartnerView, basename="All_partner")

urlpatterns = [
    path('router/', include(router.urls)),
    path('', PartnerView.as_view(), name='partnerlist')

]
