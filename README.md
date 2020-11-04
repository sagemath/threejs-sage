
# Custom build of Three.js for SageMath

The steps to create this build from a stable tagged version are

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

The minified file will be located in the `build` directory and has been copied to the same directory here. The final step before releasing is to update the `version` file with the new number.

As noted in [this issue](https://github.com/mrdoob/three.js/issues/20591), Three.js releases can be modified for up to a week after the initial release. This build process should wait for this period of time to ensure future consistency of building.
