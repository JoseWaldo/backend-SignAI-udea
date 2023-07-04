class Response:
    def __init__(self, data=None, code_status=None, message=None):
        self._data = data
        self._code_status = code_status
        self._message = message

    @property
    def data(self) -> object:
        return self._data

    @data.setter
    def data(self, new_value_data):
        self._data = new_value_data

    @property
    def code_status(self) -> int:
        return self._code_status

    @code_status.setter
    def code_status(self, new_value_code_status):
        self._code_status = new_value_code_status

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, new_value_message):
        self._message = new_value_message
