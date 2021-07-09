from setuptools import setup
import os

with open('version') as f:
    package_version_without_r = f.read()[1:]

versions = [ x for x in os.listdir('jupyter_threejs_sage/static') if x.startswith('r') ]

setup(
    version=package_version_without_r,
    data_files = [(
        f'share/jupyter/nbextensions/threejs-sage/{version}', [
            f'jupyter_threejs_sage/static/{version}/three.min.js'
        ]) for version in versions]
)
