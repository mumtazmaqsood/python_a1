

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
#list of dic
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n-----------------------------------------------")
#Make any empty list of aliens
aliens1 = []
for alien_number in range(1, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens1.append(new_alien)
#showing the first 5 aliens
for alien in aliens1[:5]:
    print(alien)

#counting total newly created aliens
print(len(aliens1))

#change the first 3 aliens color, speed and points
for alien in aliens1[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color']  == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 20
#showing first 5 alien
for alien in aliens1[:5]:
    print(alien)

print("\n-----------------------------------------------")



