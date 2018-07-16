#====================================================================
# Configuração de linguagens B"H
#====================================================================

from gluon.storage import Storage
from datetime import date, datetime, time
configs = Storage()
import locale
import platform
import sys

os_plataform = platform.system()
configs.langs = {
                    'br' : {'lang':'pt-br', 'initial':'PT','name':T('Portuguese')},
                    'es' : {'lang':'es', 'initial':'ES','name':T('Español')},
                    'us' : {'lang':'default', 'initial':'EN','name':T('English')},
                    }
if os_plataform == "Windows":
    configs.langs['il'] = {'lang':'he', 'initial':'HE', 'name':T('Hebrew')}
    configs.langs['il']['locale'] = 'hebrew_israel.1252'
    configs.langs['br']['locale'] = 'portuguese_brazil.1252'
    configs.langs['es']['locale'] = 'español_España.1252'
    configs.langs['us']['locale'] = 'English_United States.1252'
                    
elif os_plataform == "Linux":
    #configs.langs['il']['locale'] = 'he_IL.utf8'
    configs.langs['br']['locale'] = 'pt_BR.UTF-8'
    configs.langs['es']['locale'] = 'es_CU.UTF-8'
    configs.langs['us']['locale'] = 'en_US.UTF-8'



if request.vars._language: session._language=request.vars._language
if session._language: 
    T.force(configs.langs[session._language]['lang'] )
    locale.setlocale(locale.LC_ALL, configs.langs[session._language]['locale'])
else: 
    T.force('default')
    session._language='us'
    locale.setlocale(locale.LC_ALL,configs.langs['us']['locale'])
   
