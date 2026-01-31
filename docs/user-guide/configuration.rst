Configuration
=============

Learn how to configure ExtraBar to suit your needs.

Configuration File
------------------

ExtraBar looks for configuration in the following locations:

1. ``extrabar.config.js`` in your project root
2. ``.extrabarrc`` file
3. ``extrabar`` key in ``package.json``

Basic Options
-------------

.. code-block:: javascript

   module.exports = {
     // Project name
     name: 'my-project',

     // Enable verbose output
     verbose: true,

     // Output directory
     output: './dist',
   };

Environment Variables
---------------------

You can also configure ExtraBar using environment variables:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``EXTRABAR_DEBUG``
     - Enable debug mode
   * - ``EXTRABAR_CONFIG``
     - Path to config file
   * - ``EXTRABAR_OUTPUT``
     - Output directory

Advanced Configuration
----------------------

For complex setups, you can use a function:

.. code-block:: javascript

   module.exports = (env) => {
     return {
       name: 'my-project',
       output: env === 'production' ? './dist' : './dev',
     };
   };
