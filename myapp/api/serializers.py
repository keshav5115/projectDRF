from rest_framework import serializers
from myapp.models import WatchList,Review

class  ReviewSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    watchlist=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        fields='__all__'

class  WatchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    avg_rating=serializers.StringRelatedField(read_only=True)
    number_reviews=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=WatchList
        fields='__all__'
        
        
