from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models.user import User


class LoginForm(FlaskForm):
    username = StringField(
        "Usuário",
        validators=[DataRequired(message="Por favor, informe seu usuário ou e-mail")],
    )
    password = PasswordField(
        "Senha", validators=[DataRequired(message="Por favor, informe sua senha")]
    )
    submit = SubmitField("Entrar")


class RegisterForm(FlaskForm):
    name = StringField(
        "Nome Completo",
        validators=[
            DataRequired(message="Por favor, informe seu nome completo"),
            Length(min=3, max=100, message="O nome deve ter entre 3 e 100 caracteres"),
        ],
    )

    username = StringField(
        "Nome de Usuário",
        validators=[
            DataRequired(message="Escolha um nome de usuário"),
            Length(
                min=3,
                max=20,
                message="O nome de usuário deve ter entre 3 e 20 caracteres",
            ),
        ],
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Por favor, informe seu e-mail"),
            Email(message="E-mail inválido. Use o formato: exemplo@email.com"),
        ],
    )

    password = PasswordField(
        "Senha",
        validators=[
            DataRequired(message="Crie uma senha para sua conta"),
            Length(min=6, max=50, message="A senha deve ter entre 6 e 50 caracteres"),
        ],
    )

    password_confirm = PasswordField(
        "Confirmar Senha",
        validators=[
            DataRequired(message="Por favor, confirme sua senha"),
            EqualTo("password", message="As senhas não coincidem"),
        ],
    )

    submit = SubmitField("Registrar")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Este nome de usuário já está em uso. Escolha outro.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "Este e-mail já está cadastrado. Faça login ou use outro e-mail."
            )
