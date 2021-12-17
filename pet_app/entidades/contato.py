class Contato():
    def __init__(self, nome_completo, email, telefone, mensagem):
        self.__nome_completo = nome_completo
        self.__email = email
        self.__telefone = telefone
        self.__mensagem = mensagem
        
    @property
    def nome_completo(self):
        return self.__nome_completo

    @nome_completo.setter
    def nome_completo(self, nome_completo):
        self.__nome_completo = nome_completo

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone


    @property
    def mensagem(self):
        return self.__mensagem

    @mensagem.setter
    def mensagem(self, mensagem):
        self.__mensagem = mensagem


