print('what is your name?')

player_name = input()

rank = input('what class are you mage(M), warrior(W) or Swordsmage(S)?')
p_rank = False

playerm = {'name': player_name, 'atk': 5, 'heal': 16, 'health': 100, 'matk': 10}
playerw = {'name': player_name, 'atk': 10, 'heal': 16, 'health': 100, 'matk': 5}
players = {'name': player_name, 'attack': 10, 'heal': 16, 'health': 80, 'matk':10}
rival = {'name': 'Maximillian', 'atk': 12, 'heal': 10, 'health': 250}
goat = {'name': 'Kyle The Goat', 'atk': 235, 'heal': 70, 'health': 1350}
game_running = True

rival_won = False
player_won = False
while game_running == True:
    player

    print('please select an action')
    print('1) Attack')
    print('2) Heal')
    print('3) Switch to Kyle')
    player_choice = input()

    if player_choice == '1':
        rival['health'] = rival['health'] - player['attack']
        if rival['health'] <=0:
            pass

        else:
            player['health'] = player['health'] - rival['attack']
            if player['health'] <=0:
                pass
        print('rival health is', rival['health'])

    elif player_choice == '2':
        player['health'] = player['health'] + player['heal']
        rival['health'] = rival['health'] + rival['heal']
        print(player['name'], 'has healed your health is now', player['health'], 'but the monster has healed too! his health is now', rival['health'])
    
    elif player_choice == '3':
        print('You are now playing as Kyle')
        print('1) Goat Ram')
        print('2) Goat milk(heal)')
        print('3) Switch back to Abraham')
        kyle_choice = input()
        if kyle_choice == '1':
            rival['health'] = rival['health'] - goat['attack']
            goat['health'] = goat['health'] - rival['attack']
            print('attacking...')
            print('done 235 damage to Maximillian his health is now', rival['health'])
       
    else:
        print('invalid command')        

    if player['health'] <= 0 or rival['health'] <=0:
        print('game over')
        game_running = False   
      