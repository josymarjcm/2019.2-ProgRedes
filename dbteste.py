import psycopg2

def criarBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect('dbname=postgres user=postgres host=localhost password=admin')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    cursor.execute('CREATE DATABASE disciplinas_cursadas')
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=admin')
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE disciplinas (cd_disc VARCHAR(2) PRIMARY KEY, nome VARCHAR(30), notas VARCHAR(2));')
    conexao.commit()
    conexao.close()

def lerBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=admin')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM disciplinas')
    conexao.commit()
    conexao.close

def atualizarBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=admin')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    new_cod = input("Digite o codigo da nova disciplina: ")
    new_nome = input("Digite o nome da nova disciplina: ")
    new_notas = input("Digite a nova nota da disciplina: ")
    cursor.execute('UPDATE disciplinas_cursadas SET cd_disc = {0}, nome = {1}, notas = {2}'.format(new_cod, new_nome, new_notas))
    conexao.commit()
    conexao.close
    
def deletarBanco():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=admin')
    conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conexao.cursor()
    cod_del = input("Digite o codigo da disciplina que você quer deletar: ")
    cursor.execute('DELETE FROM disciplinas WHERE cod_disc = {0}'.format(cod_del))
    conexao.commit()
    conexao.close
    
def inserePessoa(strCPF,strNome,strEmail):
    conexao = psycopg2.connect('dbname=disciplinas_cursadas user=postgres host=localhost password=admin')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO disciplinas (cd_disc, nome, notas) VALUES ({0}, \'{1}\', \'{2}\')'.format(strCPF,strNome,strEmail))
    conexao.commit()
    conexao.close()
