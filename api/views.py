from django.views import generic

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class ApiExample(APIView):
	permission_classes = (permissions.AllowAny,)

	def get(self, request, *args, **kwargs):
		return Response(
			{
                "text": "Hello from django"
            }, status=status.HTTP_200_OK
        )


class ReactView(generic.TemplateView):
	template_name = "index.html"
