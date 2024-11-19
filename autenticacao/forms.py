from django import forms
from autenticacao.models import Usuario
from django.contrib.auth.models import Group


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Senha",
        help_text="Digite uma senha segura."
    )
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
        label="Grupos"
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'groups']

    def save(self, commit=True):
        """
        Sobrescreve o método save para hash da senha.
        """
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password"])  # Criptografa a senha
        if commit:
            usuario.save()
            self.save_m2m()  # Salva os relacionamentos ManyToMany
        return usuario