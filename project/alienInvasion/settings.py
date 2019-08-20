

class Settings():

  def __init__(self):

    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (230, 230, 200)
    
    self.ship_speed_factor = 8
    self.ship_limit = 2

    self.bullet_width = 8
    self.bullet_height = 15
    self.bullet_color = 60,60,60
    self.bullet_allowed = 30
    self.bullet_awesome = True


    self.fleet_drop_speed = 10

    self.fleet_direction = 1

    self.speedup_scale = 1.3
    self.score_scale = 2

    self.initialize_dynamic_settings()


  def initialize_dynamic_settings(self):

    self.ship_speed_factor = 10
    self.bullet_speed_factor = 16
    self.alien_speed_factor = 20
    self.fleet_direction = 1
    self.alien_points = 100

  def increase_speed(self):
    self.ship_speed_factor *= self.speedup_scale
    self.bullet_speed_factor *= self.speedup_scale
    self.alien_speed_factor *= self.speedup_scale
    self.alien_points = int(self.alien_points * self.score_scale)