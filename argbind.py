import functools
import inspect



def bind(func, *args, **kwargs):
  return functools.partial(
      func,
      *args,
      **{arg_name : kwargs[arg_name] for arg_name in _arg_names(func)
         if arg_name in kwargs})


def _arg_names(func):
  return inspect.getargspec(func).args
