from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class GenerateRegexAPI(APIView):
    def post(self, request):
        print("POST request received")
        return Response({"message": "POST request received"}, status=status.HTTP_200_OK)