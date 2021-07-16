from typing import Callable, Any
import functools


def counter(called: Callable) -> Any:
    """Декоратор вызываемой функции осуществляет подсчет количества вызовов
    аргументы name:str, age:int передаются в вызываемою функцию
    Возвращает строку result"""

    @functools.wraps(called)
    def wrapped_called(*args, **kwargs) -> Any:
        wrapped_called.counter += 1
        print('Вызывается {}\t{args}, {kwarg}) '.
              format(called.__name__, args=args, kwarg=kwargs), end=' ')
        result = called(*args, **kwargs)
        print("\n'greeting' вызвана {} раз".format(wrapped_called.counter))
        print(result)
        return result
    wrapped_called.counter = 0
    return wrapped_called


@counter
def greeting(name, age=None) -> str:
    """Функция анализирует наличие аргумента  age.
        при наличии возвращает фразу с использованием name и age, при отсутствии только с name
        аргументы: name-str, age-int
        возвращает строку"""
    if age:
        result = "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)

    else:
        result = "Привет, {name}!".format(name=name)
    return result


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# зачет!
