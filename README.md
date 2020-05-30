# Wheel generator
This repo generates Python wheels given a list of packages.
It's useful if your Windows machine doesn't have the proper build tools installed.

## Which operating systems and Python versions are supported?
Currently, it only generates Windows 64 bits wheels for Python 3.6, 3.7 and 3.8, but it should be easy to extend to others.

## How to add a new package
Just add the desired package to `packages.txt`. Once your changes are pushed to this repo, it will automatically trigger a CI/CD pipeline in [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/).

## How to use the generated wheels
```
pip install --extra-index=https://pkgs.dev.azure.com/masdeseiscaracteres/python_packages/_packaging/artifacts/pypi/simple/ <package_name>
```


