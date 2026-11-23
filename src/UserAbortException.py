# Exception raised to indicate user aborted operation
class UserAbortException(Exception):
    def __init__(self, message: str = "The user aborted the operation."):
        self.message = message
        super().__init__(self.message)
