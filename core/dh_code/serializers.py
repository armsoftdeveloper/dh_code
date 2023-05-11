from rest_framework import serializers
from .models import *

# Serializers RU

class BasicSerializerRU(serializers.ModelSerializer):
    class Meta:
        model = BasicRU
        fields = "__all__"

class EtapsSerializerRU(serializers.ModelSerializer):
    class Meta:
        model = EtapsRU
        fields = "__all__"
        
class ServicesSerializerRU(serializers.ModelSerializer):
    class Meta:
        model = ServicesRU
        fields = "__all__"

class AdvantagesSerializerRU(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesRU
        fields = "__all__"

class ReviewsSerializerRU(serializers.ModelSerializer):
    class Meta:
        model = ReviewsRU
        fields = "__all__"

# Serializers EN

class BasicSerializerEN(serializers.ModelSerializer):
    class Meta:
        model = BasicEN
        fields = "__all__"

class EtapsSerializerEN(serializers.ModelSerializer):
    class Meta:
        model = EtapsEN
        fields = "__all__"

class ServicesSerializerEN(serializers.ModelSerializer):
    class Meta:
        model = ServicesEN
        fields = "__all__"

class AdvantagesSerializerEN(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesEN
        fields = "__all__"

class ReviewsSerializerEN(serializers.ModelSerializer):
    class Meta:
        model = ReviewsEN
        fields = "__all__"

# DEFAULT SERIALIZERS FOR ALL LANUGAGES

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
