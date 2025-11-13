Before creating a python django app set virtual environment using 

python -m venv env

then activate the environment

env/Scripts/activate

then install django

pip install django


(env) PS D:\django-djongo-app> django-admin startproject storypost
(env) PS D:\django-djongo-app> cd storypost
(env) PS D:\django-djongo-app\storypost> django-admin startapp storyapp
(env) PS D:\django-djongo-app\storypost> 

change settings.py installed apps and dir in templates and create urls.py file in storyapp and import view there



from django.shortcuts import render again yellow underline under django.shortcutsThe yellow (or sometimes red) underline directly under django.shortcuts means:
VS Code cannot find the Django package on your system.
In other words: Django is not installed in the Python interpreter that VS Code is currently using.
Here’s how to fix it in 99% of cases (step-by-step):
Step 1: Open the integrated terminal in VS Code and install Django
bashpip install django
or, if you’re inside a virtual environment (highly recommended):
bashpython -m venv venv          # only the first time
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # macOS/Linux

pip install django
Step 2: Tell VS Code which Python interpreter to use (THIS IS THE MOST IMPORTANT PART)

Press Ctrl + Shift + P → type “Python: Select Interpreter” → press Enter
Choose the interpreter that is inside your project’s virtual environment, for example:text./venv/Scripts/python.exe          (Windows)
./venv/bin/python                  (macOS/Linux)or whichever Python you just used to run pip install django

You will instantly see the yellow underline disappear as soon as you select the correct interpreter (sometimes you need to reload the window: Ctrl + Shift + P → “Developer: Reload Window”).

(env) PS D:\django-djongo-app\storypost> python manage.py runserver



when first time pushing code to the new branch below cmd should be used

$ git push -u origin LekhDev