def my_func(a, b):
    """
    Returns the multiplication of two integers.

    Let's try

    >>> my_func(2, 7)
    14

    works well with numbers:

    >>> my_func('a', 4)
    'aaaa'

    and strings:

    >>> my_func(a, 4) # doctest: +SKIP
    Traceback (most recent call last):
      File "/usr/lib/python3.8/doctest.py", line 1336, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest hend.my_func[2]>", line 1, in <module>
        my_func(a, 4)
    NameError: name 'a' is not defined

    to be considered a string, it must have the quotes around it
    """

    return a * b
