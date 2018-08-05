# coding: utf8
'''
██╗     ██╗ ██████╗ ███╗   ██╗██████╗  █████╗ ████████╗ █████╗ 
██║     ██║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██║     ██║██║   ██║██╔██╗ ██║██║  ██║███████║   ██║   ███████║
██║     ██║██║   ██║██║╚██╗██║██║  ██║██╔══██║   ██║   ██╔══██║
███████╗██║╚██████╔╝██║ ╚████║██████╔╝██║  ██║   ██║   ██║  ██║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&((#@@@@@@@@@@@@&%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@      .@&/.     ....     ,&@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@  ,(%*    /. *@@(           %@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@(/(.    .%&.      *,        ,.    ,&@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@/         /          #            #@&/.@@@@@@@@@@@@@
@@@@@@@@@@@@@@/              */. ,*/   (        ,%.    ,@@@@@@@@@@@@@@
@@@@@@@@@@@@@%      .#*           ./  ..          @@@%.   &@@@@@@@@@@@
@@@@@@@@@@@@%.    &&/         *.  (( ./,             *%@%  ,@@@@@@@@@@
@@@@@@@@*.* .               /@     (%(#*           ..     ,/ *@@@@@@@@
@@@@@/                     &@@@*..   #(   (         *@.        %@@@@@@
@@@%                      &@@@@@*    &/  (& ,&      ,@@&     ,@,/@@@@@
@@@&/         ,.         &@@@@@.  .  .@   *@@. *@*,#@@@@&     #@&*@@@@
@@@@#       /@@@@@@*      %@@@@###   ,&  .&@  .@@@@@@@@@@%     @@@@@@@
@@@@@/      #@@@@@@@@*    .@@@@&   .&,  (@&  .@(     &@@@@     &@@@@@@
@@@@@@@@@.   %@@@@@@@@%   .@@#  .   *@@   *         @@@@,    (@@@@@@@@
@@@@@@@@@@@@@&@@@@@@@@@   &&   @/   ,@@@              (@@@,    /@@@@@@
@@@@@@@@@@@@@@@@@,//*.  .@@.  #%   /@@@@@*   ,&&      ,@@@     %@@@@@@
@@@@@@@@@@@@@@@@@@*   (@@@@.   @*     @@@@@@@@@.      ,@@*    ,@@@@@@@
@@@@@@@@@@@@@@@@@@/        .    *@     @@@@@@@,       /@%    .#@@@@@@@
@@@@@@@@@@@@@@@@@@@@@/&.         (@    /@@@@@,     .  #@    ./@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@, #         #&    #@@@@/      #  %*   ,(,@@@@@@@@
@@@@@@@@@@@@@@@@@@/  .#      * .&*    .@@@@,     ,@       %* /@@@@@@@@
@@@@@@@@@@@@@&,   ,*       .,%%       @@@%      &@      #@   .@@@@@@@@
@@@@@@@@@@@.,%*          (         @@@,     &@,    ,@@,    @@@@@@@@@@@
@@@@@@@@@%&.    ..,*#&@@@,         /@@*    (@@*   .&@#      &@@@@@@@@@
@@@@@@@@@ .&@@@@@@@@@@@,         .@@,   #@@%   *@@&.       &@@@@@@@@@@
@@@@@@@@.@@@@@@@@@@@@(     *    #&.  *@@&. .#@@&,        (@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%  .%@,    (.  (@@@#&@@@&,        .%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@,/@@%       ,&@@@@@&*         ,#@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&@@%     ,&@@@@(.     .*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&   .%@@@%. ./&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@, *@@@@@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%.&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''

@auth.requires_membership(role="admin")
@auth.requires_login()
def groups_manage():
    form_groups = SQLFORM.grid(db.auth_group,
                buttons_placement='left', # Botões a esquerda
        showbuttontext=False, # Exibe os botões
        deletable=False,
        _class='web2py_grid',
    	exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,json=False,tsv_with_hidden_cols=False))
    if request.args(-2) == 'new':
       redirect(URL('grupo_editar'))
    elif request.args(-3) == 'edit':
       idd = request.args(-1)
       redirect(URL('grupo_editar', args=idd ))


    return dict(form_groups=form_groups)

#=====================================================================
# funcao de edicao dos artigos
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def grupo_editar():
# Armazena o ID do grupo
    id_grupo = request.args(0)

    if id_grupo:
       grupo = db.auth_group(id_grupo)
    else:
       id_grupo = 0

    buttons = [TAG.button(T(' Save and continue'), _type="submit", _class="fa fa-save btn bg-olive margin")]

    form_grupo_editar = SQLFORM(db.auth_group,id_grupo if id_grupo != 0 else None,
                                      buttons =buttons,
                                      submit_button=T(' Save and continue'),
                                      field_id='id',
                                      _id='form_grupo_editar')

    for c in form_grupo_editar.elements('input','select', 'textarea'): c.add_class('span12')
    form_grupo_editar.element(_name='description')['_rows'] = '2'

    if form_grupo_editar.process().accepted:
        response.flash = 'Efetuado com sucesso!'
        redirect(URL('grupo_editar', args=[form_grupo_editar.vars.id] ))

    elif form_grupo_editar.errors:
        response.flash = 'Erro no Cadastro do Grupo principal!'

    #testa se
    if id_grupo != 0:

        form_users = LOAD(c='adminlion',
                     f='users_listar',
                     args=[id_grupo],
                     content='Aguarde, carregando...',
                     target='lista_usuarios',
                     ajax=True)
        form_permissions = LOAD(c='adminlion',
                     f='permissions_listar',
                     args=[id_grupo],
                     content='Aguarde, carregando...',
                     target='lista_permissoes',
                     ajax=True)
    else:

        form_users = "Primeiro cadastre o Grupo"
        form_permissions = "Primeiro cadastre o Grupo"

    return dict(form_grupo_editar=form_grupo_editar, form_users=DIV(form_users,_class='well'), form_permissions=form_permissions)


#=====================================================================
# funcao de listar users do Grupo
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def users_listar():


   id_grupo = request.args(0)
   db.auth_membership.group_id.default = id_grupo
   #oculta id
   db.auth_membership.group_id.readable = \
   db.auth_membership.group_id.writable = False
   frm_listausers = SQLFORM.grid(db.auth_membership.group_id==id_grupo,
       fields=[db.auth_user.username,
       	db.auth_user.email],
       buttons_placement='left', # Botões a esquerda
       left=db.auth_membership.on(db.auth_membership.user_id==db.auth_user.id),
       showbuttontext=False, # Exibe os botões
       _class='web2py_grid',
       formname='lista_usuarios',
       searchable=False,
       args=[id_grupo],
    	exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,json=False,tsv_with_hidden_cols=False, tsv=False, csv=False))


   return dict(frm_listausers=frm_listausers)


#=====================================================================
# funcao de listar permissions do Grupo
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def permissions_listar():

       id_grupo = request.args(0)
       db.auth_permission.group_id.default = id_grupo

       db.auth_permission.group_id.readable = \
       db.auth_permission.group_id.writable = False
       frm_listaperms = SQLFORM.grid(db.auth_permission.group_id==id_grupo,
          buttons_placement='left', # Botões a esquerda
          showbuttontext=False, # Exibe os botões
          _class='web2py_grid',
          formname='lista_permissoes',
          searchable=False,
          args=[id_grupo],
    	  exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
    	  json=False,tsv_with_hidden_cols=False, tsv=False, csv=False))


       return dict(frm_listaperms=DIV(frm_listaperms,_class='well'))


#=====================================================================
# funcao de Users Manage
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def users_manage():
    form_users = SQLFORM.grid(db.auth_user,
                buttons_placement='left', # Botões a esquerda
        #field_id= db_prodmal.ARTIGOS.COD_ARTIGO,
        #field_id= ' ',
        showbuttontext=False, # Exibe os botões
        deletable=False,
        _class='web2py_grid',
    	exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
    	json=False,tsv_with_hidden_cols=False))
    if request.args(-2) == 'new':
       redirect(URL('user_editar'))
    elif request.args(-3) == 'edit':
       idd = request.args(-1)
       redirect(URL('user_editar', args=idd ))


    return dict(form_users=form_users)
#=====================================================================
# funcao de Users Manage
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def systems_manage():
    form_systems = SQLFORM.grid(db.t_systems,
                buttons_placement='left', # Botões a esquerda
        #field_id= db_prodmal.ARTIGOS.COD_ARTIGO,
        #field_id= ' ',
        showbuttontext=False, # Exibe os botões
        deletable=False,
        _class='web2py_grid',
    	exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
    	json=False,tsv_with_hidden_cols=False))


    return dict(form_systems=form_systems)
#=====================================================================
# funcao de Users Manage
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def user_editar():
# Armazena o ID do grupo
    id_user = request.args(0)

    if id_user:
       user = db.auth_user(id_user)
    else:
       id_user = 0

    buttons = [TAG.button(T(' Save and continue'), _type="submit", _class="fa fa-save btn bg-olive margin")]

    # Form edição do colaborador
    if id_user == 0:
        form_user_editar = SQLFORM(db.auth_user,
                                          buttons =buttons,
                                          submit_button='Incluir',
                                          field_id='id',
                                          #field_id='COD_ARTIGO',
                                          _id='form_user_editar')
    else:
        form_user_editar = SQLFORM(db.auth_user,id_user,
                                          buttons =buttons,
                                          submit_button='Alterar',
                                          _id='form_user_editar' ,
                                          field_id='id'
                                          #field_id='COD_ARTIGO'
                                          )


    if form_user_editar.process().accepted:
        response.flash = 'Efetuado com sucesso!'
        redirect(URL('user_editar', args=[form_user_editar.vars.id] ))

    elif form_user_editar.errors:
        response.flash = 'Erro no Cadastro do Grupo principal!'

    #testa se
    if id_user != 0:

        form_grupos = LOAD(c='adminlion',
                     f='users_listar_grupos',
                     args=[id_user],
                     content='Aguarde, carregando...',
                     target='lista_users',
                     ajax=True
        )
        form_systems = LOAD(c='adminlion',
                     f='users_listar_sys',
                     args=[id_user],
                     content='Aguarde, carregando...',
                     target='lista_sys',
                     ajax=True
        )
    else:

        form_grupos = "Primeiro cadastre o User"
        form_systems = "Primeiro cadastre o User"

    return dict(form_user_editar=form_user_editar, form_grupos=form_grupos, form_systems=form_systems)
#=====================================================================
# funcao de Users listar grupos
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def users_listar_grupos():

   id_user=request.args(0)
   db.auth_membership.user_id.default = id_user

   db.auth_membership.user_id.readable = \
   db.auth_membership.user_id.writable = False
   
   frm_listausers_grp = SQLFORM.grid(db.auth_membership.user_id==id_user,
      fields=[db.auth_group.id,
      db.auth_group.role,
      db.auth_group.description],
      buttons_placement='left', # Botões a esquerda
      #left=db.auth_membership.on(db.auth_membership.group_id==db.auth_group.id),
      showbuttontext=False, # Exibe os botões
      _class='web2py_grid',
      formname='lista_grupos',
      searchable=False,
      args=[id_user],
	  exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
      json=False,tsv_with_hidden_cols=False, tsv=False, csv=False))

   return dict(frm_listausers_grp=frm_listausers_grp)

   
#=====================================================================
# funcao de Users listar Sistemas associados
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def users_listar_sys():

   id_user=request.args(0)

   
   db.t_user_system.f_user.default = id_user

   db.t_user_system.f_user.readable = \
   db.t_user_system.f_user.writable = False

   frm_listausers_sys = SQLFORM.grid(db.t_user_system.f_user==id_user,

      fields=[db.t_user_system.id,
      db.t_user_system.f_user,
      db.t_user_system.f_system],
      buttons_placement='left', # Botões a esquerda
      #left=db.t_user_system.on(db.t_user_system.f_user==db.auth_user.id),
      showbuttontext=False, # Exibe os botões
      _class='web2py_grid',
      formname='lista_sys',
      searchable=False,
      args=[id_user],
	  exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
      json=False,tsv_with_hidden_cols=False, tsv=False, csv=False))

   return dict(frm_listausers_sys=frm_listausers_sys)   
#=====================================================================
# funcao de Users listar Sistemas associados
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def menu_listar_sys():

   id_menu=request.args(0)

   
   db.t_menu_system.f_menu.default = id_menu

   db.t_menu_system.f_menu.readable = \
   db.t_menu_system.f_menu.writable = False

   frm_listamenu_sys = SQLFORM.grid(db.t_menu_system.f_menu==id_menu,

      fields=[db.t_menu_system.id,
      db.t_menu_system.f_menu,
      db.t_menu_system.f_system],
      buttons_placement='left', # Botões a esquerda
      #left=db.t_user_system.on(db.t_user_system.f_user==db.auth_user.id),
      showbuttontext=False, # Exibe os botões
      _class='web2py_grid',
      formname='lista_sys',
      searchable=False,
      args=[id_menu],
	  exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
      json=False,tsv_with_hidden_cols=False, tsv=False, csv=False))

   return dict(frm_listamenu_sys=frm_listamenu_sys)

#=====================================================================
# funcao de Menu Manage
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def menu_manage():
    form_menu = SQLFORM.grid(db.t_menu,
                buttons_placement='left', # Botões a esquerda
        #field_id= db_prodmal.ARTIGOS.COD_ARTIGO,
        #field_id= ' ',
        showbuttontext=False, # Exibe os botões
        deletable=False,
        _class='web2py_grid',
    	exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
    	json=False,tsv_with_hidden_cols=False))
    if request.args(-2) == 'new':
       redirect(URL('menu_editar'))
    elif request.args(-3) == 'edit':
       idd = request.args(-1)
       redirect(URL('menu_editar', args=idd ))

    form_menu_master = LOAD(c='adminlion',
                     f='menumaster_listar.load',
                     content='Aguarde, carregando...',
                     target='lista_master',
                     ajax=True
    )

    return dict(form_menu=form_menu, form_menu_master=form_menu_master)

#=====================================================================
# funcao de Menu Master
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def menumaster_listar():
    frmmaster= SQLFORM.grid(db.t_menu_master,
          buttons_placement='left', # Botões a esquerda
          showbuttontext=False, # Exibe os botões
          _class='web2py_grid',
          formname='lista_master',
          searchable=False,
          deletable=False,
      	  exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
          json=False,tsv_with_hidden_cols=False, tsv=False, csv=False))

    return frmmaster

#=====================================================================
# funcao de Menu Editar
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def menu_editar():
# Armazena o ID do grupo
    id_menu = request.args(0)

    if not id_menu:
       id_menu = 0

    buttons = [TAG.button(T(' Save and continue'), _type="submit", _class="fa fa-save btn bg-olive margin")]

    form_menu_editar = SQLFORM(db.t_menu,id_menu if id_menu !=0 else None,
                                buttons =buttons,
                                submit_button=T(' Save and continue'),
                                field_id='id',
                                _id='form_menu_editar')

    if form_menu_editar.process().accepted:
        response.flash = 'Efetuado com sucesso!'
        redirect(URL('menu_editar', args=[form_menu_editar.vars.id] ))

    elif form_menu_editar.errors:
        response.flash = 'Erro no Cadastro do Menu!'

    form_grupos_menu = LOAD(c='adminlion',
                 f='listar_grupos_menu',
                 args=[id_menu],
                 content='Aguarde, carregando...',
                 target='lista_grp',
                 ajax=True) if id_menu != 0 else T("Primeiro cadastre o Menu")
                 
                 
    form_systems = LOAD(c='adminlion',
             f='menu_listar_sys',
             args=[id_menu],
             content='Aguarde, carregando...',
             target='lista_sys',
             ajax=True
                    )  if id_menu != 0 else ("Primeiro cadastre o Menu")

    return dict(form_menu_editar=form_menu_editar, 
                form_grupos_menu=form_grupos_menu,
                form_systems=form_systems)


#=====================================================================
# funcao de Users listar grupos
#=====================================================================

@auth.requires_membership(role="admin")
@auth.requires_login()
def listar_grupos_menu():

   id_menu=request.args(0)
   db.t_menu_grupo.f_menu.default = id_menu

   db.t_menu_grupo.f_menu.readable = \
   db.t_menu_grupo.f_menu.writable = False

   frm_listagrupos_menu = SQLFORM.grid(db.t_menu_grupo.f_menu==id_menu,
      buttons_placement='left', # Botões a esquerda
      #left=db.t_menu_grupo.on(db.t_menu_grupo.f_grupo==db.auth_group.id),
      showbuttontext=False, # Exibe os botões
      _class='web2py_grid',
      formname='lista_grupos_menu',
      searchable=False,
      args=[id_menu],
	  exportclasses=dict(xml=False,html=False,csv_with_hidden_cols=False,
      json=False,tsv_with_hidden_cols=False, tsv=False, csv=False))

   return dict(frm_listagrupos_menu=frm_listagrupos_menu)
   
#=====================================================================
# funcao de Zerar Systema
#====================================================================   
def reset_sys():   
    zera_sys()
    return redirect(URL('default','index'))
    
#=====================================================================
# Set System
#=====================================================================      
def set_sys():  
    sys_id = request.args(0)
    sys = db.t_systems[sys_id]
    print( sys)
    session._sys = sys_id
    try:
        session._sys_defcontroller = sys['f_default_controller'] 
    except:
        session._sys_defcontroller = 'default'
        
    try:
        session._sys_deffunction = sys['f_default_function'] 
    except:
        session._sys_deffunction = 'welcome'
    
    session._sys_logo = sys['f_alias'] or "LionSys"
    session._sys_acr = sys['f_acronym'] or "LS"
    session._sys_logo_logomini = XML("<i class='fa fa-fw fa-%s'></i>" % (sys['f_icon'] or "cogs"))
    session._sys_searchtables=''
    '''
    for tbl in db.tables:
        if hasattr(db[tbl],'_extra'):
            if 'search' in db[tbl]._extra.keys():
                session._sys_searchtables+='%s,' % tbl
    '''
    for tbl in db55.tables:
        if hasattr(db55[tbl],'_extra'):
            if 'search' in db55[tbl]._extra.keys():
                session._sys_searchtables+='%s,' % tbl
    print("\n\n\n session._sys_searchtables=>", session._sys_searchtables)

    return redirect(URL(c='default',f='welcome'))
