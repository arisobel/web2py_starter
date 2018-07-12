#menus tables
########################################

#=====================================================================================
# menu Master
#=====================================================================================
#tabela do Master do menu

db.define_table('t_menu_master',
        Field('f_menu_master', 'string', label='Menu Master'),
        Field('f_ordem_master', 'integer', label='Ordenamento'),
        Field('f_system', 'string', label='Sistema'),
        Field('f_icon', 'string', label='icon'),
        format='%(f_menu_master)s',
        migrate=False)
#=====================================================================================
# menu
#=====================================================================================
#tabela do menu
db.define_table('t_menu',
        Field('f_menu_master', db.t_menu_master, label='Menu Master'),
        Field('f_menu_detalhe','string', label='Menu Detalhe'),
        Field('f_menu_controller','string',label='Controller'),
        Field('f_menu_funcao','string',label='Function'),
        Field('f_system','string',label='Sistema'),
        Field('f_men_ordem', 'integer', label='Ordenamento'),
        Field('f_icon', 'string', label='icon'),
        Field('f_need_sign', 'boolean', label='Assinatura de User'),
        format='%(f_menu_detalhe)s',
        migrate=False)

#=====================================================================================
# Menu x Grupos
#=====================================================================================
db.define_table('t_menu_grupo',
        Field('f_menu', db.t_menu, label='Menu'),
        Field('f_grupo',db.auth_group, label='Grupos'),
        migrate=False)

#=====================================================================================
# Systems
#=====================================================================================
db.define_table('t_systems',
        Field('f_acronym', 'string', label=T('Acronym')),
        Field('f_system', 'string', label=T('System')),
        Field('f_search_tables', 'text', label=T('Tables to GEneral Search')),
        Field('f_alias', 'string', label=T('Alias')),
        Field('f_create_date', 'datetime', label=T('create date')),
        Field('f_summary', 'text', label=T('Summary')),
        Field('f_icon', 'string', label=T('Icon')),
        Field('f_default_controller', 'string', label=T('controller')),
        Field('f_default_function', 'string', label=T('function')),
        format='%(f_system)s',
        migrate=False)
        
#=====================================================================================
# Menu x Sistemas
#=====================================================================================
db.define_table('t_menu_system',
        Field('f_system',db.t_systems,label='System'),
        Field('f_menu',db.t_menu,label='Function'),
        Field('f_obs','string',label='Function'),
        format='%(id)s',
        migrate=False)

#=====================================================================================
# User x System
#=====================================================================================

db.define_table('t_user_system',
        Field('f_user', db.auth_user ,label='User'), 
        Field('f_system',db.t_systems,label='System'),
        format='%(id)s',
        migrate=False)
