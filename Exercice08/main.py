def log_decorator(func):
     pass
 

def log_decorator(func):
    """Décorateur qui log un message avant et après l'exécution de func.

    Args:
        func (callable): La fonction (sans arguments) à décorer.

    Returns:
        callable: La fonction enrichie (wrapper).
    """
    def wrapper():
        print(f"Début de l'exécution de {func.__name__}")
        func()
        print(f"Fin de l'exécution de {func.__name__}")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()