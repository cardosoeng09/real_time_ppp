INSTITUTO MILITAR DE ENGENHARIA - IME
RIO DE JANEIRO - RJ - BRASIL

SEÇÃO DE ENGENHARIA CARTOGRÁFICA - SE/6

PROJETO FINAL DE CURSO 2019
POSICIONAMENTO PRECISO POR GNSS EM TEMPO REAL

ALUNOS: 
RAFAEL LARA CARDOSO - Cap
LUANA MARQUES MELLO PEREIRA - 1º Ten

ORIENTADORES:
HAROLDO ANTONIO MARQUES - PROF. D.Sc
HELOÍSA ALVES SILVA MARQUES - PROFa. D.Sc


BEM VINDO USUÁRIO, ANTES DE PROSSEGUIR, LEIA ESTE MANUAL DE USO!

Este Projeto Final de Curso visa, além de ser um trabalho de engenharia para conferir a conclusão do curso dos referidos alunos, busca interagir com os usuários de forma a todos terem acesso ao material criado e utilizado. A disponibilização de todo material está sendo feita de forma gratuita, com as devidas referências, proporcionando assim uma ferramenta de ajuda aos interessados no tema para aprofundamento e análise de dados GNSS em pesquisas futuras.

Para melhor entendimento dos procedimentos realizados é necessária a leitura do arquivo main.pdf (gerado a partir do main.tex via compilador Latex). Nesse arquivo se encontram todas as informações do presente projeto.

1) Disponibilização do material online: 

http://github.com/cardosoeng09/real_time_ppp

2) Conteúdo:

2.1) Arquivo README.md com instruções iniciais;

2.2) Desktop/PPP_tempo_real :

    2.2.1) Pasta Data:
            * Graphics: gráficos de análise gerados no trabalho;
                - Pasta com todos os gráficos gerados no trabalho.
            * Logs : arquivos logs obtidos;
                Os logs estão divididos em pastas referentes a cada levantamento/coleta de dados. 
                - "POAL20636" - RTPPP na estação POAL - Sem especificacoes de antena
                - "POAL20650" - RTPPP na estação POAL - Com especificacoes de antena
                - "RJ_T20712" - RTPPP no terraco da secao de Eng. Car. do IME no dia 17/09 - Conexao do notebook (BNC) com cabo serial
                - "POAL20716" - RTPPP na estação POAL em 21/09/2019 - simultaneamente com a coleta do PPP-WIZARD
                - 'POAL001_ppp_wizard' - PPP-RTK feita em 21/09 - simultanamente com a coleta do BNC (RTPPP)
                "RJ_T20721" - RTPPP feita em 23/09 na praça Gen Tiburcio com BNC
            * Códigos aplicados para manipulação dos dados e geração de gráficos - Comentário mais detalhados se encontram nos próprios códigos.
                - main.py - executa as linhas principais de código que geram todos os gráficos de uma só vez;
                - graphics.py - possui todas as funções necessárias para construir os gráficos;
                - auxiliary_functions.py - possui todas as funções auxiliares necessárias para manipulação dos arquivos de log.
    2.2.2) Pasta pfc_pdf_files: arquivos do trabalho na plataforma           Tais arquivos geram o .pdf que possui todas as especificações do projeto - é necessário compilar o arquivo main.tex utilizando alguma plataforma Latex - recomenda-se o uso da ferramenta "Overleaf".
            * caps -  Pasta com os Capítulos;
            * extra - Pasta com arquivos extras necessários para configuração e "pré-texto";
            * img - Pasta com as imagens - com exceção dos gráficos;
            * main.tex : arquivo principal do projeto;
            * Importação de bibliotecas;
            * Referências.