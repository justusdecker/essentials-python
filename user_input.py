def check_user_input_until_integer(prompt:str) -> int:
    user_input: str = ""
    while not user_input:
        user_input = input(prompt)
        user_input = user_input if user_input.isdecimal() else ""
    return int(user_input)