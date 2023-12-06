
import re
from cryptography.fernet import Fernet

# criptografar e descripitografar senhas ==================
key_secret = Fernet.generate_key()
fernet_key = Fernet("ry1fy9Wnjok5871ZJoISH0-t7VZRKIuVws2WbjlCqnc=")
# cripitografando
def cryptography_password(senha):
    return fernet_key.encrypt(senha.encode()).decode()

# descripitografando
def decrypt_password(senha_cripto):
    return fernet_key.decrypt(senha_cripto.encode()).decode()


# validar formato de email
def is_valid_email(email):
    # Verifica se o email tem um formato válido
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+$"
    return re.match(email_regex, email) is not None

# verificar se email ja existe
def email_exists(user, email, lista):
    for stored_user, stored_email, *_ in lista:
        if stored_email == email:
            return True
    return False


# verificar se usuario ja existe
def user_exists(user, email, lista):
    for stored_user, stored_email, *_ in lista:
        if stored_user == user:
            return True
    return False


#formatar cpf ao mudar de foco 
def format_cpf(event):
    entry = event.widget
    text = entry.get()
    if text and len(text) == 11 and text.isdigit():  # Verifica se o texto possui o tamanho de um CPF (sem pontos e traço)
        formatted_cpf = f"{text[:3]}.{text[3:6]}.{text[6:9]}-{text[9:]}"
        entry.delete(0, "end")
        entry.insert(0, formatted_cpf)
        
#verificar se o cpf digitado esta correto para registro
def check_cpf_format(cpf):
    # Define um padrão para o formato do CPF usando uma expressão regular
    pattern = r"\d{3}\.\d{3}\.\d{3}-\d{2}"

    # Verifica se a entrada corresponde ao padrão do CPF
    if re.match(pattern, cpf):
        return True
    else:
        return False
    
#verificar se o valor digitado nos entrys está correto de acordo com o formato brl
def check_real_brl(valor):
    # Expressão regular para validar um valor de moeda no formato brasileiro (BRL)
    pattern = r'^\d+\.\d{2}$'  # Exige um ou mais dígitos, seguidos por um ponto e exatamente dois dígitos

    # Verifica se o valor corresponde ao padrão de moeda BRL
    if re.match(pattern, valor):
        return True
    else:
        return False