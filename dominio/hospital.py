class Hospital:
    alas = {}
    pacientes = {}

    @classmethod
    def configurar_hospital_para_sessao(cls, nome, capacidade_maxima_alas):
        cls.nome = nome
        if capacidade_maxima_alas < 1:
            raise ValueError("A capacidade máxima de alas deve ser maior ou igual a 1.")
        cls.capacidade_maxima_alas = capacidade_maxima_alas
        cls.alas = {}  
        print(f"Hospital {nome} configurado com capacidade máxima de {capacidade_maxima_alas} alas.")

    @classmethod
    def criar_ala(cls, nome, capacidade):
        if capacidade < 1:
            raise ValueError("A capacidade da ala deve ser maior ou igual a 1.")
        if len(cls.alas) >= cls.capacidade_maxima_alas:
            raise ValueError("Capacidade máxima de alas atingida.")
        cls.alas[nome] = [None] * capacidade
        print(f"Ala '{nome}' criada com capacidade para {capacidade} leitos.")

    @classmethod
    def alocar_paciente(cls, nome_ala, nome_paciente, indice_leito):
        if nome_ala not in cls.alas:
            raise ValueError("Ala não encontrada.")
        ala = cls.alas[nome_ala]
        if indice_leito < 0 or indice_leito >= len(ala):
            raise ValueError("Índice de leito inválido.")
        if ala[indice_leito] is not None:
            raise ValueError("Leito ocupado.")
        ala[indice_leito] = nome_paciente
        print(f"Paciente '{nome_paciente}' alocado no leito {indice_leito + 1} da ala '{nome_ala}'.")

    @classmethod
    def remover_paciente(cls, nome_ala, nome_paciente):
        if nome_ala not in cls.alas:
            raise ValueError("Ala não encontrada.")
        ala = cls.alas[nome_ala]
        for i, paciente in enumerate(ala):
            if paciente == nome_paciente:
                ala[i] = None
                print(f"Paciente '{nome_paciente}' removido da ala '{nome_ala}'.")
                return
        raise ValueError("Paciente não encontrado na ala.")

    @classmethod
    def adicionar_paciente(cls, paciente):
        if paciente.nome in cls.pacientes:
            raise ValueError("Paciente já está registrado.")
        cls.pacientes[paciente.nome] = paciente
        print(f"Paciente '{paciente.nome}' adicionado ao registro.")

    @classmethod
    def buscar_paciente(cls, nome):
        paciente = cls.pacientes.get(nome)
        if paciente:
            return paciente
        raise ValueError("Paciente não encontrado.")

    @classmethod
    def listar_pacientes(cls):
        if not cls.pacientes:
            print("Nenhum paciente registrado.")
        for paciente in cls.pacientes.values():
            print(f"Paciente: {paciente.nome}")
