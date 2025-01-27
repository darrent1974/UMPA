# UMPA
This repository contains an improved, faster implementation of the "Unified Modulated Pattern Analysis" (UMPA) model, which is achieved through the use of C++ and Cython.
A publication describing and explaining this work can be found at

[F. De Marco, S. Savatović, R. Smith, V. Di Trapani, M. Margini, G. Lautizi, and P. Thibault, "High-speed processing of X-ray wavefront marking data with the Unified Modulated Pattern Analysis (UMPA) model," Opt. Express **31**, 635-650 (2023)](https://doi.org/10.1364/OE.474794).

**Please cite this work when using this version of UMPA!**

## Related work

 * This package is also used by an [**extension to directional dark-field**](https://github.com/optimato/UMPA_directional_dark_field). That work is described in the publication
[R.&nbsp;Smith, F.&nbsp;De&nbsp;Marco, L.&nbsp;Broche, M.-C.&nbsp;Zdora, N.&nbsp;W.&nbsp;Phillips, R.&nbsp;Boardman, and P.&nbsp;Thibault, "X-ray directional dark-field imaging using Unified Modulated Pattern Analysis," PLoS ONE **17**(8), e0273315 (2022)](https://doi.org/10.1371/journal.pone.0273315).

 * The original (Python-based) implementation of the method is available at https://github.com/pierrethibault/UMPA, and is also included in this repository, in the file [speckle_matching.py](https://github.com/optimato/UMPA/blob/main/UMPA/speckle_matching.py). The publication associated with that work is [M.-C.&nbsp;Zdora, P.&nbsp;Thibault, T.&nbsp;Zhou, F.&nbsp;J.&nbsp;Koch, J.&nbsp;Romell, S.&nbsp;Sala, A.&nbsp;Last, C.&nbsp;Rau, and I.&nbsp;Zanette, “X-ray Phase-Contrast Imaging and Metrology through Unified Modulated Pattern Analysis,” Phys. Rev. Lett., **118** 203903 (2017)](http://dx.doi.org/10.1103/PhysRevLett.118.203903).

## Local source innstallation instructions
In the current state, this repository is only compatible with Linux, and has only been tested with the `gcc` / `g++` compiler.

### Linux

```
pip install .
```


