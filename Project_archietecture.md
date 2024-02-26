## Steps:

1) Create a new env 
    - conda create -p venv python==3.10 -y
2) Create a project archietecture
    - src
        - __init__.py
        - utils.py
        - mcqgenerator.py
        - logger.py
    - experiment
        - __init__.py
        - experiment.ipynb
    - setup.py
    - requirements.txt
    - README.md
    - .env
 
Here is the explanation for each file

Let's break down each file and its purpose in the project architecture:

1. **src/**:
    - This directory typically contains the source code of your project.
    - **\_\_init\_\_.py**: This file is required to make Python treat the directories as containing packages. It can be empty or can contain initialization code for the package.
    - **utils.py**: This file typically contains utility functions or helper functions that are used across your project. These functions can help in various tasks like data manipulation, file handling, or any other common operation.
    - **mcqgenerator.py**: Assuming this generates multiple-choice questions, this file would contain the code responsible for generating MCQs. It could contain functions/classes related to question generation, formatting, and any other logic specific to MCQ generation.
    - **logger.py**: This file contains code related to logging. Logging is essential for tracking the behavior of your application, debugging, and monitoring. It could define a logger class or setup logging configurations.
    - **exceptions.py**: This file contains custom exception classes. These are used to handle specific errors or exceptional cases within your code in a more organized manner.

2. **experiment/**:
    - This directory seems to contain an experiment notebook, which is often used for exploring data, testing out algorithms, or documenting your experimentation process.
    - **experiment.ipynb**: This is a Jupyter notebook file (.ipynb extension) where you can write and execute code, add explanatory text, and visualize data. It's commonly used for data analysis, machine learning experiments, or documenting step-by-step procedures.

3. **setup.py**:
    - This file is used for specifying the metadata about your Python package and the dependencies required to run it. It's essential for packaging and distribution purposes. It typically includes information like the package name, version, author, dependencies, etc.

4. **requirements.txt**:
    - This file lists all the Python packages that your project depends on. It's useful for managing dependencies, ensuring that anyone who wants to run your code can install all the required packages with a single command (`pip install -r requirements.txt`).

5. **README.md**:
    - This file contains information about your project, including what it does, how to install it, how to use it, and any other relevant details. It serves as documentation for your project and helps users and developers understand it better.

6. 5. **.env**:
    - In this file we store our variable in the system and can keep them hidden. Also, it helps to transport the file to other people and help them to access the values of variables stored in the system.

Each of these files serves a specific purpose in organizing, documenting, and managing your project, which is crucial for effective software development and collaboration.

3) Write all the important packages in the requirements.txt
    - **Important** = Write "- e." in requirements file

In a `requirements.txt` file, the `-e` flag is used to specify that you want to install a package in "editable" mode. This mode is often used during development when you're actively working on a package and want changes to be immediately reflected without having to reinstall the package each time.

Here's what the `-e` flag does:

- **Editable mode (`-e`)**: When you specify a package with the `-e` flag in the `requirements.txt` file, it means that you want to install the package in editable mode. In editable mode, instead of copying the package's files into the Python environment's site-packages directory, a symbolic link (or symlink) is created instead. This symlink points directly to the source code directory of the package. As a result, any changes made to the source code are immediately reflected when you import the package in your code, without needing to reinstall the package.

For example, let's say you have a package named `mypackage`, and you want to install it in editable mode using `requirements.txt`. You would write it like this:

```
-e ./path/to/mypackage
```

This tells `pip` to install `mypackage` from the specified path in editable mode.

Using editable mode can be convenient during development because it allows you to make changes to your package's source code and immediately see the effects without needing to reinstall the package each time. However, it's important to note that this mode is primarily intended for development purposes and shouldn't be used in production environments.

4) Write setup.py file
