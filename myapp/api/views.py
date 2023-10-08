from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework import status
from myapp.api.serializers import WatchListSerializer,ReviewSerializer
from myapp.models import WatchList,Review
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from myapp.api.permissions import AdminOrReadOnly,ReviewUserOrReadOnly


class WatchListAV(APIView):
    permission_classes=[AdminOrReadOnly]
    def get(self,request):
        watchlist=WatchList.objects.all()
        serializer=WatchListSerializer(watchlist,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class WatchDetailAV(APIView):
    permission_classes=[AdminOrReadOnly]
    def get(self, request,pk):
        try:
            watchlist=WatchList.objects.get(id=pk)
            serializer=WatchListSerializer(watchlist)
            return Response(serializer.data)
        except:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        watchlist=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(watchlist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        watchlist=WatchList.objects.get(pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

class ReviewListVW(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        
        return Review.objects.filter(watchlist=pk)
    
class ReviewCreateVW(generics.CreateAPIView):
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        user=self.request.user
        watchlist=WatchList.objects.get(pk=pk)
        review=Review.objects.filter(user=user,watchlist=watchlist)
        if review.exists():
            raise  ValidationError('Review already exists')
        if watchlist.number_ratings == 0:
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(serializer.validated_data['rating']+ watchlist.avg_rating)/2
        watchlist.number_ratings +=1
        watchlist.save() 
        serializer.save(watchlist=watchlist,user=user)
            
class ReviewDetailVW(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[ReviewUserOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)