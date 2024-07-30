from solution.solution import SelicCalc
from solution.calculator_handler import CalculatorHandler
from datetime import datetime
import json

if __name__ == '__main__':
    environment_variables = json.load(open('config.json','r'))
    c = CalculatorHandler()
    #calc = SelicCalc()

    #calc.calc_amount_earned(
    #    start_date=date(2010, 1, 1),
    #    end_date=date(2021, 3, 1),
    #    capital=657.43,
    #    frequency="daily",
    #    save_csv=False,
    #)


# fazer a leitura do json 
# minha ideia eh fzr com que ele receba um dicionario com parametros e use a estrategia de dicionarios de funcoes para setar os atributos
# ja tem isso pronto no sgs_handler, então tudo certo
# percebi que o sgs handler deveria ser responsável por setar essas variaveis, dado que recebeu um dicionario
# depois desse ajuste, salvar o dataframe do intervalo total e fazer testes
# provavelmente deve ter algum erro, os valores estão bem altos.
# cogitei fazer um database_handler só de brincadeira que iria salvar o .csv. 