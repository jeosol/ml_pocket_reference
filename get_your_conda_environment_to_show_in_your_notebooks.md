Method 1: “The Easy Way”
This is my preferred method because it is simple. New environments appear automatically (as long as they have ipykernel installed.)
g
To get your other environment kernels to show automatically:
1. First, install nb_conda_kernels in your base environment. Once this is installed any notebook running from the base environment will automatically show the kernel from any other environment which has ipykernel installed.
(base)$ conda install nb_conda_kernels
2. Next, create a new environment. I will call mine new-env. If you already have an environment you are trying to get to show on Jupyter Notebook, skip this step.
(base)$ conda create --name new-env
3. Activate the environment you want to use in your notebook and install iypkernel. My environment is called new-env. If you already have an environment substitute your environment nane for new-env
(base)$ conda activate new-env
(new-env)$ conda install ipykernel
4. Restart Jupyter Notebooks from your base environment and done. You can see here that all of my environments with ipykernel installed including new-env are showing. I can now switch between them at will. Bliss.


Method 2: “The Usual Way”
It is not that much harder to individually register each environment you want to show in your kernels list. If you have many environments this might be preferable because it allows you to register and un-register your environment kernels which could help keep that list tidy.
In your new environment install ipykernel
(new-env)$ conda install ipykernel
2. Register the kernel spec with Jupyter using the following command. The--name= argument will set the name you see in Jupyter Notebooks for this environment’s kernel (so you can call it whatever you want but using the environment’s name might be wise).
(new-env)$ipython kernel install --user --name=new-env
3. Now new-env will be displayed in your list of kernels (no need to restart Jupyter Notebook — just reload the page in your browser).

Image by author
4. When you want to un-register that kernel spec (remove the environment’s kernel from the list of available kernels) use the following command:
$jupyter kernelspec uninstall new-env

Method 3: “The Quick and Dirty Method”
This method doesn’t actually get your environment to show in Jupyter Notebooks, but it is worth noting. If you install jupyter in any environment and run jupyter notebook from that environment the notebook will use the kernel from the active environment. The kernel will show with the default name Python 3 but we can verify this works by doing the following.
Activate your environment, install jupyter, and run jupyer notebook.
(base)$ conda activate new-env
(new_env)$ conda install jupyter
(new_env)$ jupyter notebook
2. Run the following code in your notebook to confirm that you are using the correct kernel
import os
print (os.environ['CONDA_DEFAULT_ENV'])

Image by author

