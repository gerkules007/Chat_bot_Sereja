import json

class InputData:
    token: str
    json_dict: dict

    def get_token(self, path_t):
        with open(path_t, 'r') as tf:
            self.token = tf.read()
    
    def get_ai_bot_json(self, path_j):
        with open(path_j, 'r', encoding='utf-8') as read_file:
            self.json_dict : dict = json.load(read_file)

class AI_BOT:
    key_talk : dict
    answer : dict
    not_answer : list
    atrib = ['key_talk', 'answer', 'not_answer']

    def __init__(self, load_dict : dict):
        self.key_talk = load_dict[self.atrib[0]]
        self.answer = load_dict[self.atrib[1]]
        self.not_answer = load_dict[self.atrib[2]]