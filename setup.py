from setuptools import setup

setup(
    name='helloworld-zacthewise',  # pip install
    version='0.0.1',
    description='Say hello!',
    py_modules=["helloworld"],  # import
    package_dir={'': 'src'},  # code is in src dir
)
