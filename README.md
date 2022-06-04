# jupyter_notebooks
examples

## useful shortcuts

 - `shift + enter` - run current cell; optionally you can use `▶ Run` button
 
 - `A` - create new cell above
 
 - `B` - create new cell below
 
 - `D-D` (double D) - delete current cell
 
 - `ctr-O` - clear cell output (Help -> Edit Keyboard Shortcuts -> clear cell output -> Ctrl-O)
 
 - `shift + tab` - function help box
 
## change python kernel

 - https://stackoverflow.com/questions/39007571/running-jupyter-with-multiple-python-and-ipython-paths

- list visibile kernels:

    `jupyter kernelspec list`

- install ipykernel package for specified python version:

    `python -m pip install ipykernel`

- install kernel for specified python:

    `python -m ipykernel install`

- list kernels again:

    `jupyter kernelspec list`

- if there is no kernel you installed:

    - https://stackoverflow.com/questions/42635310/remove-kernel-on-jupyter-notebook

    - remove conflict kernel(s) (with the same name):

        `jupyter kernelspec uninstall <unwanted-kernel>`

        example:

        `jupyter kernelspec uninstall python3`

     - install kernel for specified python version again:

        `python -m ipykernel install`

     - run jupyter notebook and choose installed kernel
