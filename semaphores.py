import time
import datetime
from threading import Timer

#
# Este programa simula dois sinais de trânsito em um cruzamento
#
class Semaforo(object):

    direcao = None
    current_state = None

    def __init__(self,direcao,current_state):
       self.direcao = direcao
       self.current_state = current_state

    def iniciar_trafego(self):
       while True:
          if self.current_state == 'Verde':
              self.sinal_verde_amarelo()
          elif self.current_state == 'Vermelho':
              self.sinal_vermelho()


    def sinal_verde_amarelo(self):
        print('Direção: ', self.direcao, ' - Sinal Verde em ' , datetime.datetime.now().time() )
        time.sleep(2)
        print('Direção: ', self.direcao, ' - Sinal Amarelo em ', datetime.datetime.now().time())
        time.sleep(3)
        self.current_state = 'Vermelho'

    def sinal_vermelho(self):
        print('Direção: ', self.direcao ,' - Sinal Vermelho em ', datetime.datetime.now().time())
        time.sleep(5)
        self.current_state = 'Verde'


Semaforo_A = Semaforo('Presidente Vargas' , 'Verde')
Semaforo_B = Semaforo('Rio Branco' , 'Vermelho' )

Presidente_Vargas = Timer(0.0, Semaforo_A.iniciar_trafego)
Rio_Branco  = Timer(0.0, Semaforo_B.iniciar_trafego)

Presidente_Vargas.start()
Rio_Branco.start()