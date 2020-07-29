'''Answer for 9-12'''
from privileges_admin import Admin 

myself = Admin('yue','yu','female','yueyue','111222333@qq.com')
privileges = ['can add post','can delete post','can ban post']
myself.privileges.privileges = privileges #实例的privileges属性 = Privileges类的previliges属性
myself.privileges.show_privileges()