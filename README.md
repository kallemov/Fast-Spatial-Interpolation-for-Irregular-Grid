## Fast-Spatial-Interpolation-for-Irregular-Grid

This is C library for bilinear (biquadratic) interpolation for the scattered points (irregular grid) based on this discussion https://math.stackexchange.com/questions/828392/spatial-interpolation-for-irregular-grid

![](images/theory.jpeg)

This library was used to only create an interpolation stencil in Watershed project, so there is no standard api at the moment.

I provided an interface for python linking a C library and create a demostration

To create a shared C lib:

```
 gcc -fPIC -O3 -shared -o bilinear.so bilinear.cpp
 ```

To get animation:

```
python test.py
```
![](images/output.gif)
