def my_function(my_parameter):
    """This is my function.


    There are many like it, but this one is mine.
    My function is my best friend. It is my life.
    I must master it as I must master my life.

    Without me, my function is useless.
    Without my function, I'm useless.

    Parameters
    ----------
    my_parameter : string
        A parameter.


    Notes
    -----
    This docstring contains an undefined reference_.
    """
    pass


class MyClass(object):
    """This is a class.


    It has a docstring.

    It also has attributes:


    Attributes
    ----------
    not_attribute : string
        It's not actually there.

    bad_attribute_ : int
        This one has a trailing underscore. uh-oh!

    """
    def __init__(self):
        pass

    def other_method(self):
        """The method!

        This is the best method any class ever had!

        Parameters
        ----------
        self : MyClass instance
            Because it's a method! It's myself!

        parameter_with_underscore_ : because
            Apparently this is fine in parameters.

        Notes
        -----
        There's also an undefined_ reference here!
        """
        pass
