from rest_framework.routers import DefaultRouter

from play.myapi.viewsets import HeroViewSet
from play.rental.viewsets import FriendViewSet, BelongingViewSet, BorrowedViewSet
from play.employee.viewsets import EmployeeViewSet



router = DefaultRouter()


router.register(
      'heroes',
      HeroViewSet,
      basename='myapi',
)

router.register(
      'friends',
      FriendViewSet,
      basename='friend-api',
)

router.register(
      'belongings',
      BelongingViewSet,
      basename='belonging-api',
)

router.register(
      'borrowings',
      BorrowedViewSet,
      basename='borrowing-api',
)

router.register(
      'employee',
      EmployeeViewSet,
      basename='employee-api',
)