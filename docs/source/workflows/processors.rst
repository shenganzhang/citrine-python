Processors
==========

A processor defines how a :doc:`design space <design_spaces>` is searched.
There are three processors:

-  `EnumeratedProcessor <#enumerated-processor>`__ enumerates up to a fixed number of materials from a finite, enumerable space.
-  `GridProcessor <#grid-processor>`__ creates finite, enumerable space from a (semi-)continuous one by discretizing the continuous variables and enumerating the finite variables.
-  `MonteCarloProcessor <#monte-carlo-processor>`__ uses Monte Carlo methods to explore a space, taking a semi-directed random walk to find high-performing points.

Enumerated processor
--------------------

An :class:`~citrine.informatics.processors.EnumeratedProcessor` takes up to a maximum number of materials from a :doc:`design space <design_spaces>` and processes each independently.
The maximum number of candidates sampled from the Design Space is defined by the optional ``max_candidates`` parameter when creating an :class:`~citrine.informatics.processors.EnumeratedProcessor` using the Citrine Python client.
To be valid, enumerated processors must have a maximum number of candidates of at least 1.

An enumerated processor can be used with finite and infinite Design Spaces.
A finite space can be defined using an :class:`~citrine.informatics.design_spaces.EnumeratedDesignSpace` or a :class:`~citrine.informatics.design_spaces.ProductDesignSpace` composed only of :class:`EnumeratedDimensions <citrine.informatics.dimensions.EnumeratedDimension>`.
In these cases, the processor will systematically pull up to ``max_candidates`` samples from the space.

An infinite Design Space is created when a :class:`~citrine.informatics.design_spaces.ProductDesignSpace` contains one or more continuous dimensions.
When an enumerated processor is combined with an infinite Design Space, ``max_candidates`` samples are always pulled from the domain.
If all dimensions of a Design Space are continuous, samples are created by randomly sampling from each dimension.
If there are mixed continuous and enumerated dimensions in the Design Space, samples are created by combining the Cartesian product of enumerated dimensions with random samples from continuous dimensions.
Finite elements repeat once the Cartesian product is exhausted.

The following demonstrates how to create an enumerated processor that takes up to 100 samples from a Design Space, register it with a project, and view validation results:

.. code:: python

   from time import sleep
   from citrine import Citrine
   from citrine.informatics.processors import EnumeratedProcessor

   # create a session with citrine using API variables
   session = Citrine(api_key=API_KEY)

   project = session.projects.register('Example project')

   # create an enumerated processor and register it with the project
   processor = project.processors.register(
       EnumeratedProcessor(
           name='Enumerated processor',
           description='Samples up to 100 items from a design space',
           max_candidates=100
       )
   )

   # wait until the processor is no longer validating
   # we must get the processor every time we wish to fetch the latest status
   while project.processors.get(processor.uid).status != "VALIDATING":
       sleep(10)

   # print final validation status and status information
   validated_processor = project.processors.get(processor.uid)
   print(validated_processor.status)
   print(processor.status_info)

Grid processor
--------------

A :class:`~citrine.informatics.processors.GridProcessor` generates samples from the outer product of finite dimensions.
This processor can only be used with a :class:`~citrine.informatics.design_spaces.product_design_space.ProductDesignSpace`.
To create a finite set of materials from continuous dimensions, a uniform grid is created between the bounds of the descriptor.
The number of points is specified by ``grid_sizes``.
``grid_sizes`` is a map from descriptor key to the number of points to select between bounds of the dimension.
For example, if the dimension is bounded by 0 and 10 and the grid size is 11, points are taken from 0 to 10 in increments of 1.
Each continuous dimension in the Design Space must be given a grid size.
Enumerated dimensions cannot be given a grid size because it is not clear how to downsample or create a grid for a finite dimension.

The following demonstrates how to create a grid processor that searches
a 2D Design Space of enumerated x values and continuous y values:

.. code:: python

   from citrine.informatics.descriptors import RealDescriptor
   from citrine.informatics.dimensions import ContinuousDimension, EnumeratedDimension
   from citrine.informatics.processors import GridProcessor

   # create descriptors for x and y
   x = RealDescriptor(key='x', lower_bound=0, upper_bound=10, units='')
   y = RealDescriptor(key='y', lower_bound=0, upper_bound=100, units='')

   # enumerate x and create a continuous dimension for y
   # note the upper bound on y is lower than that of the descriptor to restrict the search domain
   x_dim = EnumeratedDimension(descriptor=x, values=['0', '5', '10'])
   y_dim = ContinuousDimension(descriptor=y, lower_bound=0, upper_bound=10)

   # create a design space from x and y dimensions
   design_space = ProductDesignSpace(
       name='2D coordinate system',
       description='Design space that contains (x, y) points',
       dimensions=[x_dim, y_dim]
   )

   # define a processor that will create a grid of 11 points over the y dimension
   # a grid size for x is not specified since it is already finite
   processor = GridProcessor(
       name='Grid processor',
       description='Creates a grid over y',
       grid_sizes={'y': 11}
   )

Monte Carlo processor
---------------------

A :class:`Monte Carlo processor <citrine.informatics.processors.MonteCarloProcessor>` uses Monte Carlo methods to explore the Design Space.
A Monte Carlo method involves a random walk in which steps that improve the score are always accepted, and steps that make the score worse are accepted probabilistically.
This balances exploitation, the desire to find the best nearby candidate, with exploration, the desire to investigate different regions of the Design Space.
Monte Carlo methods are flexible and broadly applicable, and especially useful for non-convex problems.
The Monte Carlo processor can be applied to any Design Space, although it is most useful for high-dimensional spaces that cannot easily be enumerated.

There are no parameters to configure when creating a Monte Carlo processor.
