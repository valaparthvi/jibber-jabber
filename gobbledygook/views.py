from django.contrib.auth import views
from .forms import WordForm
from random import randint, choice
# Create your views here.


class HomeView(views.FormView):
    form_class = WordForm
    template_name = 'gobbledygook/home.html'

    def form_valid(self, form, **kwargs):
        word_length = form.cleaned_data['word_length']
        alphabets = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z'
        ]
        paragraph = ''
        for i in range(word_length):
            for j in range(1, randint(2, 15)):
                for k in choice(alphabets):
                    paragraph += k
            paragraph += ' '
        context_data = self.get_context_data(**kwargs)
        context_data['paragraph'] = paragraph
        return self.render_to_response(context_data)
