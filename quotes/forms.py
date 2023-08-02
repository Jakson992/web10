from django.forms import ModelForm, CharField, TextInput, ModelMultipleChoiceField, SelectMultiple,ModelChoiceField,Select
from .models import Quote, Author, Tag


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, required=True, widget=TextInput())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'), required=True, widget=SelectMultiple())
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'), widget=Select())

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']
        # exclude = ['tags']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput())
    date_born = CharField(max_length=50, widget=TextInput)
    location_born = CharField(max_length=150, widget=TextInput())
    bio = CharField(widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'date_born', 'location_born', 'bio']


class TagForm(ModelForm):
    name = CharField(max_length=30, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']
