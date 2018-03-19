from django import forms


class WordForm(forms.Form):
    word_length = forms.CharField()

    def clean_word_length(self):
        word_length = self.data.get('word_length')
        try:
            word_length = int(word_length)
        except ValueError:
            raise forms.ValidationError("Please enter Integer only.")
        return word_length
