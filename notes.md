Adding An Environment to Jupyter Notipyonebooks
FEBRUARY 1, 2019 ECHRIS CODE SNIPPETS
This is a code snippet to allow you to use a Python environment within a Jupyter Notebook on Windows.

conda create -n newenv python=3.7
activate newenv 
conda install -c anaconda ipykernel
ipython kernel install --user --name=envname
ipython kernet install --user --name=ml_pocket_reference
Now let’s break it down into steps.

Step 1: Create your environment
Using conda in your terminal, type:

conda create -n newenv python=3.7
newenv is the name of your new environment.

Step 2: Activate your environment
In the terminal:

activate newenv
Step 3: Install ipykernel
In the active environment, type:

pip install ipykernel
Or if you want to use conda:

conda install -c anaconda ipykernel
Step 4: Install the new kernel
In the active environment, type:

ipython kernel install --user --name=envname
envname can be anything, but I recommend using the same name as the environment so that it does not get too confusing.

Step 5: Open Jupyter Notebook / Lab
You should now see the new environment when you open Jupyter. With notebooks, you can select it as a kernel when you create a new notebook. In Lab, you should see it listed as a notebook option on your Launcher.

Removing an Environment from Jupyter
To remove an environment from Jupyter, simply run the following code:

jupyter kernelspec uninstall envname

To create a file with the package requirements in it, run:
conda env export > environment.yml

To install these requirements in a new environment, run:
conda create -f environment.yml


To activate the environment for the book
conda activate ml_pocket_reference


TO install yellowbricks
conda install -c districtdatalabs yellowbrick


