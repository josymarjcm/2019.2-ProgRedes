import psycopg2



def principal():
   print(existeTabela('pessoas'))
   if (existeTabela('pessoas')):
      print('Banco e tabela encontrados...')
      
   else:
      print('Criando banco e tabela...')
      criarBanco()

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
   operacao()

def criarBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect('dbname=postgres user=postgres host=localhost password=1234')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    cursor.execute('CREATE DATABASE disciplinas_cursadas')
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=1234')
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE disciplinas (cd_disc VARCHAR(2) PRIMARY KEY, nome VARCHAR(30), notas VARCHAR(2));')
    conexao.commit()
    conexao.close()
    operacao()

def lerBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=1234')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM disciplinas')
    conexao.commit()
    conexao.close
    operacao()

def atualizarBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=1234')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    new_cod = input("Digite o codigo da nova disciplina: ")
    new_nome = input("Digite o nome da nova disciplina: ")
    new_notas = input("Digite a nova nota da disciplina: ")
    cursor.execute('UPDATE disciplinas_cursadas SET cd_disc = {0}, nome = {1}, notas = {2}'.format(new_cod, new_nome, new_notas))
    conexao.commit()
    conexao.close
    operacao()
    
def deletarBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=1234')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    cod_del = input("Digite o codigo da disciplina que você quer deletar: ")
    cursor.execute('DELETE FROM disciplinas WHERE cod_disc = {0}'.format(cod_del))
    conexao.commit()
    conexao.close
    operacao()

def inserePessoa():
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=1234')
    cursor = conexao.cursor()
    new_cod = input("Digite o codigo da nova disciplina: ")
    new_nome = input("Digite o nome da nova disciplina: ")
    new_notas = input("Digite a nova nota da disciplina: ")
    cursor.execute('INSERT INTO disciplinas (cd_disc, nome, notas) VALUES ({0}, \'{1}\', \'{2}\')'.format(new_cod,new_nome,new_notas))
    conexao.commit()
    conexao.close()
    operacao()

def operacao():
    verif = input("Digite a operação do banco(C, R, U, D ou I): ")
    if verif.lower()=="c":
        criarBanco()
    if verif.lower()=="r":
        lerBanco()
    if verif.lower()=="u":
        atualizarBanco()
    if verif.lower()=="d":
        deletarBanco()
    if verif.lower()=="i":
        inserePessoa()


operacao()