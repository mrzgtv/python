goods = []
features = {'Description': '', 'Price': '', 'Q-ty': '', 'MeasUnit': ''}
analytics = {'Description': [], 'Price': [], 'Q-ty': [], 'MeasUnit': []}
num = 0
while True:
    if input('For quit type "Q", "ENTER" to continue: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        a = input(f'Enter "{f}": ')
        features[f] = int(a) if (f == 'Price' or f == 'Q-ty') else a
        analytics[f].append(features[f])
    goods.append((num, features))
    print(f'\nCurrent analytics: \n ')
    for key, value in analytics.items():
        print(f'{key}: {value}')