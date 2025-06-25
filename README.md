# A Template Collection of useful python snippets

## How to use?

- You need to download this Extension for VSCode [easy-snippet](https://marketplace.visualstudio.com/items/?itemName=inu1255.easy-snippet)
- Go to the Snippet Tab(Its normally on the left side)
- Create a new group(click plus)
- Select your language
- In this Group create a new snippet
- Give your snippet a key
- Here you copy&paste some lines of code.
- In python you can access this snippet by typing your key, **ENTER** and there is your snippet!

> [!WARNING]
> Some snippets might need a bit extra work!

## Snippets

### Files

Reading, writing & creating

>```
> def file_read(filepath : str) -> str:
>     
>     with open(filepath, 'r') as f:
>         return f.read()
>```