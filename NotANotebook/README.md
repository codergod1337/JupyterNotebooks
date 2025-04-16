# 🌌 Not A Jupyter Notebook

This folder contains projects which are no Jupyter Notebooks.

## 🧠 Contents

- `test.py`: lets test

## 🧪 Environment Setup via miniConda

I recommend creating a dedicated Conda environment for this module:

```bash
conda create -n thomas python=3.12.9
conda activate thomas
conda install ipython matplotlib numpy rich sympy pandas
```
to activate in VS Code press ctrl + shift + p and select correct environment!

remember you can deactivate the environment again:
```bash
conda deactivate
```

or delete WARNING check the environtment-name i chose 'thomas':
```bash
conda remove -n thomas --all
```

##Troubleshooting 
activation not working:
maybe you need to execute to enable scripts
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
