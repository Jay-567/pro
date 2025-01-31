from rest_framework.routers import DefaultRouter
from detail.views import CollegeViews

router=DefaultRouter()
router.register("college",CollegeViews,basename='yourmodel')