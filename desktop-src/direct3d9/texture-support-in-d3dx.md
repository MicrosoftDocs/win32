---
description: Learn about texture support in D3DX. D3DX is a utility library that provides helper services. It is a layer above the Direct3D component.
ms.assetid: 84815851-ca96-47ab-9f84-56ecaeb4a6d9
title: Texture Support in D3DX (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Texture Support in D3DX (Direct3D 9)

D3DX is a utility library that provides helper services. It is a layer above the Direct3D component.

## Textures

Many different textures are supported in the following topics.

-   Standard mipmapped texture support. See [Automatic Generation of Mipmaps (Direct3D 9)](automatic-generation-of-mipmaps.md).
-   Cube map support. See [Cubic Environment Mapping (Direct3D 9)](cubic-environment-mapping.md).
-   Volume texture support. See [Volume Texture Resources (Direct3D 9)](volume-texture-resources.md).
-   Environment mapping support. See [Environment Mapping (Direct3D 9)](environment-mapping.md).
-   Bump mapping support. See [Bump Mapping (Direct3D 9)](bump-mapping.md).

### Texture Color Conversion

When using any of the D3DXLoadSurfacexxx, D3DXLoadVolumexxx, D3DXCreateTexturexxx, D3DXCreateCubeTexturexxx, or D3DXCreateVolumeTexturexxx functions, color conversion might need to be performed. For example, one surface might be type RGBA and the other might be UVWQ. For cases of dissimilar formats, the conversion sequence is as follows:

### Mapping RGBA to UVWQ

-   R <-> U, R channel is mapped to the U channel, or vice versa.
-   G <-> V, G channel is mapped to the V channel, or vice versa.
-   B <-> W, B channel is mapped to the W channel, or vice versa.
-   A <-> Q/L, A channel is mapped to either the Q or the L channel (depending on which one is available in the destination format), or vice versa.


```
R->U
G->V
B->W
A->Q or A->L
```



### Mapping UV to RGBA

-   U <-> R, U channel is mapped to the R channel, or vice versa.
-   V <-> G, V channel is mapped to the G channel, or vice versa.
-   1 <-> B, 1 is mapped to the B channel, or vice versa.
-   1 <-> A, 1 is mapped to the A channel, or vice versa.

If a channel does not exist in the source, it is assumed to be 1 (with the exception of A8, where R,G,B are assumed to be 0). For example:


```
U -> R
V -> G
1 -> B
1 -> A
```



## Related topics

<dl> <dt>

[D3DX](d3dx.md)
</dt> </dl>

 

 



