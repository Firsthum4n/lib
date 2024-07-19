class CustomError(Exception):
    """Базовый класс для пользовательских исключений."""
    pass


class ExistError(CustomError):
    def __init__(self, message='Уже существует'):
        self.message = message
        super().__init__(self.message)


is_exist_ex = ExistError


