import json
import os
from typing import List, Dict, Optional

class Contato:
    def __init__(self, nome: str, telefone: str, email: str = "", favorito: bool = False):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito
    
    def to_dict(self) -> Dict:
        return {
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'favorito': self.favorito
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        return cls(
            nome=data['nome'],
            telefone=data['telefone'],
            email=data.get('email', ''),
            favorito=data.get('favorito', False)
        )
    
    def __str__(self):
        favorito_str = " ⭐" if self.favorito else ""
        email_str = f" | Email: {self.email}" if self.email else ""
        return f"{self.nome}{favorito_str} | Tel: {self.telefone}{email_str}"

class ListaTelefonica:
    def __init__(self, arquivo: str = "contatos.json"):
        self.arquivo = arquivo
        self.contatos: List[Contato] = []
        self.carregar_contatos()
    
    def carregar_contatos(self):
        """Carrega contatos do arquivo JSON"""
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    self.contatos = [Contato.from_dict(contato) for contato in dados]
            except (json.JSONDecodeError, FileNotFoundError):
                self.contatos = []
    
    def salvar_contatos(self):
        """Salva contatos no arquivo JSON"""
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump([contato.to_dict() for contato in self.contatos], f, 
                     ensure_ascii=False, indent=2)
    
    def adicionar_contato(self, nome: str, telefone: str, email: str = "", favorito: bool = False):
        """Adiciona um novo contato"""
        # Verifica se já existe um contato com o mesmo nome
        if self.buscar_contato_por_nome(nome):
            return False, "Já existe um contato com este nome!"
        
        contato = Contato(nome, telefone, email, favorito)
        self.contatos.append(contato)
        self.salvar_contatos()
        return True, "Contato adicionado com sucesso!"
    
    def buscar_contato_por_nome(self, nome: str) -> Optional[Contato]:
        """Busca um contato pelo nome"""
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None
    
    def listar_contatos(self) -> List[Contato]:
        """Retorna lista de todos os contatos ordenados por nome"""
        return sorted(self.contatos, key=lambda x: x.nome.lower())
    
    def listar_favoritos(self) -> List[Contato]:
        """Retorna lista de contatos favoritos ordenados por nome"""
        favoritos = [contato for contato in self.contatos if contato.favorito]
        return sorted(favoritos, key=lambda x: x.nome.lower())
    
    def editar_contato(self, nome_atual: str, novo_nome: str = None, 
                      novo_telefone: str = None, novo_email: str = None) -> tuple:
        """Edita um contato existente"""
        contato = self.buscar_contato_por_nome(nome_atual)
        if not contato:
            return False, "Contato não encontrado!"
        
        # Verifica se o novo nome já existe (se for diferente do atual)
        if novo_nome and novo_nome.lower() != nome_atual.lower():
            if self.buscar_contato_por_nome(novo_nome):
                return False, "Já existe um contato com este nome!"
        
        # Atualiza os dados
        if novo_nome:
            contato.nome = novo_nome
        if novo_telefone:
            contato.telefone = novo_telefone
        if novo_email is not None:  # Permite string vazia
            contato.email = novo_email
        
        self.salvar_contatos()
        return True, "Contato editado com sucesso!"
    
    def alternar_favorito(self, nome: str) -> tuple:
        """Marca/desmarca um contato como favorito"""
        contato = self.buscar_contato_por_nome(nome)
        if not contato:
            return False, "Contato não encontrado!"
        
        contato.favorito = not contato.favorito
        self.salvar_contatos()
        
        status = "marcado como favorito" if contato.favorito else "desmarcado dos favoritos"
        return True, f"Contato {status}!"
    
    def remover_contato(self, nome: str) -> tuple:
        """Remove um contato"""
        contato = self.buscar_contato_por_nome(nome)
        if not contato:
            return False, "Contato não encontrado!"
        
        self.contatos.remove(contato)
        self.salvar_contatos()
        return True, "Contato removido com sucesso!"

def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("           LISTA TELEFÔNICA")
    print("="*50)
    print("1. Adicionar contato")
    print("2. Visualizar todos os contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar favorito")
    print("5. Ver contatos favoritos")
    print("6. Remover contato")
    print("7. Sair")
    print("="*50)

def adicionar_contato_menu(lista: ListaTelefonica):
    """Menu para adicionar contato"""
    print("\n--- ADICIONAR CONTATO ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome é obrigatório!")
        return
    
    telefone = input("Telefone: ").strip()
    if not telefone:
        print("Telefone é obrigatório!")
        return
    
    email = input("Email (opcional): ").strip()
    
    favorito_str = input("Marcar como favorito? (s/n): ").strip().lower()
    favorito = favorito_str in ['s', 'sim', 'y', 'yes']
    
    sucesso, mensagem = lista.adicionar_contato(nome, telefone, email, favorito)
    print(f"\n{mensagem}")

def visualizar_contatos_menu(lista: ListaTelefonica):
    """Menu para visualizar contatos"""
    contatos = lista.listar_contatos()
    
    if not contatos:
        print("\nNenhum contato cadastrado.")
        return
    
    print(f"\n--- TODOS OS CONTATOS ({len(contatos)}) ---")
    for i, contato in enumerate(contatos, 1):
        print(f"{i}. {contato}")

def editar_contato_menu(lista: ListaTelefonica):
    """Menu para editar contato"""
    if not lista.contatos:
        print("\nNenhum contato cadastrado.")
        return
    
    print("\n--- EDITAR CONTATO ---")
    nome_atual = input("Nome do contato a editar: ").strip()
    
    contato = lista.buscar_contato_por_nome(nome_atual)
    if not contato:
        print("Contato não encontrado!")
        return
    
    print(f"\nContato atual: {contato}")
    print("\nDeixe em branco para manter o valor atual:")
    
    novo_nome = input(f"Novo nome ({contato.nome}): ").strip()
    novo_telefone = input(f"Novo telefone ({contato.telefone}): ").strip()
    novo_email = input(f"Novo email ({contato.email}): ").strip()
    
    # Converte strings vazias para None (manter valor atual)
    novo_nome = novo_nome if novo_nome else None
    novo_telefone = novo_telefone if novo_telefone else None
    novo_email = novo_email if novo_email != contato.email else None
    
    if not any([novo_nome, novo_telefone, novo_email is not None]):
        print("Nenhuma alteração feita.")
        return
    
    sucesso, mensagem = lista.editar_contato(nome_atual, novo_nome, novo_telefone, novo_email)
    print(f"\n{mensagem}")

def marcar_favorito_menu(lista: ListaTelefonica):
    """Menu para marcar/desmarcar favorito"""
    if not lista.contatos:
        print("\nNenhum contato cadastrado.")
        return
    
    print("\n--- MARCAR/DESMARCAR FAVORITO ---")
    nome = input("Nome do contato: ").strip()
    
    sucesso, mensagem = lista.alternar_favorito(nome)
    print(f"\n{mensagem}")

def ver_favoritos_menu(lista: ListaTelefonica):
    """Menu para ver contatos favoritos"""
    favoritos = lista.listar_favoritos()
    
    if not favoritos:
        print("\nNenhum contato marcado como favorito.")
        return
    
    print(f"\n--- CONTATOS FAVORITOS ({len(favoritos)}) ---")
    for i, contato in enumerate(favoritos, 1):
        print(f"{i}. {contato}")

def remover_contato_menu(lista: ListaTelefonica):
    """Menu para remover contato"""
    if not lista.contatos:
        print("\nNenhum contato cadastrado.")
        return
    
    print("\n--- REMOVER CONTATO ---")
    nome = input("Nome do contato a remover: ").strip()
    
    contato = lista.buscar_contato_por_nome(nome)
    if not contato:
        print("Contato não encontrado!")
        return
    
    print(f"\nContato: {contato}")
    confirmacao = input("Confirma a remoção? (s/n): ").strip().lower()
    
    if confirmacao in ['s', 'sim', 'y', 'yes']:
        sucesso, mensagem = lista.remover_contato(nome)
        print(f"\n{mensagem}")
    else:
        print("Remoção cancelada.")

def main():
    """Função principal"""
    lista = ListaTelefonica()
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("\nEscolha uma opção (1-7): ").strip()
            
            if opcao == '1':
                adicionar_contato_menu(lista)
            elif opcao == '2':
                visualizar_contatos_menu(lista)
            elif opcao == '3':
                editar_contato_menu(lista)
            elif opcao == '4':
                marcar_favorito_menu(lista)
            elif opcao == '5':
                ver_favoritos_menu(lista)
            elif opcao == '6':
                remover_contato_menu(lista)
            elif opcao == '7':
                print("\nObrigado por usar a Lista Telefônica!")
                break
            else:
                print("\nOpção inválida! Escolha entre 1 e 7.")
            
            input("\nPressione Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    main()