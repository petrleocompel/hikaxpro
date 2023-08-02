class SessionLogin:
    def __init__(self, session_id, username, password, session_id_version: str = "2.1"):
        self.sessionID = session_id
        self.userName = username
        self.password = password
        self.sessionIDVersion = session_id_version
