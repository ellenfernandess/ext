# Importa os módulos necessários para o desenvolvimento do sistema
import tkinter as tk  # tkinter é utilizado para criar a interface gráfica do usuário
import sqlite3  # sqlite3 é utilizado para gerenciar o banco de dados local

# Configura o banco de dados para armazenar informações sobre pequenos negócios
def setup_database():
    # Conecta ao banco de dados (ou cria se não existir)
    conn = sqlite3.connect('negocios.db')
    # Cria um cursor para executar comandos SQL
    cursor = conn.cursor()
    
    # Cria uma tabela para armazenar os dados dos negócios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS negocios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            contato TEXT NOT NULL,
            endereco TEXT NOT NULL,
            descricao TEXT
        )
    ''')
    # Confirma a criação da tabela no banco de dados
    conn.commit()
    # Fecha a conexão com o banco de dados
    conn.close()

# Função para adicionar um novo negócio ao banco de dados
def adicionar_negocio(nome, tipo, contato, endereco, descricao):
    conn = sqlite3.connect('negocios.db')
    cursor = conn.cursor()
    
    # Insere os dados do novo negócio na tabela
    cursor.execute('''
        INSERT INTO negocios (nome, tipo, contato, endereco, descricao)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, tipo, contato, endereco, descricao))
    
    conn.commit()
    conn.close()

# Função para exibir todos os negócios cadastrados
def mostrar_negocios():
    conn = sqlite3.connect('negocios.db')
    cursor = conn.cursor()
    
    # Seleciona todos os negócios do banco de dados
    cursor.execute('SELECT * FROM negocios')
    negocios = cursor.fetchall()
    
    conn.close()
    return negocios

# Criação da interface gráfica do sistema usando tkinter
def criar_interface():
    # Cria uma janela principal
    root = tk.Tk()
    root.title("Gerenciador de Pequenos Negócios")
    
    # Labels e campos de entrada para o formulário de cadastro de negócios
    tk.Label(root, text="Nome do Negócio:").grid(row=0, column=0)
    nome_entry = tk.Entry(root)
    nome_entry.grid(row=0, column=1)
    
    tk.Label(root, text="Tipo de Negócio:").grid(row=1, column=0)
    tipo_entry = tk.Entry(root)
    tipo_entry.grid(row=1, column=1)
    
    tk.Label(root, text="Contato:").grid(row=2, column=0)
    contato_entry = tk.Entry(root)
    contato_entry.grid(row=2, column=1)
    
    tk.Label(root, text="Endereço:").grid(row=3, column=0)
    endereco_entry = tk.Entry(root)
    endereco_entry.grid(row=3, column=1)
    
    tk.Label(root, text="Descrição:").grid(row=4, column=0)
    descricao_entry = tk.Entry(root)
    descricao_entry.grid(row=4, column=1)
    
    # Função chamada ao clicar no botão para adicionar um negócio
    def on_adicionar():
        # Recupera os valores inseridos nos campos de entrada
        nome = nome_entry.get()
        tipo = tipo_entry.get()
        contato = contato_entry.get()
        endereco = endereco_entry.get()
        descricao = descricao_entry.get()
        
        # Chama a função para adicionar o negócio ao banco de dados
        adicionar_negocio(nome, tipo, contato, endereco, descricao)
        
        # Limpa os campos de entrada após a inserção
        nome_entry.delete(0, tk.END)
        tipo_entry.delete(0, tk.END)
        contato_entry.delete(0, tk.END)
        endereco_entry.delete(0, tk.END)
        descricao_entry.delete(0, tk.END)
    
    # Botão para adicionar um novo negócio
    tk.Button(root, text="Adicionar Negócio", command=on_adicionar).grid(row=5, column=0, columnspan=2)
    
    # Função chamada ao clicar no botão para exibir os negócios cadastrados
    def on_mostrar():
        # Chama a função para obter os negócios do banco de dados
        negocios = mostrar_negocios()
        # Cria uma nova janela para exibir os negócios
        negocios_window = tk.Toplevel(root)
        negocios_window.title("Negócios Cadastrados")
        
        # Exibe cada negócio na nova janela
        for negocio in negocios:
            tk.Label(negocios_window, text=f"ID: {negocio[0]}").pack()
            tk.Label(negocios_window, text=f"Nome: {negocio[1]}").pack()
            tk.Label(negocios_window, text=f"Tipo: {negocio[2]}").pack()
            tk.Label(negocios_window, text=f"Contato: {negocio[3]}").pack()
            tk.Label(negocios_window, text=f"Endereço: {negocio[4]}").pack()
            tk.Label(negocios_window, text=f"Descrição: {negocio[5]}").pack()
            tk.Label(negocios_window, text="").pack()  # Linha em branco para separação
    
    # Botão para exibir todos os negócios cadastrados
    tk.Button(root, text="Mostrar Negócios", command=on_mostrar).grid(row=6, column=0, columnspan=2)
    
    # Inicia o loop principal da interface gráfica
    root.mainloop()

# Executa a função para configurar o banco de dados na inicialização do programa
setup_database()
# Executa a função para criar a interface gráfica
criar_interface()
