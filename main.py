import os

listaTarefas = []

class Tarefa:
    def __init__(self, titulo, descricao, status, data):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data = data
    def __call__(self, *args, **kwds):
        
        return [self.titulo, self.descricao, self.status, self.data]
    #função para adicionar um novo item à lista
    def adicionar_item(self):
        
        listaAtt = [self.titulo, self.descricao, self.status, self.data]
        listaTarefas.append(listaAtt)
        
        return listaTarefas
    #função para excluir um item da lista


    def excluir_item(self, titulo):
        try:
            
            for listas in listaTarefas:
                listaTarefas.pop(listas.index(titulo))
            
            return listaTarefas
        except ValueError: #o value error é para se a pessoa tentar excluir uma tarefa que não existe na lista dela
            print('Este item não pode ser excluído, pois ele não existe')
instanciaTarefa = Tarefa(None, None, None, None)   
while True: #dentro do loop vai perguntar oq o usuário quer fazer e chamar as devidas funções. Caso o usuário queira parar, usa o S para quebrar o laço e conseguir salvar o json no bloco abaixo
    ComandoInicial = input('\nSelecione um comando:\n[L]istar [A]dicionar [E]xcluir [S]air \n\n').upper()
    if ComandoInicial.startswith('S'):
        break
    elif ComandoInicial.startswith('L'):
        for lista in listaTarefas:
            print(f'Título: {lista[0]} | Descrição: {lista[1]} | Status: {lista[2]} | Data: {lista[3]}')
    elif ComandoInicial.startswith('A'):
        titulo = input('Digite o título do item que será adicionado:\n')
        
        descricao = input('Digite a descrição do item que será adicionado:\n')
        
        status = input('Digite o status do item que será adicionado:\n')
    
        data = input('Digite a data em que está adicionando o item:\n')
        
        
        instanciaTarefa = Tarefa(titulo, descricao, status, data)
        listaTarefas.append(instanciaTarefa())

    elif ComandoInicial.startswith('E'):
        
        tarefaASerExcluida = input('Digite o título do item que você deseja excluir:\n')
        for listas in listaTarefas:
            if listas[0] == tarefaASerExcluida:
                instanciaTarefa.excluir_item(tarefaASerExcluida)
        print(f'\nAqui está a lista atualizada:\n{listaTarefas}')

    elif ComandoInicial == 'CLEAR':
        os.system('cls') #Vai depender do sistema operacional. no W10 é cls, no W11 é clear e no mac/linux é clear também, aí tem que alterar
    else:
        print('Digite um comando válido')

#Abre o arquivo json, salva todas as alterações feitas na dictJson, dentro do arquivo json em si, e depois fecha dnv o arquivo
