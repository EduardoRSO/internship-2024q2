### Portuguese Version

# Desafio Técnico - Estágio 2022Q2

Obrigado por se candidatar a uma posição na Giant Steps Capital. Gostaríamos de propor um desafio técnico para lhe dar a oportunidade de demonstrar sua experiência e habilidades com desenvolvimento de software.

## O Desafio

Durante o processo de recrutamento anterior, os candidatos foram solicitados a resolver um problema específico detalhado aqui: (https://github.com/giant-steps/internship-2022q2). Infelizmente, um candidato chamado 'Bot' não teve um bom desempenho no teste. Você pode ajudar a corrigir os problemas?

## Suas tarefas são as seguintes:

* Identificar e corrigir o bug que está impedindo o código de produzir a resposta correta.
* Melhorar o código para torná-lo mais robusto e fácil de manter. Considere como você pode estruturar o código para facilitar a adição de novas funcionalidades.
* Implementar testes unitários para garantir a correção do código. Talvez se 'Bot' tivesse escrito alguns testes unitários, o bug poderia ter sido evitado.

## A Pergunta

No processo anterior, havia a seguinte pergunta a ser respondida:

* Qual foi o período mais lucrativo de 500 dias corridos desde 2010-01-01 até 2021-03-01? Ou seja, se você tivesse que investir `657,43` de capital por 500 dias, qual teria sido o período mais lucrativo desde o início de 2000 até o início de março/2021? Sua resposta deve ser as datas de início e fim do período que você encontrou.

A resposta esperada para a pergunta do desafio anterior é:
2015-06-16, com um valor ganho de 787.952750655493 de 2015-06-16 a 2016-10-28.

## Entregável

Entregue sua solução escrita em Python (versão 3.10) em um repositório **privado** do GitHub, dando acesso apenas ao nosso avaliador quando solicitado. O repositório deve conter os seguintes itens:
* Uma solução de código que possa fornecer uma saída conforme especificado.
* Um arquivo README, em inglês, com:
    * Instruções detalhadas de execução da solução de maneira clara e concisa;
    * A resposta para a [pergunta](https://github.com/giant-steps/internship-2022q2/#the-question).

## Perguntas Frequentes (FAQ)

**Existem frameworks, sistemas de banco de dados ou ferramentas específicas que devo usar para este desafio?**
- Não, use o que você se sentir mais confortável e que melhor demonstre suas habilidades de engenharia de software e codificação. O único requisito técnico para este desafio é que você deve usar Python no processo de desenvolvimento.

**A saída do meu programa deve estar em um formato específico ou usar uma estrutura de dados particular?**
- Não, desde que possamos validar a saída da sua solução, você pode definir como irá entregá-la.

## Minha Solução

Acabei não corrigindo o erro, mas acredito que seja porque o método rolling do pandas é aplicado a índices anteriores e não aos posteriores, como é feito em `calc_sum`. Inclusive tentei usar o método de `shift`, reordenar os índices em ordem decrescente e até mesmo o `expanding`, mas continuei obtendo respostas inválidas. Também observei que o DataFrame gerado pelo arquivo `solution.py` ignora alguns dados anteriores a 2010-01-11 e não entendi o motivo.

Optei por construir o código de tal modo que ele fosse adaptativo de acordo com as variáveis de ambiente passadas em `config.json` para simular a manipulação de um lambda no AWS Management HUB.

Utilizei a programação orientada a objetos e os princípios SOLID para abstrair o problema em dois componentes: uma classe responsável por obter o DataFrame e formatá-lo da forma necessária e outra classe que recebe esse DataFrame formatado e faz os cálculos. Dessa forma, foi possível construir dicionários do tipo `<str, classe>` para definir qual o Handler da taxa a ser utilizado, assim como `<str, função>` para a configuração dos atributos a partir dos valores lidos nas variáveis de ambiente.

Também utilizei a biblioteca de logging para se aproximar do que utilizo para depurar os lambdas via CloudWatch. De maneira empírica, descobri que é muito mais fácil identificar possíveis erros quando se faz uso de mensagens de log no início e fim de cada método, indicando os parâmetros recebidos e qual o valor ou o shape do DataFrame gerado.

Os testes de unidade foram bem sucintos e garantiam apenas a uniformidade da tipagem dos parâmetros, assim como a integridade dos DataFrames. Uma possível melhoria seria utilizar a biblioteca `unittest` do Python para criar testes específicos para as funções de cálculo, com exemplos extremos.

Uma possível adição em um exemplo real seria a implementação do `DatabaseHandler`. Nesse caso, optei por omitir essa classe, pois só é necessário salvar um único `.csv`.

---

### English Version

# Technical Challenge - Internship 2022Q2

Thank you for applying for a position at Giant Steps Capital. We would like to propose a technical challenge to give you the opportunity to demonstrate your experience and skills with software development.

## The Challenge

During the previous recruiting process, candidates were asked to solve a specific problem detailed here: (https://github.com/giant-steps/internship-2022q2). Unfortunately, a candidate named 'Bot' did not perform well on the test. Can you help rectify the issues?

## Your Tasks Are as Follows:

* Identify and fix the bug that is preventing the code from producing the correct answer.
* Enhance the code to make it more robust and easier to maintain. Consider how you can structure the code to facilitate the addition of new features.
* Implement unit tests to ensure the correctness of the code. Perhaps if 'Bot' had written some unit tests, the bug might have been prevented from occurring in the first place.

## The Question

In the previous process, there was the following question to be answered:

* What was the most profitable period of 500 calendar days since 2010-01-01 until 2021-03-01? That is, if you had to invest `657.43` of capital for 500 days, what would have been the most profitable period from the beginning of 2000 until the beginning of March/2021? Your answer should be the start and end dates of the period you found.

The expected answer for the previous challenge question is:
2015-06-16, with an amount earned of 787.952750655493 from 2015-06-16 to 2016-10-28.

## Deliverable

Deliver your solution written in Python (version 3.10) to a **private** GitHub repository, giving access only to our evaluator when requested. The repository should contain the following items:
* A code solution that can deliver an output as specified.
* A README file, in English, with:
    * Detailed execution instructions of the solution in a clear and concise fashion;
    * The answer to the [question](https://github.com/giant-steps/internship-2022q2/#the-question).

## Frequently Asked Questions (FAQ)

**Are there any particular frameworks, database systems, or tools I should use for this challenge?**
- No, use whatever you feel most comfortable with and that will best demonstrate your software engineering and coding skills. The only technical requirement for this challenge is that you must use Python in the development process.

**Should the output of my program be in a specific format or use a particular data structure?**
- No, as long as we are able to validate the output of your solution, you can define how you will deliver it.

## My Solution

I did not manage to fix the error, but I believe it's because the rolling method of pandas is applied to previous indices and not to subsequent ones, as done in `calc_sum`. I even tried using the shift method, reordering the indices in descending order, and even expanding, but I kept getting invalid answers. I also noticed that the DataFrame generated by the `solution.py` file ignores some data before 2010-01-11, and I didn't understand why.

I chose to build the code in such a way that it would be adaptive according to the environment variables passed in `config.json` to simulate the manipulation of a lambda in the AWS Management HUB.

I used object-oriented programming and SOLID principles to abstract the problem into two components: one class responsible for obtaining the DataFrame and formatting it as needed and another class that receives this formatted DataFrame and performs the calculations. This way, it was possible to build dictionaries of the type `<str, class>` to define which rate Handler to use, as well as `<str, function>` for configuring the attributes from the values read in the environment variables.

I also used the logging library to approximate what I use to debug lambdas via CloudWatch. Empirically, I found that it is much easier to identify possible errors when using log messages at the beginning and end of each method, indicating the received parameters and what the value or shape of the generated DataFrame is.

The unit tests were quite succinct and only ensured the uniformity of parameter typing, as well as the integrity of the DataFrames. A possible improvement would be to use Python's `unittest` library to create specific tests for the calculation functions, with extreme examples.

A possible addition in a real example would be the implementation of the `DatabaseHandler`. In this case, I chose to omit this class, because it is only necessary to save a single `.csv`.
