from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Prediction


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'username', 'email', 'bio']


class PredictionForm(ModelForm):
    class Meta:
        model = Prediction
        fields = ['country', 'instrument', 'decade', 'mood', 'topic']
        labels = {
            'country': 'Which country would you like to visit more?',
            'instrument': 'Choose the instrument you like the most',
            'decade': 'Choose your favorite decade',
            'mood': 'What mood are you in right now?',
            'topic': 'Choose a topic',
        }
