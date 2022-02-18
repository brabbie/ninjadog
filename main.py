import characters.ninjadog as nd

if __name__ == '__main__':
    print('='*20, 'NinjaDog', '='*20)
    name = input('Name your NinjaDog: ')
    ninja = nd.NinjaDog('Nash')
    print(f'''
Welcome to the NinjaDog dogo! It's like dojo but dogo. Get it? If not, fuck out of here.
This is where you can train for future adventures. Some training requires XP. To gain XP,
go on adventures!

What does {ninja.name} want to do first?

> ''', end='')
    action = input('') 
