def get_started():
    password = request.vars.password.strip()
    id_admin_user, id_admin_grp = None,None
    base_sys =db(db.t_systems.f_system=="awesome").select()
    if not base_sys:
        id_base_sys = db.t_systems.insert(
                                        f_system = "awesome", 
                                        f_acronym = "aw", 
                                        f_alias = "Awesome", 
                                        f_icon = "cogs", 
                                        f_summary = "Awesome System is a template system to allow you beggining awesome apps", 
                                        )


                            
    admin_user =db(db.auth_user.username=="admin").select()                        
    if not admin_user:
        id_admin_user = db.auth_user.insert(
                                        username = "admin", 
                                        first_name = "admin", 
                                        last_name = "admin", 
                                        password = CRYPT()('%s' % password)[0],)
                                     
    admin_grp =db(db.auth_group.role=="admin").select() 
    if not admin_user:
        id_admin_grp = db.auth_group.insert(
                                        role = "admin", 
                                        descriptio = "admin automatic inserted on %s" % str(request.now), 
                                        )  

    if id_admin_user:
        membership = db.auth_membership.insert(
                                        user_id = id_admin_user, 
                                        group_id = id_admin_grp
                                        )                                    
                                        
    master =db(db.t_menu_master.id>0).select()

    if not master:
        id = db.t_menu_master.insert(f_menu_master = "Admin", f_icon = "cogs")


        ids_menus = db.t_menu.bulk_insert([
                            {'f_need_sign': False,
                            'f_menu_master': id ,
                            'f_menu_funcao': 'groups_manage',
                            'f_menu_controller': 'adminlion',
                            'f_menu_detalhe': 'Grupos',
                            'f_icon': 'circle-o',},
                            {'f_need_sign': False,
                            'f_menu_master': id,
                            'f_menu_funcao': 'users_manage',
                            'f_menu_controller': 'adminlion',
                            'f_menu_detalhe': 'Users',
                            'f_icon': 'circle-o',},                    
                            {'f_need_sign': False,
                            'f_menu_master': id ,
                            'f_menu_funcao': 'menu_manage',
                            'f_menu_controller': 'adminlion',
                            'f_menu_detalhe': 'Menu',
                            'f_icon': 'circle-o',},
                            
                            ])
                            
        for idd in ids_menus:
            db.t_menu_grupo.insert(
                                        f_menu = idd, 
                                        f_grupo = id_admin_grp
                                        )
            db.t_menu_system.insert(
                                        f_menu = idd, 
                                        f_system = id_base_sys
                                        )
                                        
    return redirect(URL('default', 'index'))