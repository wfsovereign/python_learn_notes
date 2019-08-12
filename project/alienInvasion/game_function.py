
import sys
import pygame 

from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ai_settings, screen, ship, bullets)
    
    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)

def check_keyup_events(event, ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False
  elif event.key == pygame.K_q:
    sys.exit()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    ship.moving_left = True
  elif event.key == pygame.K_SPACE:
    fire_bullet(ai_settings, screen, ship, bullets)

def update_screen(ai_settings, screen, ship, aliens, bullets):
  screen.fill(ai_settings.bg_color)
  for bullet in bullets.sprites():
    bullet.draw_bullet()
  ship.blitme()
  aliens.draw(screen)

  pygame.display.flip()

  

def update_bullets(bullets):

  bullets.update()

  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
  if len(bullets) < ai_settings.bullet_allowed:
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):

  alien = Alien(ai_settings, screen)
  alien_width = alien.rect.width

  number_alien_x = get_number_aliens_x(ai_settings, alien_width)

  for alien_number in range(number_alien_x):
    create_alien(ai_settings, screen, aliens, alien_number, alien_width)


def get_number_aliens_x(ai_settings, alien_width):
  available_space_x = ai_settings.screen_width - 2 * alien_width
  number_alien_x = int(available_space_x / (2 * alien_width))

  return number_alien_x

def create_alien(ai_settings, screen, aliens, alien_number, alien_width):
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)
  
  