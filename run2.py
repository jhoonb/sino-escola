from sino import Sino

#----------------------------
s = Sino()
s.diretorio_usb_linux = '/media/constantino-radio/'
s.tempo_musica = 40
#----------------------------

s.horarios = ['13:59', '14:00', '14:01','14:02','14:03', '14:04', '14:08','14:09', '14:10', '14:11']
s.horarios_sino_padrao = ['13:17', '14:10']

# executa o agendamento e fica na escuta
s.agendar_sino()


'''
s.horarios = ['07:25', '08:15', '09:05', '09:20', '10:10', '11:00', '11:50', '13:00',
'13:50', '14:40', '14:55', '15:45', '16:35']
s.horarios_sino_padrao = ['09:20', '13:00', '14:55']
'''
