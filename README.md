### Some Project Euler Problems

Some years ago I did some of these problems in [Haskell](https://github.com/ewilson/haskell-euler) in order
to learn the language a bit.

Now I'm doing some in Python 3. I already know Python, but I rarely do mathematical stuff, or have
to think about efficiency.

#### Solutions

The solution to problem 3 is the function named `f` in the module `pe003.py`. Usually. Sometimes you will find
two functions, `f0` and `f1`. In this case, `f0` is the easy-to-read function I would normally write, and `f1` is 
the one that performs well.

You will also find `test_f` functions in each module, these are for running with `py.test`. Unfortunately, these
will give away the solution, but I'm sure others on the Internet have done that already.

#### Performance

The _one-minute rule_ that Project-Euler mentions is surely a bit outdated. I'm including my `timeit` results in the
`docstring` of each function, and I'm going to try to keep individual problems under 60 milliseconds in any case.

I'll try to keep the cumulative computation time under 1 second. 
Currently all tests can be run in under 10 milliseconds.

#### Tests

On my machine, I run tests with:

    $ python3 -m pytest
    
Since `$ py.test` alone uses python 2.
