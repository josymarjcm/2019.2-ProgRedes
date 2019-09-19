import psycopg2

def principal():
   print(existeTabela('pessoas'))
   if (existeTabela('pessoas')):
      print('Banco e tabela encontrados...')
   else:
      print('Criando banco e tabela...')
      criarBanco()
   
   print('')
   print('Inserindo os Dados...')
   inserePessoa('22222222222', 'Beltrano', 'Beltrano@email.com.br')
def existeTabela(strNomeTabela):
   exists = False
   try:
      conexao = psycopg2.connect('dbname=exemplo_aula user=postgres host=localhost password=admin')
      cursor = conexao.cursor()
      cursor.execute('SELECT EXISTS(SELECT relname FROM pg_class WHERE relname=\'{0}\');'.format(strNomeTabela))
      exists = cursor.fetchone()[0]
      cursor.close()
   except psycopg2.Error as e:
      print (e)
   return exists
def criarBanco():
   from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
   conexao = psycopg2.connect('dbname=postgres user=postgres host=localhost password=admin')
   conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
   cursor = conexao.cursor()
   cursor.execute('CREATE DATABASE exemplo_aula')
   conexao = psycopg2.connect('dbname=exemplo_aula user=postgres host=localhost password=admin')
   cursor = conexao.cursor()
   cursor.execute('CREATE TABLE pessoas (cpf VARCHAR(11) PRIMARY KEY, nome VARCHAR(30), email VARCHAR(60));')
   conexao.commit()
   conexao.close()
def inserePessoa(strCPF,strNome,strEmail):
   conexao = psycopg2.connect('dbname=exemplo_aula user=postgres host=localhost password=admin')
   cursor = conexao.cursor()
   cursor.execute('INSERT INTO pessoas (cpf, nome, email) VALUES ({0}, \'{1}\', \'{2}\')'.format(strCPF,strNome,strEmail))
   conexao.commit()
   conexao.close()
def lerDados():
    conexao = psycopg2.connect('dbname=exemplo_aula user=postgres host=localhost password=admin')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM pessoas')
    conexao.commit()
    conexao.close
def delPessoa():
    conexao = psycopg2.connect('dbname=exemplo_aula user=postgres host=localhost password=admin')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM pessoas WHERE *')
