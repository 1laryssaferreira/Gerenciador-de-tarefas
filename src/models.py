class Task:

    def __init__(self, titulo, descricao, prioridade):

        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade

        self.status = "To Do"

    def iniciar(self):

        self.status = "In Progress"

    def concluir(self):

        self.status = "Done"