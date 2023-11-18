from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not (3 <= len(username) <= 20 and username.islower()):
            raise UserInputError("Username has to be 3-20 characters and have only lowercase letters")

        if not (8 <= len(password) and any(merkki.isalpha() for merkki in password) and any(merkki.isdigit() for merkki in password)):
            raise UserInputError("Password has to be at least 8 characters long and have numbers")
        
        if password != confirm_password:
            raise UserInputError("Incorrect password confirmation")