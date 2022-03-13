def say_hello(name: str = 'Lucas'):
    print(f'Hello {name} ')


def ask_age():
    age_user = input('Age?')
    return age_user


def say_hello_mp(name, age_user=25):
    print(f'Hello {name} {age_user}')


if __name__ == '__main__':
    print(say_hello('Pierre'))
    say_hello_mp(age_user=23, name='toto')
    age = ask_age()

    print(f'You are {age} year(s) old')
