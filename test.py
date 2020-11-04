env_dice = {0: 'stg', 1: 'prd', 2: 'preview'}

a = int(input(''))
if a in env_dice:
    print('in')
else:
    print('not in')