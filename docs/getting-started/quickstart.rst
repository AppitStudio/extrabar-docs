Quick Start
===========

This guide will get you up and running with ExtraBar in minutes.

Basic Setup
-----------

1. Open your terminal
2. Navigate to your project directory
3. Initialize ExtraBar:

.. code-block:: bash

   extrabar init

Your First Project
------------------

Let's create a simple example:

.. code-block:: bash

   extrabar create my-project
   cd my-project
   extrabar start

Configuration
-------------

ExtraBar uses a configuration file. Create ``extrabar.config.js``:

.. code-block:: javascript

   module.exports = {
     name: 'my-project',
     options: {
       // your options here
     }
   };

What's Next?
------------

- Learn about :doc:`/user-guide/features`
- Explore :doc:`/user-guide/configuration`
- Check the :doc:`/api/reference`
