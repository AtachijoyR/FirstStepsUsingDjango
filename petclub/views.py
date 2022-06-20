from django.shortcuts import render

# Create your views here.
# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # PRUEBA
        return Response(data="Hello, World !", status=200) # respuesta del servicio
    def patch(self, request): #Sobrescribe el comportamiento del anterior para
        return Response(data="Me encuentro en patch", status = 200)
    def delete(self,request):
        return Response(data = "Me encuentro en delete", status = 200)
    def post(self, request):
        return Response(data = "Me encuentro en post", status = 200)
class PetView(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio
    def patch(self, request): #Sobrescribe el comportamiento del anterior para
        return Response(data="Me encuentro en patch", status = 200)
    def delete(self,request):
        return Response(data = "Me encuentro en delete", status = 200)
    def post(self, request):
        return Response(data = "Me encuentro en post", status = 200)

class PersonView(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio
    def patch(self, request): #Sobrescribe el comportamiento del anterior para
        return Response(data="Me encuentro en patch", status = 200)
    def delete(self,request):
        return Response(data = "Me encuentro en delete", status = 200)
    def post(self, request):
        return Response(data = "Me encuentro en post", status = 200)

#class PetListAPIView(ListAPIView):
 #   def get(self, request):
  #      pets = Pet.object.all()
   #     pets_serializer = CustomPetSerializer(pets, many=True)
    #    return Response(data = pets_serializer.data(), status = 200)

#class petAPIView(RetrieveAPIView): #se debe poner en la URL
 #   def get(self, request):
  #      return Response(data = "Mi mascota",status = 200)