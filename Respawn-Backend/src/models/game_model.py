class Game:
    def __init__(self, owner_id, game_id, game_name, game_release_date, game_summary, game_status, game_list):
        self._owner_id = owner_id
        self._game_id = game_id
        self._game_name = game_name
        self._game_release_date = game_release_date
        self._game_summary = game_summary
        self._game_status = game_status
        self._game_list = game_list