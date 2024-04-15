from rest_framework import serializers
from neotour.models import TourCategory, Tour, Review, TourBook
from authentication.serializers import UserSerializer


class TourSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()
    category = serializers.PrimaryKeyRelatedField(queryset=TourCategory.objects.all())

    class Meta:
        model = Tour
        fields = ['id', 'name', 'photo', 'description', 'location', 'category']


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TourCategory
        fields = ['id', 'name']


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'tour', 'author', 'text', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Assuming `request.user` is the author and is authenticated
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class TourBookSerializer(serializers.ModelSerializer):
    tour = serializers.PrimaryKeyRelatedField(queryset=Tour.objects.all())

    class Meta:
        model = TourBook
        fields = ['tour', 'phone_number', 'commentary', 'number_of_people']
