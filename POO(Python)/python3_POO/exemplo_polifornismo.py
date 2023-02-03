class Relatorio:
    def gera_relatorio(self):
        print('Relatorio geral')

class RelatorioUsuarios(Relatorio):
    def gera_relatorio(self):
        print('Relatorio dos usuarios')

class RelatorioCustos(Relatorio):
    def gera_relatorio(self):
        print('Relatorio de custos')

relatorio1 = RelatorioUsuarios()
relatorio2 = RelatorioCustos()
relatorio3 = RelatorioUsuarios()
relatorio4 = RelatorioUsuarios()

relatorios = [relatorio1, relatorio2, relatorio3, relatorio4]
for rel in relatorios:  
    rel.gera_relatorio()