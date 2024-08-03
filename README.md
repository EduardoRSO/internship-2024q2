Acabei não corrigindo o erro, mas acredito que seja porque o método rolling do pandas é aplicado a índice anteriores e não aos posteriores, como é feito em calc_sum. Inclusive tentei usar o método de shift, reordenar os índice em ordem descrecente e até mesmo o expand, mas continuei obtendo respostas inválidas... Támbém observei que o dataframe gerado pelo arquivo solution.py ignora alguns dados anteriores à 2010-1-11 e não entendi o motivo.

Optei por construir o código de tal modo que ele fosse adaptativo de acordo com as variáveis de ambiente passadas em config.json para simular a manipulação de um lambda no AWS Management HUB.

Utilizei a programação orientada a objetos e os princípios SOLID para abstrair o problema em duas componentes: Uma classe responsável por obter o dataframe e formatá-lo da forma necessária e uma outra classe que recebe esse dataframe formatado e faz os cálculos. Desse modo foi possível construir dicionários do tipo <str, classe> para definir qual o Handler da taxa a ser utilizado. Assim como <str, função> para a configuração dos atributos a partir dos valores lidos nas variáveis de ambiente.

Também utilizei a biblioteca de logging para se aproximar do que eu utilizo para debuggar os lambdas via cloudwatch. De maneira empírica, descobri que é muito mais fácil identificar possíveis erros quando se é feito o uso de mensagens d elog no ínicio e fim de cada método, indicando os parametros recebidos e qual o valor ou o shape do dataframe gerado.

Os testes de unidade foram bem sucintos e garantiam apenas a uniformidade da tipagem dos parametros, assim como a integridade dos dataframes. Uma possível melhoria seria utilizar a bliblioteca unittest do python para criar testes específicos para as funções de cálculo, com exemplos extremos.

Uma possível adição em um exemplo real seria a implementação do DatabaseHandler. Nesse caso optei por omitir essa clase, porque só é necessário salvar um único .csv

