from typing import Self


class Singleton(object):
  _instance: Self | None = None

  def __new__(cls) -> Self:
    if cls._instance is None:
      cls._instance = super().__new__(cls)

    return cls._instance

singleton = Singleton()
singleton2 = Singleton()
singleton3 = Singleton()

print(singleton, singleton2, singleton3)
