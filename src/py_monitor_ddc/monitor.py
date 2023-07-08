import typer
import monitorcontrol
from typing import Callable


app = typer.Typer()
monitors = monitorcontrol.get_monitors()


def try_execute(func: Callable, args: tuple=None, attempts: int=3) -> None:
    '''
    Attempts to execute callable for the specified number of attempts.

    Args:
        func (Callable): The function to be executed.
        args (tuple, optional): Arguments to be passed to the callable. Defaults to None.
        attempts (int, optional): The number of attempts to execute the function. Defaults to 3.

    Returns:
        None
    '''
    exceptions = []
    for attempt in range(0, attempts):
        try:
            # Handle arguments
            if args is None:
                func()
            else:
                func(*args)
            # Code below will only execute if the function will not throw an exception
            break
        except Exception as e:
            exceptions.append(e)
    else:
        # This code block will only execute after function fails to execute attempt-times
        print(f'Failed to execute \'{func.__name__}\', the following exceptions occured:')
        for index, exception in enumerate(exceptions):
            print(f'{index}: {exception}')
        return

    

def set_all_monitor_luminance(luminance: int) -> None:
    for monitor in monitors:
        with monitor:
            monitor.set_luminance(luminance)


@app.command()
def brightness(brightness: int) -> None:
    try_execute(set_all_monitor_luminance,args=(brightness,))

