from setuptools import setup
setup(data_files = [(
    # When trying to put this in setup.cfg,
    # the dash is replaced by underscore on installation?!
    'share/jupyter/nbextensions/threejs-sage/r122', [
        'jupyter_threejs_sage/static/r122/three.min.js'
    ])]
)
