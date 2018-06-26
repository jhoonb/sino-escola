#
# Python 3 - Jhonathan Paulo Banczek 
# Escola Padre Constantino de Monte - Escola da Autoria
# Junho de 2018
#

import sys
import schedule
import random
import pygame
import time
from pathlib import Path
import threading


class Sino:

    def __init__(self):
        self._lista_musicas = []
        self._tempo_musica = 70
        self._diretorio_usb_linux = "/media/constantino-radio/"
        self._musica = '/home/constantino-radio/sino/sino_padrao.mp3'
        self._horarios = []
        self._sched = schedule.Scheduler()
        self._horarios_sino_padrao = []

    
    def _is_mp3(self, x):
        """
        is_mp3: retorna True se o tipo de arquivo lido é mp3,
        False caso contrário
        params: x, type: pathlib.Path
        return: boolean
        """
        if x.is_file() and str(x).split('.')[-1] == 'mp3':
            return True
        return False


    @property
    def diretorio_usb_linux(self):
        return self._diretorio_usb_linux


    @diretorio_usb_linux.setter
    def diretorio_usb_linux(self, diretorio_usb_linux):
        self._diretorio_usb_linux = diretorio_usb_linux

    
    @property
    def tempo_musica(self):
        return self._tempo_musica


    @tempo_musica.setter
    def tempo_musica(self, tempo_musica):
        self._tempo_musica = tempo_musica


    @property
    def horarios_sino_padrao(self):
        return self._horarios_sino_padrao


    @horarios_sino_padrao.setter
    def horarios_sino_padrao(self, horarios_sino_padrao):
        self._horarios_sino_padrao = horarios_sino_padrao


    @property
    def horarios(self):
        return self._horarios

    
    @horarios.setter
    def horarios(self, horarios):
        self._horarios = horarios


    def _unidades_por_plataforma(self):
        if sys.platform == 'linux':
            #p = Path('/media/constantino-radio/')
            print('unidades_por_plataforma: ', self._diretorio_usb_linux)
            p = Path(self._diretorio_usb_linux)
            return [str(i) for i in p.iterdir() if i.is_dir()] if p.exists() else []
        return ['D:/musicas/', 'E:/musicas/', 'F:/musicas/', 'G:/musicas/'] 


    def _buscar_musicas(self):

        for un in self._unidades_por_plataforma():
            # procura a pasta de musica nas provaveis unidades de pendrive
            print(' \t > diretorio: {}'.format(un))    
            p = Path(un+'/musicas/') # [UPDATE] atualizado aqui pra procurar o diretorio /musicas/ dentros dos pendrives
            try:
                lista_musicas = [str(i) for i in p.iterdir() if p.is_dir() and self._is_mp3(i)] if p.exists() else []
            except:
                print("    >> nenhuma unidade preparada ... ")
                continue
            # se achar musicas, encerra a busca. [break]
            # print('->', lista_musicas)
            if lista_musicas:
                print('musicas achadas...')
                #return lista_musicas
                self._lista_musicas = lista_musicas
                return True
            # se não encontrou as musicas nas pastas, executa o SINO PADRAO
        print('não encontrou as musicas nas pastas, o SINO PADRÃO será selecionado')
        #return ['sino_padrao.mp3']
        self._lista_musicas = []
        return False

    
    def _selecionar_musica_aleatoria(self):
        """
        captura_musica_aleatoria: retorna uma música aleatoriamente da listade musicas
        params: lista_musicas(list)
        return: str
        """
        return random.choice(self._lista_musicas)


    def _tocar_musica(self, h):
        """
        tocar_musica: executa a música selecionada num tempo determinado com fadeout
        params: musica(str), tempo(int)
        """

        musica = ''

        #horario dos sinos padrão
        print("-> Horário: ", h)

        # buscar musicas no diretorio / selecionar musica via random
        if not self._buscar_musicas():
            musica = '/home/constantino-radio/sino/sino_padrao.mp3'
        else:
            musica = self._selecionar_musica_aleatoria()

        #print("lista de musicas: ", self._lista_musicas)
        print("||||||  musica: {} |||||| ".format(musica))

        if h in self._horarios_sino_padrao:
            print('** Horario do sino PADRÃO!! **')
            musica = '/home/constantino-radio/sino/sino_padrao.mp3'

        print('play')
        #pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play()
        tempo = int(self._tempo_musica) * 1000 # millisegundos
        pygame.mixer.music.fadeout(tempo)
        print('-#############- SINO TOCANDO - #############-')
        time.sleep(self.tempo_musica + 1)
        #pygame.mixer.music.stop()


    def agendar_sino(self):

        if not self.horarios:
            print(" ->> nenhum horário configurado <<- ")
            return

        print("tempo_musica_: ", self._tempo_musica)

        for h in self._horarios:

            self._sched.every().day.at(h).do(self._tocar_musica, h)

        # Start a thread to run the events
        #t = threading.Thread(target=schedule.run)
        #t.start()
        
        while True:
            print(' -> procurando horario...')
            self._sched.run_pending()
            time.sleep(5)
        print('saiu')

