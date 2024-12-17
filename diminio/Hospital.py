from modelo.edl import VetorTADS, Ala

class AlaCheiaException(Exception):
    def __init__(self, message):
        super().__init__(message)

class LeitoOcupadoException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Hospital(VetorTADS):
    instancia = None

    def __init__(self, descricao: str, quantidade_de_elementos: int):
        super().__init__(Ala, quantidade_de_elementos)
        self.descricao = descricao

    @staticmethod
    def get_instancia():
        return Hospital.instancia

    @staticmethod
    def configurar_hospital_para_sessao(descricao: str, quantidade_de_elementos: int):
        if Hospital.instancia is None:
            Hospital.instancia = Hospital(descricao, quantidade_de_elementos)
        return Hospital.instancia

    def __str__(self):
        alas = self.array()
        sb = ["Alas Registradas para o Hospital: \n"]
        
        for i, ala in enumerate(alas):
            texto = ala.get_descricao() if ala is not None else "Sem Definição"
            sb.append(f"[ {i} ] - {texto}\n")
        
        sb.append("\n")
        return ''.join(sb)