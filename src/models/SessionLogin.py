class SessionLogin:
    def __init__(self, session_id, username, password, session_id_version: str = "2.1"):
        self.session_id = session_id
        self.username = username
        self.password = password
        self.session_id_version = session_id_version
