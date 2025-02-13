# from django import forms

# class CreateTaskForm(forms.ModelForm):
#     deadline = forms.SplitDateTimeField(label='締切')

#     class Meta:
#         model = Post
#         fields = '__all__'



# from django import forms
# from django.utils import timezone

# class CreateTaskForm(forms.Form):
#     PRIORITY = (
#         ('1', '高'),
#         ('2', '中'),
#         ('3', '低'),
#     )

#     title = forms.CharField(
#         label='タイトル',
#         max_length=100
#     )
#     status = forms.BooleanField(
#         label = 'ステータス',
#         required = False
#     )
#     priority = forms.ChoiceField(
#         label = '優先度',
#         choices = PRIORITY
#     )
#     deadline = forms.DateTimeField(
#         label = '締切',
#         widget = forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
#         input_formats = ['%Y-%m-%dT%H:%M']
#     )
#     text = forms.CharField(
#         label = '詳細',
#         widget = forms.Textarea
#     )