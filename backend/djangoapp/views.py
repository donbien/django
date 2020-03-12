from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from djangoapp.serializers import UserSerializer,PatientSerializer, NameSerializer, Blood_groupSerializer
from .models import User, Patient, Name, Blood_group
from rest_framework.decorators import api_view





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    @api_view(['POST',])
    def add_user(request):
    	if request.method == 'POST':
    		serializer = UserSerializer(data = request.data)
    		data = {}
    		if serializer.is_valid():
    			user = serializer.save()
    			data['response'] = "User added successfuly"
    			data['username'] = user.username
    			data['email'] = user.email
    		else:
    			data = serializer.errors
    		return Response(data)


# class GroupViewSet(viewsets.ModelViewSet):

#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
	queryset = Patient.objects
	serializer_class = PatientSerializer
	permission_classes =[permissions.IsAuthenticated]

	@api_view(['POST',])

	def add_patient(request):
		if request.method == 'POST':
			serializer = PatientSerializer(data = request.data)
			data = {}
			if serializer.is_valid():
				patient = serializer.save()
				data['response'] = "Patient added successfuly"
				data['PatientName'] = patient.PatientName
				data['email'] = patient.email
				data['Gender'] = patient.Gender
				data['MaritalStatus'] = patient.MaritalStatus
				data['Blood_group'] = patient.Blood_group
				data['Birthday'] = patient.birthday
			else :
				data = serializer.errors
			return Response(data)

class NameViewSet(viewsets.ModelViewSet):
	queryset = Name.objects
	serializer_class = NameSerializer
	permission_classes =[permissions.IsAuthenticated]
	
	@api_view(['POST',])
	def add_Name(self):
		if request.method == 'POST':
			serializer = NameSerializer(data = request.data)
			data = {}

			if serializer.is_valid():
				name = serializer.save()
				data['message'] = "Name added succesfuly"
				data['text'] =  name.text
				data['use']  =  name.use
				data['family'] = name.family
				data['given']  = name.given
			else:
				data = serializer.errors
			return Response(data)

	@api_view(['PUT',])
	def update_name(request, slug):

		try:
			name = Name.objects.get(slug)
		except:
			return Response(status = STATUS.HTTP_404_NOT_FOUND)

		if request.method == 'POST':
			serializer = NameSerializer(name, data= request.data)
			data ={}

			if serializer.is_valid():
				name = serializer.save()
				data['success'] = "update succesfull"
				return Response(data = data)

			return Response(serializer.errors, status = STATUS.HTTP_404_NOT_FOUND)

	@api_view(['DELETE',])

	def delete_name(request, slug):
		try:
			name = Name.objects.get(slug)
		except:
			return Response(status = STATUS.HTTP_404_NOT_FOUND)

		if request.method == 'DELETE':
			operation = name.delete()
			data = {}

			if operation:
				data['success'] = "delete successfuly"
			else:
				data['fail'] = "unable to delete name "

				return Response(data = data)
			return Response(data = data)
	



class BloodViewSet(viewsets.ModelViewSet):
	queryset = Name.objects
	serializers_class = Blood_groupSerializer
	permission_classes = [permissions.IsAuthenticated]



# class RegistrationViewSet(viewsets.ModelViewSet):
# 	queryset = User.objects
# 	serializer_class = RegistrationSerializer
# 	@api_view(['POST',])
# 	def registration_view(request):
# 		if request.method == 'POST':
# 			serializer = RegistrationSerializer(data = request.data)
# 			data = {}
# 			if serializer.is_valid():
# 				user = serializer.save()
# 				data['response'] = "successfuly register user"
# 				data['email'] = user.email
# 				data['username'] = user.username
# 			else:
# 				data = serializer.errors

# 			return Response(data)





	

	


  


   
