from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'empty'
    elif 'hello' in lowered:
        return 'hello there!'
    elif 'roll dice' in lowered:
        return f'you roalled: {randint(1,6)}'
    else:
        return choice(['nothing','repeate','okay'])