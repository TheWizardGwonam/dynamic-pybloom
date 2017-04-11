dynamic-pybloom
===============

``dynamic-pybloom`` is a fork of the popular https://travis-ci.org/jaybaird/python-bloomfilter repo module
that includes a Bloom Filter data structure, an implementation of the Scalable Bloom Filter[1] and
a new implementation of the Dynamic Bloom Filter[2].

Bloom filters are great if you understand what amount of bits you need to set
aside early to store your entire set. Scalable Bloom Filters allow your bloom
filter bits to grow as a function of false positive probability and size.
Dynamic Bloom Filters allow your bloom filters to grow like a Scalable
Bloom Filter, but they preserve the ability to intersect or union with
one another.

A filter is "full" when at capacity: M * ((ln 2 ^ 2) / abs(ln p)), where M
is the number of bits and p is the false positive probability. When capacity
is reached a new filter is then created exponentially larger than the last
with a tighter probability of false positives and a larger number of hash
functions.

installation
============
either clone this repository and run

    $ python setup.py install
..
or simply

    $ pip install dynamic-python
..

examples
========
.. code-block:: python

    >>> from dynamic_pybloom import BloomFilter
    >>> f = BloomFilter(capacity=1000, error_rate=0.001)
    >>> [f.add(x) for x in range(10)]
    [False, False, False, False, False, False, False, False, False, False]
    >>> all([(x in f) for x in range(10)])
    True
    >>> 10 in f
    False
    >>> 5 in f
    True
    >>> f = BloomFilter(capacity=1000, error_rate=0.001)
    >>> for i in xrange(0, f.capacity):
    ...     _ = f.add(i)
    >>> (1.0 - (len(f) / float(f.capacity))) <= f.error_rate + 2e-18
    True

    >>> from dynamic_pybloom import ScalableBloomFilter
    >>> sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
    >>> count = 10000
    >>> for i in xrange(0, count):
    ...     _ = sbf.add(i)
    ...
    >>> (1.0 - (len(sbf) / float(count))) <= sbf.error_rate + 2e-18
    True
    # len(sbf) may not equal the entire input length. 0.01% error is well
    # below the default 0.1% error threshold. As the capacity goes up, the
    # error will approach 0.1%.

    >>> from dynamic_pybloom import DynamicBloomFilter
    >>> dbf = DynamicBloomFilter(base_capacity=100, max_capacity=100000, error_rate=0.001)
    >>> dbf.add(0)
    >>> len(dbf.filters)
    1
    >>> for i in xrange(1, 10000):
    ...     _ = sbf.add(i)
    ...
    >>> len(dbf.filters)
    100
    >>> other_dbf = DynamicBloomFilter(base_capacity=100, max_capacity=100000, error_rate=0.001)
    >>> other_dbf.add(5)
    >>> intersection = dbf & other_dbf
    >>> 5 in intersection
    True
    >>> 10 in intersection
    False
    # the Dynamic Bloom Filter grows as you add elements to it, but it still
    # preserves the ability to perform intersections and unions

..
references
==========
[1] P. Almeida, C.Baquero, N. Preguiça, D. Hutchison, Scalable Bloom Filters,
(GLOBECOM 2007), IEEE, 2007. http://www.sciencedirect.com/science/article/pii/S0020019006003127
[2] http://ieeexplore.ieee.org/document/4796196/?reload=true

