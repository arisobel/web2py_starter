# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
'''
response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

'''


from collections import defaultdict
#carrega grupos pertencentes a esse user - funcao lista_grupos() em 0.py
list_groups = list_groups()
#list_mns_sys = list_menus_system(session._sys)
list_mns_sys = list_menus_system(1)

#print "imprime sistema => ", session._sys, "list_mns_sys => ", list_mns_sys


#response.flash = lista_grupos
#carrega o menu master numa vari[avel, pra nao precisar ficar acessando o BD toda hora
master = db().select(db.t_menu_master.ALL,orderby=db.t_menu_master.f_ordem_master)

#print "sql menu_master \n\n\n",db._lastsql


#carrega to tabea do menu mua variável, contendo todos os dados para montagem do menu
detalhes = db((db.t_menu.f_system==configuration.get('app.system')) | (db.t_menu.f_system==None)).select(db.t_menu.ALL)


session._detalhes = BEAUTIFY(detalhes) 
session._list_groups = BEAUTIFY(list_groups)  
session._list_mns_sys = BEAUTIFY(list_mns_sys)   
#flitra os itens de menu fazendo join com a tabela t_menu_grupo - e flitrando com as que pertencem aos
#gurpos do usuário logado = lista_grupos
menu_detalhe = db(db.t_menu_grupo.f_grupo.belongs(list_groups) & (db.t_menu.id.belongs(list_mns_sys))).select(db.t_menu.f_menu_master,
   db.t_menu.id,
        join=db.t_menu_grupo.on(db.t_menu_grupo.f_menu==db.t_menu.id),
        groupby=db.t_menu.id,
        orderby=db.t_menu.f_men_ordem

                                                       )

session._menux = BEAUTIFY(menu_detalhe)  
                                                                  
#atribui a variável Menu à um defaultlist - que é um dict que possuiu listas incrementáveis -
#formando o Menu Master e Details
menu = defaultdict(list)
menu_new = dict()

#itera sobre os tens de menu flitrados já pelos grupos do usuário detro da variável Menu
for row in menu_detalhe:
    if int(row.id) not in menu[row.f_menu_master]:
        menu[row.f_menu_master].append(int(row.id))
 
    
        
for row in menu_detalhe:
    if int(row.id) not in menu[row.f_menu_master]:
        menu[row.f_menu_master].append(int(row.id))
        

#monta o menu propriamente dito em ciam da variavel que já possui a estrutura do master detail
#onde o m é o Id do Master e l a lista dos detalhes

response.menu = []
for m, l in iter(menu.items()):
    master = db.t_menu_master[m]
    item_master = {'nome_master':master['f_menu_master'], 'iconemaster': master['f_icon']}
    internal_list=[]
    for x in l:
        menu_det = db.t_menu[x]
        item = {'nome':menu_det['f_menu_detalhe'],'url': URL(db.t_menu[x]['f_menu_controller'],menu_det['f_menu_funcao']), 'icon':menu_det['f_icon']}
        internal_list.append(item)
    response.menu.append([item_master,internal_list])

