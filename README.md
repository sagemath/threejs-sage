
# Custom build of Three.js for SageMath

This package provides a single minified Javascript file `three.min.js`, which combines
standard Three.js with a number of scripts from `examples/jsm/`.

The file is made available both as package data of a Python package `jupyter_threejs_sage` (for local access by SageMath) and as a Jupyter notebook extension (to be installed in the Jupyter notebook's Python environment).

# Development

The steps to create this build from a stable tagged version of Three.js are

* Perform a shallow clone of the desired version with

`git clone --depth=1 --branch r<n> --single-branch https://github.com/mrdoob/three.js.git`

* Add the following lines to `src/Three.js` just after all other exports

```
export { OrbitControls } from '../examples/jsm/controls/OrbitControls.js';
export { Line2 } from '../examples/jsm/lines/Line2.js';
export { LineGeometry } from '../examples/jsm/lines/LineGeometry.js';
export { LineMaterial } from '../examples/jsm/lines/LineMaterial.js';
export { LineSegments2 } from '../examples/jsm/lines/LineSegments2.js';
export { LineSegmentsGeometry } from '../examples/jsm/lines/LineSegmentsGeometry.js';
```

* Move into the library directory with `cd three.js`

* Configure the library with `npm install`

* Build the library with `npm run build`

  The minified file `three.min.js` will be located in the `build` directory.

* Copy the minified file to the `build` directory here.

* Create a new directory for the new version in `jupyter_threejs_sage/static/` and copy the minified file there.
  (Do not remove old versions that needed by any released versions of Sage.)

* The final step before releasing is to update the `version` file.


As noted in [this issue](https://github.com/mrdoob/three.js/issues/20591), Three.js releases can be modified for up to a week after the initial release. This build process should wait for this period of time to ensure future consistency of building.
