Deploying to Read the Docs
==========================

To publish your documentation on Read the Docs, follow these steps to complete the setup:

1. **Add a `.readthedocs.yaml` File**

   Create a `.readthedocs.yaml` file in the root of your project directory (not in the `source` folder). This file specifies the build environment and configuration for Read the Docs.

   .. code-block:: yaml

      version: "2"

      build:
        os: "ubuntu-22.04"
        tools:
          python: "3.10"

      python:
        install:
          - requirements: requirements.txt

      sphinx:
        configuration: source/conf.py

      # formats:
      #   - pdf

2. **Create a `requirements.txt` File**

   In the root directory, add a `requirements.txt` file to define the dependencies for your project.

   .. code-block:: bash

      sphinx-rtd-theme==2.0.0
      sphinx-copybutton==0.5.2
      sphinx-code-tabs==0.5.5
      sphinx-new-tab-link==0.6.1
      sphinx-togglebutton==0.3.2

3. **Push Your Changes to GitHub**

   Commit and push all your changes to GitHub:

   .. code-block:: bash

      cd <your-cloned-repository>
      git status
      git add .
      git status
      git commit -m "Add Read the Docs configuration"
      git push

4. **Login to Read the Docs**

   Sign in to Read the Docs using your GitHub account at [Read the Docs Login](https://readthedocs.org/accounts/login/).

5. **Import Your Project**

   Click ``Import a Project`` and select your GitHub repository from the list.

6. **Configure Your Project**

   Adjust any necessary settings for your project, but you can leave most settings at their default values.

7. **Build Your Documentation**

   After importing, go to the ``Builds`` section of your project on Read the Docs. If everything is configured correctly, the build process should complete without errors.

8. **View Your Documentation**

   Once the build is successful, click on ``View Docs`` to see your masterpiece come to life. Share the URL from the Overview tab with your friends, colleagues, or anyone who’ll appreciate your documentation brilliance. Feel free to brag a little — after all, you’ve earned it!

Congratulations, you've successfully deployed your documentation to Read the Docs!
