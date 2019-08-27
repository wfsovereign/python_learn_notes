import os

path = os.path

highest_score_file_path = path.join(path.abspath('./'), 'static/highest_score.txt')

class GameStats():

  def __init__(self, ai_settings):

    self.ai_settings = ai_settings
    self.game_active = False
    self.init_hightest_score()
    self.reset_stats()

  def reset_stats(self):
    self.ships_left = self.ai_settings.ship_limit
    self.score = 0
    self.level = 1
    self.init_hightest_score()

  def set_high_score(self, score):
    self.high_score = score
    self.update_highest_score()

  def init_hightest_score(self):
    with open(highest_score_file_path, 'r') as file_obj:
      file_content = file_obj.read()
      if not file_content:
        file_content = '0'
      high_score = int(file_content)
      self.high_score = high_score

  def update_highest_score(self):
    if (self.score > self.high_score):
      with open(highest_score_file_path, 'w') as file_obj:
        file_obj.write(str(self.score))
        