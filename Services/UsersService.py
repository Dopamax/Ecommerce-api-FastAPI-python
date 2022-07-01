from Dtos.User.UserSignInDto import UserSignInDto
from Models.User import User

class UsersService:
    users = []
    users.append(User("Hicham ElGUERROUJ","+21269854721","hicham.e@gmail.com","123456","Rabat","Morocco"))
    users.append(User("Nezha BIDOUANE","+21269125421","nezha.b@gmail.com","123456","Settat","Morocco"))
    
    def getAllUsers(self):
        return self.users

    def register(self, user:User):
        self.users.append(user)
    
    def signIn(self, userSignIn:UserSignInDto):
        for u in self.users:
            if u.email == userSignIn.email:
                if u.password == userSignIn.password:
                    return True
        return False