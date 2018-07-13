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
        
#========================================================
# user_visibility
#========================================================
    

def user_visibility(*groups):
    """in views, in class attribute: {{=user_visibility('list', 'of', 'authorized', 'user_groups')}}"""
    return 'hidden' if not is_user_member(*groups) else 'visible'
    
    
#========================================================
# is_user_member
#========================================================
    
        
def is_user_member(*roles):
    # @auth.requires(lambda: is_user_member('arg', 'list', 'of', 'roles')
    # if is_user_member('arg', 'list', 'of', 'roles'):

    # @auth.requires(lambda: any([auth.has_membership(r) for r in ['list', 'of', 'roles'])) # db lookups!?
    # if auth.user and any(auth.has_membership(r) for r in ['customer_service', 'admin']): # performs potentially 4 database queries
    # if auth.has_membership('customer_service'): # performs two database
    # restrict menu options based on membership
    # https://groups.google.com/d/msg/web2py/bz-mKIFqP1w/eEma0XOyCAAJ
    # https://groups.google.com/forum/#!searchin/web2py/response.menu$20auth.user_id$20auth.has_membership/web2py/E8Krnt9cxB8/xSpuPy8d6M4J
    # https://groups.google.com/forum/#!searchin/web2py/response.menu$20auth.user_id$20auth.has_membership/web2py/GvDAXRIpKA0/sEcPeB8a40oJ
    # https://groups.google.com/forum/#!topic/web2py/8AHYqV_EKy0

    user_auth_groups = [x.lower() for x in auth.user_groups.values()]
    required_auth_groups = [x.lower() for x in roles]

    if auth.user and any(role in required_auth_groups for role in user_auth_groups):
        return True
    else:
        return False