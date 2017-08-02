from django import forms
from .models import Post

'''
class PostForm(forms.Form):
    # Form은 모두 CharField()이다. DB를 제외하고는 길이가 짧든 길든 다 문자열이다.
    # 그래서 폼클래스에는 CharField() 밖에 없는 것이다.
    author = forms.CharField()
    title = forms.CharField()
    content = forms.CharField()
'''

class PostForm(forms.ModelForm): # forms의 ModelForm을 상속받음.
    class Meta:
        model = Post
        fields = '__all__';
        '''fields = '__all__';의 의미
        모든 필드를 지정한다. autor = forms.CharField(), title = forms.CharField(), content = forms.Charfield()를 자동으로 생성함.
        필드만 지정하면 정보를 알아서 다 가져온다.
        '''
        # fields = ['author', 'title', 'content']
