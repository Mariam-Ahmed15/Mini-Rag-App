from helper.config import get_settings, Settings

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()