To get your other environment kernels to show automatically:
1. First, install nb_conda_kernels in your base environment. Once this is installed any notebook running from the base environment will automatically show the kernel from any other environment which has ipykernel installed.
(base)$ conda install nb_conda_kernels
2. Next, create a new environment. I will call mine new-env. If you already have an environment you are trying to get to show on Jupyter Notebook, skip this step.
(base)$ conda create --name new-env
3. Activate the environment you want to use in your notebook and install iypkernel. My environment is called new-env. If you already have an environment substitute your environment nane for new-env
(base)$ conda activate new-env
(new-env)$ conda install ipykernel
4. Restart Jupyter Notebooks from your base environment and done. You can see here that all of my environments with ipykernel installed including new-env are showing. I can now switch between them at will. Bliss.
