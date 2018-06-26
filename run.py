from datetime import date
from sino import Sino

#################################################################################
# SEGUNDA-FEIRA
_seg = ['07:25', '08:15', '09:05', '09:20', '10:10', '11:00', '11:50', '13:00',
'13:50', '14:40', '14:55', '16:35']
_segp = ['07:25', '09:20', '13:00', '14:55']

# TERÇA-FEIRA
_ter = ['07:25', '08:15', '09:05', '09:20', '10:10', '11:00', '11:50', '13:00',
'13:50', '14:40', '14:55', '15:45', '16:35']
_terp = ['07:25', '09:20', '13:00', '14:55']

# QUARTA-FEIRA
_qua = ['07:25', '08:15', '09:05', '09:20', '10:10', '11:00', '11:50', '13:00',
'13:50', '14:40', '14:55', '16:35']
_quap = ['07:25', '09:20', '13:00', '14:55']

# QUINTA-FEIRA
_qui = _ter
_quip = _terp

# SEXTA-FEIRA
_sex = _ter 
_sexp = _terp
################################################################################

hj = date.today()
dias = ('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
dia = dias[hj.weekday()]
print("Hoje é: | {} | ".format(dia))

#----------------------------
s = Sino()
s.diretorio_usb_linux = '/media/constantino-radio/'
s.tempo_musica = 70
#----------------------------

if dia == 'segunda':
    s.horarios = _seg
    s.horarios_sino_padrao = _segp
elif dia == 'terca':
    s.horarios = _ter
    s.horarios_sino_padrao = _terp
elif dia == 'quarta':
    s.horarios = _qua
    s.horarios_sino_padrao = _quap
elif dia == 'quinta':
    s.horarios = _qui
    s.horarios_sino_padrao = _quip
elif dia == 'sexta':
    s.horarios = _sex
    s.horarios_sino_padrao = _sexp
else: # se nao pegar nenhum dia, roda o sino da terça
    s.horarios = _ter
    s.horarios_sino_padrao = _terp

# executa o agendamento e fica na escuta
s.agendar_sino()


'''
s.horarios = ['07:25', '08:15', '09:05', '09:20', '10:10', '11:00', '11:50', '13:00',
'13:50', '14:40', '14:55', '15:45', '16:35']
s.horarios_sino_padrao = ['09:20', '13:00', '14:55']
'''
