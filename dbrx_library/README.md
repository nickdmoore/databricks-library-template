# README

This is a minimal template for building a packaged Python library to deploy and use within Databricks notebooks.

## Build
```
python3 setup.py bdist_wheel
```

## Install (Local)
```
pip3 install ./dist/dbrx_library-x.x.x-py3-none-any.whl
```

## Install (Databricks)

### Via Databricks `dbutils` api
```
dbutils.library.installPyPI("dbrx_library", repo="https://your.artifact.feed/dbrx_library")
```

### Via pip in shell
```
%sh
sudo apt install -y python3-pip
python3 -m pip install --upgrade pip
pip3 install --force dbrx_library --extra-index-url https://your.artifact.feed/dbrx_library
```
