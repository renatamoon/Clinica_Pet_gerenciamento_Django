class ConsultaPet():
    def __init__(self, pet, motivo_consulta, medicamento_atual, medicamentos_prescritos,
                 exames, doutor, especialidade, observacoes, data=""):
        self.__pet = pet
        self.__motivo_consulta = motivo_consulta        
        self.__medicamento_atual = medicamento_atual
        self.__medicamentos_prescritos = medicamentos_prescritos
        self.__exames = exames
        self.__doutor = doutor
        self.__especialidade = especialidade
        self.__observacoes = observacoes
        self.__data = data

    @property
    def pet(self):
        return self.__pet

    @pet.setter
    def pet(self, pet):
        self.__pet = pet

    @property
    def motivo_consulta(self):
        return self.__motivo_consulta

    @motivo_consulta.setter
    def motivo_consulta(self, motivo_consulta):
        self.__motivo_consulta = motivo_consulta
    
    @property
    def medicamento_atual(self):
        return self.__medicamento_atual

    @medicamento_atual.setter
    def medicamento_atual(self, medicamento_atual):
        self.__medicamento_atual = medicamento_atual

    @property
    def medicamentos_prescritos(self):
        return self.__medicamentos_prescritos

    @medicamentos_prescritos.setter
    def medicamentos_prescritos(self, medicamentos_prescritos):
        self.__medicamentos_prescritos = medicamentos_prescritos

    @property
    def exames(self):
        return self.__exames

    @exames.setter
    def exames(self, exames):
        self.__exames = exames

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def doutor(self):
        return self.__doutor

    @doutor.setter
    def doutor(self, doutor):
        self.__doutor = doutor

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidades):
        self.__especialidade = especialidade

    @property
    def observacoes(self):
        return self.__observacoes

    @observacoes.setter
    def observacoes(self, observacoes):
        self.__observacoes = observacoes

