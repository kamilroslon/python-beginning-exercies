class ElementsInOrderLimit(Exception):
    def __init__(self, allowed_limit, message="Limit reached", *args):
        self.allowed_limit = allowed_limit
        super().__init__(message, *args)
