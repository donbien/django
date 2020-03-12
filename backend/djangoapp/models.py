from django.db import models


# Create your models here.
class User(models.Model):
	id       = models.AutoField(primary_key=True)
	username = models.CharField(max_length=30, null = False, blank = False)
	email    = models.EmailField(max_length=100, null = False, blank = False)
	password = models.CharField(max_length=20, null = False, blank = False)
	password2= models.CharField(max_length=20, null = False, blank = False)

	def __str__(self):
		return "{}".format(self.username)

class Patient(models.Model):

	Gender = (

	  ('M', ('Male')),
	  ('F', ('Female')),
     ('Other', ('Other')),

	)

	MaritalStatus = (
	("Single", ("Single")),
	("Married", ("Married")),
	("Window(er)",("Window(er)")),
	("Nan",("None")),

	)
	PatientId       = models.AutoField(primary_key=True)
	PatientName     = models.ForeignKey('Name', on_delete = models.CASCADE, null = False, blank=False)
	email           = models.EmailField(max_length=30, null=False, blank=False)
	gender          = models.CharField(max_length=10, null= False,  choices = Gender)
	MaritalStatus   = models.CharField(max_length=10, null =False, choices = MaritalStatus)
	Blood_group     = models.ForeignKey('Blood_group', on_delete = models.CASCADE, null = False, blank = False)
	birthday      = models.DateField(null = False)

	def __str__(self):
		return "{} {}".format(self.PatientName, self.PatientName)



class Blood_group(models.Model):
	code = (
	('1',('A+')),
	('2',('A-')),
	('3',('B+')),
	('4',('B-')),
	('5',('O+')),
	('6',('O-')),
	('7',('AB+')),
	('8',('AB-')),
	)

	display =(
	('A+',('A+')),
	('A-',('A-')),
	('B+',('B+')),
	('B-',('B-')),
	('O+',('O+')),
	('O-',('O-')),
	('AB+',('AB+')),
	('AB-',('AB-')),
	)

	id      = models.AutoField(primary_key = True)
	code    = models.CharField(max_length =5, null= False, choices = code),
	display = models.CharField(max_length = 5, null = False, choices = display)

	def __str__(self):
		return "{} {}".format(self.code, self.display)

	def __iter__(self):
		return iter(self)
		
class Name(models.Model):
	id       = models.AutoField(primary_key = True)
	use      = models.CharField(max_length = 30, null = False,  blank = False)
	text     = models.CharField(max_length = 30, null = False,  blank = False)
	family   = models.CharField(max_length = 30, null = False,  blank = False)
	given    = models.CharField(max_length = 30, null = False,   blank  =False)

	def __iter__(self):
		return iter(self)

# 

# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.conf import settings
# from django.db.models.signals import post_save


# # Create your models here.
# class UserManager(BaseUserManager):

# 	def create_user(self, username, email, password=None,password2=None):
# 		if not email:
# 			raise ValueError('User must have an email')
# 		if not username:
# 			raise ValueError('User must have username')

# 		user = self.model(
# 			email = self.normalize_email(email),
# 			username = username,
# 			password = password,
# 			password2 = password2,
# 		)

# 		is_admin = True,
# 		is_staff = True, 
# 		is_superuser = True,
# 		user.save(using= self.db)
# 		return user

# class User(AbstractUser):
# 	email = models.EmailField(verbose_name ="email", max_length =100, null = False, unique =True, blank =False)
# 	username = models.CharField(max_length=30, unique = True)
# 	# date_join = models.DateTimeField(verbose_name ="date_join", auto_now_add = True)
# 	# last_login = models.DateTimeField(verbose_name ="last_login", auto_now = True)


# 	USERNAME_FIELD = 'email'
# 	REQUIRED_FIELDS = ['username']

# 	objects = UserManager()

# 	def __str__(self):
# 		return self.email


# 	def has_permis(self, perm, obj=None):
# 		return self.is_admin

# 	def has_module_perms(self, app_label):
# 		return True
