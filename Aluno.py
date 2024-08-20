class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

class Escola:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}, Nota: {aluno.nota}")

escola = Escola()
aluno1 = Aluno("Pedro", "00118111392", 9.0)
aluno2 = Aluno("Barbara", "12345678", 9.5)

escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)
escola.listar_alunos()
