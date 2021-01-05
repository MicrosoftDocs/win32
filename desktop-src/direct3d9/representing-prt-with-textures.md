---
description: The PRTDemo sample and PRTCmdLine simulator included in the DirectX SDK represent transfer vectors at the vertices of a mesh.
ms.assetid: cee049e8-3245-4fce-ab2f-ba251eacc72a
title: Representing PRT With Textures (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Representing PRT With Textures (Direct3D 9)

The PRTDemo sample and PRTCmdLine simulator included in the DirectX SDK represent transfer vectors at the vertices of a mesh. In order to represent the PRT signal accurately, this can require tessellations that may be impractical for current games. Representing transfer vectors in texture maps is an alternative approach that has the same data cost independent of mesh complexity. There are several ways to generate transfer vector texture maps using the D3DX PRT Library.

## Precomputing Transfer Vectors

One approach would be to modify the PRTDemo and PRTCmdLine samples to compute a transfer vector at every texel in a parameterization of a surface. To do this:

1.  Modify the call to [**D3DXCreatePRTEngine**](d3dxcreateprtengine.md) to extract texture coordinates from the mesh (ExtractUVs must be **TRUE**)
2.  Replace [**D3DXCreatePRTBuffer**](d3dxcreateprtbuffer.md) calls with [**D3DXCreatePRTBufferTex**](d3dxcreateprtbuffertex.md) using the same texture size.

All ID3DXPRTEngine methods work with per-texel simulations except for: ComputeBounceAdaptive, ComputeSSAdaptive, ComputeSS, and ComputeDirectLightingSHAdaptive. While texture-space simulation will generate the correct result, it can often be fairly slow since it will most likely be computing transfer vectors at a high density.

Another approach is to compute an adaptive per-vertex PRT simulation (with texture coordinates that will be used for the per-texel data) and then call [**ID3DXPRTEngine::ResampleBuffer**](id3dxprtengine--resamplebuffer.md) (using an output buffer created using [**D3DXCreatePRTBufferTex**](d3dxcreateprtbuffertex.md) at the appropriate resolution). This works with all D3DX PRT functionality in the SDK and can often be much more efficient than directly computing a per-texel transfer buffer.

## Runtime Calculations

If a single cluster is used the results can be filtered and mip-mapped like any other texture and the pixel shader is identical to the vertex shader code that ships with PRTDemo.

If compression generates multiple clusters, you cannot filter or mipmap the data because clustering indexes are not continuous. Here are some alternatives for handling multi-clustered data:

-   Do all of the filtering yourself in the pixel shader. Unfortunately, this is generally impractical for performance reasons.
-   If the textures are low resolution non mip-mapped textures (ie: light maps), it is most likely more efficient to just compute the lighting directly in texture space - where no filtering will occur, and render the object with a shaded texture. This is essentially a dynamic light map that is created entirely on the GPU.
-   If a texture atlas is used (see [Using UVAtlas (Direct3D 9)](using-uvatlas.md)), you could manually cluster the scene by having all transfer vectors in a connected component in texture space be in the same cluster. This way you can filter the texture because all texels accessed would be in the same cluster by construction. The cluster ID for a given face could be propagated from the vertex shader.

Pixel shaders have much fewer constant registers that cannot be indexed, so the pixel shader is somewhat different than the vertex shader. Storing the per-cluster work in a low resolution dynamic texture and using texture loads would be the most efficient way to render when using multiple clusters.

## Related topics

<dl> <dt>

[Precomputed Radiance Transfer](precomputed-radiance-transfer.md)
</dt> <dt>

[PRT Demo Sample](https://msdn.microsoft.com/library/Ee418763(v=VS.85).aspx)
</dt> <dt>

[PRT Simulator (prtcmdline.exe)](https://msdn.microsoft.com/library/Ee418766(v=VS.85).aspx)
</dt> </dl>

 

 



