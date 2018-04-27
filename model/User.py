#--*-- coding:utf-8 --*--
class User():
    def __init__(self,username):
        self.username=username
        self.passwd=None

    @property
    def username(self):
        return self.username

    @username.getter
    def username(self):
        return self.username

    @username.setter
    def username(self,username):
        self.username=username

    @property
    def passwd(self):
        return self.passwd
    @passwd.setter
    def passwd(self,passwd):
        self.passwd=passwd

    @passwd.getter
    def passwd(self):
        return self.passwd




class Profile():
    def __init__(self,user,email):
        self.user=user
        self.email=email
        self.birthday=None
        self.gender=None



def main():
    u=User('kangkai')
    u.username='kk'
    print u.username

if __name__ == '__main__':
    main()



