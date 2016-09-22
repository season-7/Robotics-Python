class Config():
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


config = {'development': Config}
