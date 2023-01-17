from django.contrib.auth.hashers import make_password, check_password


class Utils():

    @staticmethod
    def get_encrypted_password(password):

        return make_password(password)

    @staticmethod
    def check_password(password, hashed_password):

        return True if check_password(password, hashed_password) else False