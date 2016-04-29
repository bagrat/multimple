# multimple

[![Build Status](https://travis-ci.org/n9code/multimple.svg?branch=master)](https://travis-ci.org/n9code/multimple)
[![Code Health](https://landscape.io/github/n9code/multimple/master/landscape.svg?style=flat)](https://landscape.io/github/n9code/multimple/master)
[![Coverage Status](https://coveralls.io/repos/github/n9code/multimple/badge.svg?branch=master)](https://coveralls.io/github/n9code/multimple?branch=master)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/n9code/multimple/master/LICENSE)

Multimple provides a decorator that lets you define multiple implementations a Python class and use them in an easy way. Ok, less words, more code:

    from multimple import multimple

    @multimple
    class YourClass(object):
        @multimple('impl1')
        def your_function(self):
            print('This is impl1')

        @your_function.multimple('impl2')
        def your_function(self):
            print('This is impl2')

Now go ahead and use your beautiful new class:

    >>> Impl1 = YourClass.multimple('impl1')
    >>> Impl2 = YourClass.multimple('impl2')
    >>> Impl3 = YourClass.multimple('impl3')
    >>> Impl1().your_function()
    This is impl1
    >>> Impl2().your_function()
    This is impl2
    >>> Impl3().your_function()
    Traceback (most recent call last):
        ...
    NotImplementedError: 'your_function' is not implemented for 'impl3'
