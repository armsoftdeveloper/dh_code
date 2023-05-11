# Rest Framework
from rest_framework import status
from django.core.mail import EmailMessage
from rest_framework.response import Response
# Serializer
from .serializers import *
# View
from rest_framework import generics


# Views RU

class BasicAPIViewRU(generics.ListCreateAPIView):
    queryset = BasicEN.objects.all()
    serializer_class = BasicSerializerRU

class EtapsAPIViewRU(generics.ListCreateAPIView):
    queryset = EtapsRU.objects.all()
    serializer_class = EtapsSerializerRU


class ServicesAPIViewRU(generics.ListCreateAPIView):
    queryset = ServicesRU.objects.all()
    serializer_class = ServicesSerializerRU

class AdvantagesAPIViewRU(generics.ListCreateAPIView):
    queryset = AdvantagesRU.objects.all()
    serializer_class = AdvantagesSerializerRU

class ReviewsAPIViewRU(generics.ListCreateAPIView):
    queryset = ReviewsRU.objects.all()
    serializer_class = ReviewsSerializerRU


# Views EN

class BasicAPIViewEN(generics.ListCreateAPIView):
    queryset = BasicEN.objects.all()
    serializer_class = BasicSerializerEN

class EtapsAPIViewEN(generics.ListCreateAPIView):
    queryset = EtapsEN.objects.all()
    serializer_class = EtapsSerializerEN

class ServicesAPIViewEN(generics.ListCreateAPIView):
    queryset = ServicesEN.objects.all()
    serializer_class = ServicesSerializerEN

class AdvantagesAPIViewEN(generics.ListCreateAPIView):
    queryset = AdvantagesEN.objects.all()
    serializer_class = AdvantagesSerializerEN

class ReviewsAPIViewEN(generics.ListCreateAPIView):
    queryset = ReviewsEN.objects.all()
    serializer_class = ReviewsSerializerEN

# DEFAULT VIEWS

class MessagesAPIView(generics.ListCreateAPIView):
    def post(self, request, format=None):
        serializer = MessagesSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            phone = serializer.validated_data['phone']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            email_subject = 'Новое сообщение'
            email_body = f'Имя: {name}\nЭлектронная почта: {email}\nСообщение: {message}\nТелефон: {phone}'
            email = EmailMessage(
                email_subject,
                email_body,
                'arm.vardanyan9559@gmail.com',
                ['armsoftdeveloper@gmail.com'],
                reply_to=[email],
            )
            email.send()
            return Response({'success': 'Email sent successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PortfolioAPIView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ContactAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer