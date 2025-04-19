# 🌌 VISION 

This folder contains notebooks related to machine vision.

## 🧠 Contents

- `files.ipynb`: desc

## 🧪 Environment Setup via miniConda

I recommend creating a dedicated Conda environment for this module:

```bash
conda create -n vision python=3.12.9
conda activate vision
conda install jupyter matplotlib numpy ipywidgets sympy pandas ipympl
```

remember you can deactivate the environment again:
```bash
conda deactivate
```

or delete WARNING check the environtment-name i chose 'fractals-env':
```bash
conda remove -n vision --all
```

##Troubleshooting 
activation not working:
maybe you need to execute to enable scripts
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
