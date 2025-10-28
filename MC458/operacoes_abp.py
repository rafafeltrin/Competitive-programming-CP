class no:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
class arvore_binaria:
    def __init__(self, raiz):
        self.raiz = no(raiz)
    
    def percorrer_pre(self, no_atual, resultado):
        if no_atual != None:
            resultado.append(no_atual.valor)
            self.percorrer_pre(no_atual.esquerda, resultado)
            self.percorrer_pre(no_atual.direita, resultado)

    def percorrer_in(self, no_atual, resultado):
        if no_atual != None:
            self.percorrer_in(no_atual.esquerda, resultado)
            resultado.append(no_atual.valor)
            self.percorrer_in(no_atual.direita, resultado)

    def percorrer_pos(self, no_atual, resultado):
        if no_atual != None:
            self.percorrer_pos(no_atual.esquerda, resultado)
            self.percorrer_pos(no_atual.direita, resultado)
            resultado.append(no_atual.valor)

    def inserir_valor(self, valor, no_atual):
        if valor <= no_atual.valor:
            if no_atual.esquerda == None:
                no_atual.esquerda = no(valor)
            else:
                self.inserir_valor(valor, no_atual.esquerda)
        elif valor > no_atual.valor:
            if no_atual.direita == None:
                no_atual.direita = no(valor)
            else:
                self.inserir_valor(valor, no_atual.direita)

    def pesquisar_valor(self, valor, no_atual) -> bool:
        if no_atual == None:
            return False
        if no_atual.valor == valor:
            return True
        elif valor < no_atual.valor:
            return self.pesquisar_valor(valor, no_atual.esquerda)
        else:
            return self.pesquisar_valor(valor, no_atual.direita)
    
    def remover_valor(self, valor, no_atual):
        if no_atual != None:
            if no_atual.valor == valor:
                if no_atual.esquerda and no_atual.direita:
                    substituto = self.busca_max(no_atual.esquerda)
                    no_atual.valor = substituto.valor
                    no_atual.esquerda = self.remover_valor(substituto.valor, no_atual.esquerda)
                    return no_atual
                elif no_atual.direita:
                    return no_atual.direita
                elif no_atual.esquerda:
                    return no_atual.esquerda
                else:
                    return None
            elif valor < no_atual.valor:
                no_atual.esquerda = self.remover_valor(valor, no_atual.esquerda)
            else:
                no_atual.direita = self.remover_valor(valor, no_atual.direita)
        return no_atual
    
    def busca_max(self, no_atual):
        if no_atual.direita:
            return self.busca_max(no_atual.direita)
        else:
            return no_atual

if __name__ == "__main__":
    arvore = None
    while True:
        try:
            comando = input()
            #print("aaa"+comando)
        except EOFError:
            break

        if comando == "INFIXA":
            lista_in = []
            arvore.percorrer_in(arvore.raiz, lista_in)
            print(*lista_in)
        elif comando == "PREFIXA":
            lista_pre = []
            arvore.percorrer_pre(arvore.raiz, lista_pre)
            print(*lista_pre)
        elif comando == "POSFIXA":
            lista_pos = []
            arvore.percorrer_pos(arvore.raiz, lista_pos)
            print(*lista_pos)
        elif comando[0] == "I":
            valor = int(comando[2:])
            if arvore == None or arvore.raiz == None:
                arvore = arvore_binaria(valor)
            else:
                arvore.inserir_valor(valor, arvore.raiz)
        elif comando[0] == "P":
            valor = int(comando[2:])
            encontrado = arvore.pesquisar_valor(valor, arvore.raiz)
            if encontrado:
                print(f"{valor} existe")
            else:
                print(f"{valor} nao existe")
        elif comando[0] == "R":
            valor = int(comando[2:])
            arvore.raiz = arvore.remover_valor(valor, arvore.raiz)