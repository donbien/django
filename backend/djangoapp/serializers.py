from django.contrib.auth.models import User, Group
from rest_framework  import serializers
from djangoapp.models import  Patient, Blood_group, Name, User
from rest_framework.relations import HyperlinkedIdentityField



class UserSerializer(serializers.HyperlinkedModelSerializer):
	password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

	
	class Meta:
		model = User
		fields = ['url','email','username','password', 'password2']
		extra ={
		      'password':{'write_only' : True}
		}

	def save(self):

		user = User(
			email = self.validated_data['email'],
			username = self.validated_data['username'],
			)
		password = self.validated_data['password'],
		password2 = self.validated_data['password2'],

		if password != password2:
			raise serializers.ValidationError({'password:Password must match'})
		user.set_password(password)
		user.save()


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url','name']


class Blood_groupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blood_group
		fields = ['url','code','display']

		def save(self):
			blood_group = Blood_group(
				code = self.validated_data['code'],
				display = self.validated_data['display']
				)
			blood_group.save()


class PatientSerializer(serializers.HyperlinkedModelSerializer):

	#since these are foreign key twe hyperlinked then view_name = name which is the Name model 
	PatientName = serializers.HyperlinkedIdentityField(view_name ='name-detail',read_only = True)
	# Blood_group = Blood_groupSerializer(many = True, read_only =True)
	Blood_group = serializers.SlugRelatedField(
		many = True,
		read_only = True,
		slug_field = 'Blood_group'
	)

	class Meta:
		model = Patient
		fields = ['url','PatientName','email','Gender','MaritalStatus','Blood_group','birthday']

		def save(self):
			patient = Patient(
				PatientName = self.validated_data['PatientName'],
				email = self.validated_data['email'],
				Gender = self.validated_data['Gender'],
				MaritalStatus = self.validated_data['MaritalStatus'],
				Blood_group = self.validated_data['Blood_group'],
				birthday = self.validated_data['birthday']

				)
			patient.save()





class NameSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Name
		fields = ['url','text','use','family','given']

		def save(self):
			name = Name(
				text    =  self.validated_data['text'],
				use     =  self.validated_data['use'],
				family  =  self.validated_data['family'],
				given   =  self.validated_data['given']
				)
			name.save()



# class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
# 	password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
	
# 	class Meta:
# 		model = User
# 		fields = ['url','email','username','password', 'password2']
# 		extra ={
# 		      'password':{'write_only' : True}
# 		}

# 	def save(self):
# 		user = User(
# 			email = self.validated_data['email'],
# 			username = self.validated_data['username'],
# 			)
# 		password = self.validated_data['password'],
# 		password2 = self.validated_data['password2'],

# 		if password != password2:
# 			raise serializers.ValidationError({'password:Password must match'})
# 		user.set_password(password)
# 		user.save()



