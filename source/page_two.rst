How to Write Documentation with reStructuredText
================================================

This guide will help you understand how to format and structure your documentation using **reStructuredText (RST)**. RST is the markup language used by Sphinx and other tools to generate clean and organized documentation.

For more details, refer to the official `reStructuredText documentation <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.

---

Headings
--------

reStructuredText supports multiple levels of headings. Here are a few examples:

* **Level 1 Heading** (with `=` symbols below the heading):

  .. code-block:: rst
    
    This is a Level 1 Heading
    =========================

  **Note:** The `=` symbols must be at least as long as the heading text.

* **Level 2 Heading** (with `-` symbols below the heading):

  .. code-block:: rst

    This is a Level 2 Heading
    -------------------------

  **Note:** The `-` symbols must be at least as long as the heading text.

* **Level 3 Heading** (with `~` symbols below the heading):

  .. code-block:: rst

    This is a Level 3 Heading
    ~~~~~~~~~~~~~~~~~~~~~~~~~

  **Note:** The `~` symbols must be at least as long as the heading text.

---

Text Formatting
---------------

* **Bold Text**: Use double asterisks `**` around the text.

  .. code-block:: rst

    **This is bold**

  **This is bold**

* *Italic Text*: Use single asterisks `*` around the text.

  .. code-block:: rst

    *This is italic*

  *This is italic*

* ``Monospace Text``: Use double backticks around code or filenames.

  .. code-block:: rst

    ``code_block.py``

  ``code_block.py``

* Hyperlinks: You can link to external URLs using this syntax:

  .. code-block:: rst

    `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

  `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

---

Blocks
------

There are different types of blocks to highlight important information:

.. code-block:: rst

    .. note::
        This is a note block. Use it to provide additional information.

.. note::
    This is a note block. Use it to provide additional information.

.. code-block:: rst

    .. warning::
        **Warning**: This is a warning block. Use it to alert the reader to something important!

.. warning::
    **Warning**: This is a warning block. Use it to alert the reader to something important!

.. code-block:: rst

    .. error::
        **Error**: This block is for highlighting errors or critical information.

.. error::
    **Error**: This block is for highlighting errors or critical information.

.. code-block:: rst

    .. tip::
        This is a tip block. Use it to provide helpful advice.

.. tip::
    This is a tip block. Use it to provide helpful advice.

.. code-block:: rst

    .. important::
        This is an important block. Use it to emphasize key points.

.. important::
    This is an important block. Use it to emphasize key points.

---

Custom Blocks
-------------

You can define your own custom blocks to present additional content with icons or visual markers.

.. code-block:: rst

  .. admonition:: Custom Block Title

      This is a custom block. Use it to highlight key sections of your documentation.

.. admonition:: Custom Block Title

    This is a custom block. Use it to highlight key sections of your documentation.

---

Toggle Button
-------------

You can create collapsible blocks using the toggle button for content that you don't want to reveal immediately.

.. code-block:: rst

  .. admonition:: This will be shown
    :class: hint

    .. toggle:: Click to expand

      This content will be hidden until the toggle is clicked. You can add more details here, such as code snippets, images, or additional explanations.


.. admonition:: Hint
  :class: hint

  .. toggle:: Click to expand

    This content will be hidden until the toggle is clicked. You can add more details here, such as code snippets, images, or additional explanations.

.. important::

  A new file called *custom.css* need to be added in *source/_static* with the following content:

  .. code-block:: bash
    
    .hint {
      border-color: var(--pst-color-success);
      > .admonition-title {
        &:before {
          background-color: var(--pst-color-success);
        }

        &:after {
          color: var(--pst-color-success);
          content: var(--pst-icon-admonition-hint);
        }
      }
    }

  The *conf.py* need to be updated with ``html_css_files = ['custom.css']``. 


---

Tables
------

You can create tables in reStructuredText using two common formats:

1. **Grid Tables**

   .. code-block:: rst

      +------------------------+------------+----------+
      | Header row, column 1   | Header 2   | Header 3 |
      +========================+============+==========+
      | body row 1, column 1   | column 2   | column 3 |
      +------------------------+------------+----------+
      | body row 2             | Cells may span        |
      +------------------------+-----------------------+

  +------------------------+------------+----------+
  | Header row, column 1   | Header 2   | Header 3 |
  +========================+============+==========+
  | body row 1, column 1   | column 2   | column 3 |
  +------------------------+------------+----------+
  | body row 2             | Cells may span        |
  +------------------------+-----------------------+

2. **Simple Tables**

   .. code-block:: rst

      ====================  ==========  ==========
      Header row, column 1  Header 2    Header 3
      ====================  ==========  ==========
      body row 1, column 1  column 2    column 3
      body row 2            Cells may span columns
      ====================  ======================

  ====================  ==========  ==========
  Header row, column 1  Header 2    Header 3
  ====================  ==========  ==========
  body row 1, column 1  column 2    column 3
  body row 2            Cells may span columns
  ====================  ======================

---

Lists
-----

reStructuredText supports different types of lists, including:

1. **Unordered Lists:**

   .. code-block:: rst

      * This is an item
      * This is another item
      
        * Nested item
        * Another nested item

   * This is an item
   * This is another item

    * Nested item
    * Another nested item

2. **Ordered Lists:**

   .. code-block:: rst

      1. First item
      2. Second item

        1. Nested item
        2. Another nested item

   1. First item
   2. Second item

    1. Nested item
    2. Another nested item

---

Figures and Images
------------------

You can include figures or images in your documentation using the following syntax:

.. code-block:: rst

    .. figure:: /path/to/image.png
       :align: center
       :width: 90%
       :alt: Image description

       This is an example of a figure with a caption.

.. figure:: /images/image1.jpg
    :align: center
    :width: 90%
    :alt: Image description

    This is an example of a figure with a caption.

For regular images without a caption, use the `image` directive:

.. code-block:: rst

    .. image:: /path/to/image.png
       :align: center
       :alt: Example image

.. image:: /images/image2.jpg
    :align: center
    :alt: Example image

---


Code Blocks
-----------

To include code snippets, use the `code-block` directive:

.. code-block:: rst

  .. code-block:: python

      def hello_world():
          print("Hello, Sphinx!")

.. code-block:: python

    def hello_world():
        print("Hello, Sphinx!")

For bash commands, specify the language as `bash`:

.. code-block:: rst

  .. code-block:: bash

      echo "Hello, Sphinx"

.. code-block:: bash

    echo "Hello, Sphinx"

---

Tabs
----

You can organize content into tabs using the `tab` directive from the Sphinx tabs extension:

.. code-block:: rst

  .. tabs::

      .. tab:: Python

          .. code-block:: python

              def example():
                  return "Python code block"

      .. tab:: Bash

          .. code-block:: bash

              echo "This is a Bash code block"

.. tabs::

    .. tab:: Python

        .. code-block:: python

            def example():
                return "Python code block"

    .. tab:: Bash

        .. code-block:: bash

            echo "This is a Bash code block"

---

Tips and Best Practices
-----------------------

* Use **RST** consistently to maintain clean documentation structure.
* Take advantage of Sphinx extensions for advanced formatting and functionality.
* Keep sections modular for easy navigation and readability.