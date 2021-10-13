
from rest_framework import viewsets
from .models import UserPost
from .serializer import UserSerializer
from rest_framework.filters import SearchFilter

# Create your views here.
class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',) # 항상 튜플이므로 ',' 필수입력

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.id == 1:
                filtered_queryset = queryset
                return filtered_queryset
            filtered_queryset = queryset.filter(author=self.request.user)
            return filtered_queryset
        else:
            filtered_queryset = queryset.none()
    