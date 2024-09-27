Setting Up Sphinx
=================

In this section, we'll guide you through the process of setting up a Sphinx documentation project from scratch. You will learn how to create a GitHub repository, set up a virtual environment, install Sphinx and its extensions, and configure your project. Follow these steps to get your documentation project up and running.

1. **Create a Public GitHub Repository**

    First, create a new public repository on GitHub to host your Sphinx documentation project.

2. **Clone the Repository Locally**

    Clone the newly created repository to your local machine using the following command:

    .. code-block:: bash

        git clone <your-repository-url>

3. **Set Up a Virtual Environment**

    Move into the cloned repository folder:

    .. code-block:: bash

        cd <your-cloned-repository>

    Then set up a virtual environment using either `venv` or `virtualenv`, adapting the command based on your Python version:

    - To use `venv` (included in the Python standard library):

    .. code-block:: bash

        python3 -m venv env

    - To use `virtualenv` (requires separate installation):

    .. code-block:: bash

        python3.10 -m virtualenv env


4. **Activate the Virtual Environment**

    Activate the virtual environment to isolate your project's dependencies:

    .. code-block:: bash

        source env/bin/activate

5. **Install Sphinx**

    Install Sphinx within your virtual environment:

    .. code-block:: bash

        pip install sphinx

6. **Install Additional Extensions**

    Enhance your Sphinx setup with useful extensions:

    .. code-block:: bash

        pip install sphinx_rtd_theme sphinx-copybutton sphinx_code_tabs

7. **Create Sphinx Documentation**

    Initialize your Sphinx documentation project:

    .. code-block:: bash

        sphinx-quickstart

    .. tip::
        It's a good practice to separate source and build directories to keep everything organized.

8. **Open the Project in Visual Studio Code**

    Launch Visual Studio Code in the project directory:

    .. code-block:: bash

        code .

9. **Activate the Virtual Environment in VS Code**

    Open a terminal in VS Code and activate your virtual environment:

    .. code-block:: bash

        source env/bin/activate

10. **Generate HTML Documentation**

    Build the HTML documentation to see the output:

    .. code-block:: bash

        make html 

    .. note::
        The generated `index.html` file will be located in the `build/html` directory.

    .. warning::
        To preview the latest version of the HTML page, remember to refresh your browser. If changes do not appear, first ensure that the build succeeded without errors. If the build is successful but changes are still not visible, try running the following commands:

        .. code-block:: bash

            make clean
            make html

        Then, open the new `index.html` file in the `build/html` directory to check the updated documentation.

11. **Add Extensions to `conf.py`**

    Edit the `conf.py` file to include the extensions you installed:

    .. code-block:: python

        extensions = ['sphinx_rtd_theme', 'sphinx_copybutton', 'sphinx_code_tabs']

12. **Change the Theme**

    Set the theme for your documentation in `conf.py`:

    .. code-block:: python

        html_theme = 'sphinx_rtd_theme'

13. **Configure Theme Options**

    Customize the theme options in `conf.py`:

    .. code-block:: python

        html_theme_options = {
            'logo_only': False,
            'collapse_navigation': True,
            'sticky_navigation': True,
            'includehidden': True,
            'navigation_depth': 4,
            'titles_only': False
        }

14. **Add a New Page**

    a. Create a new `.rst` file for your page in the `source` directory:

    .. code-block:: bash

        touch source/new_page.rst

    b. Add content to `new_page.rst`, starting with a title:

    .. code-block:: rst

        New Page Title
        ==============

        New Page Subtitle
        -----------------

    c. Update the `toctree` directive in `index.rst` to include your new page:

    .. code-block:: rst

        .. toctree::
            :maxdepth: 2
            :caption: Contents

            new_page.rst