# Windows wheel generator
This repo generates Windows wheels for the specified Python packages.
It's useful if your Windows machine doesn't have the proper build tools installed.

## How to add a new package
Just add the desired package to `packages.txt`. Once pushed, it will automatically trigger a CI/CD pipeline in [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/).

## How to use the generated wheels
```
pip install --extra-index=https://pkgs.dev.azure.com/masdeseiscaracteres/python_packages/_packaging/artifacts/pypi/simple/ <package_name>
```


