decorator-pattern-example
=========================

This code gives a simple demonstration of how to implement the decorator design pattern in python. 

If you are trying to write an object-oriented code base that you intend to continually adapt by adding more features, using inheritance to create more complex objects from simpler ones can lead to lots of code duplication and redundancy. The more times identical code appears in more than one place, the greater the likelihood that a future change to one code segment will fail to be propagated to the other segment, which leads to bugs. This simple python code shows an archetypal example of how to use composition, rather than inheritance, to start from a simple object, and build ever more complex objects with new features. The major advantage of composition is that the existing code base need not ever be touched when adding a new bell or whistle, so that once your base code is debugged, it remains debugged.