#========================================================
# list_groups
#========================================================
def list_groups():

    try:
       idd = auth.user.id
    except:
       idd = 10
    list_groups = db(db.auth_membership.user_id==idd).select(db.auth_membership.group_id)
    lst_grp=[]
    for l in list_groups:
        lst_grp.append(int(l.group_id))
    return lst_grp
    
    
def list_menus_system(sys=4):
    list_mnus_sys = db(db.t_menu_system.f_system==sys).select(db.t_menu_system.f_menu)
    #print "db._lastsql de entro de list_menus_system => \n\n" , db._lastsql[0]
    lst_mns=[]
    for l in list_mnus_sys:
        lst_mns.append(int(l.f_menu))
    return lst_mns
    
#========================================================
# sidebar_menu_item
#========================================================
    
def sidebar_menu_item(label, url=None, icon='link', master=None):
    '''
    <li><a href="{{=URL('default','about')}}"><i class="fa fa-book"></i> <span>About</span></a></li>
    <a href="#"><i class="fa fa-gears"></i> <span>Admin</span> <i class="fa fa-angle-left pull-right"></i></a>
    '''

    if url:
        
        if url == URL():
            active = 'active' 
            session._menu_fat = master
            session._menu_fat_it = label
        else:
            active = None
            
            
        if session._menu_fat_it == label:
            active = 'active'
            
            
            
        icon_active = XML('<i class="fa fa-arrow-circle-left text-aqua pull-right" ></i>') if label == session._menu_fat_it else XML('')
        return LI(
            A(
                (I(' ', _class='fa fa-%s' % icon), SPAN(T(label), icon_active)),
                _href=url,
                _class="menu-tree menu-item",
                _data=label,
                
            ),
            _class= active
        )
    else:
        return A(
            (
                I(' ', _class='fa fa-%s' % icon),
                SPAN(T(label)),
                I(' ', _class='fa fa-angle-left pull-right'),
            ),
            _href="#"
        )