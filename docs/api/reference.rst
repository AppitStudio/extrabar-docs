API Reference
=============

Complete API documentation for ExtraBar.

Core API
--------

init()
~~~~~~

Initialize a new ExtraBar instance.

**Parameters:**

- ``options`` (Object) - Configuration options

**Returns:** ExtraBar instance

**Example:**

.. code-block:: javascript

   const bar = extrabar.init({
     name: 'my-project'
   });

create()
~~~~~~~~

Create a new project.

**Parameters:**

- ``name`` (String) - Project name
- ``options`` (Object, optional) - Creation options

**Returns:** Project object

**Example:**

.. code-block:: javascript

   const project = extrabar.create('my-project', {
     template: 'default'
   });

run()
~~~~~

Execute ExtraBar with the given configuration.

**Parameters:**

- ``config`` (Object) - Runtime configuration

**Returns:** Promise<Result>

Events
------

ExtraBar emits events during execution:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Event
     - Description
   * - ``start``
     - Emitted when execution begins
   * - ``progress``
     - Emitted during processing
   * - ``complete``
     - Emitted when execution finishes
   * - ``error``
     - Emitted on errors

Types
-----

Configuration Object
~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   interface ExtraBarConfig {
     name: string;
     verbose?: boolean;
     output?: string;
     options?: Record<string, any>;
   }
