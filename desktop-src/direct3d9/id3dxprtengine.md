---
description: The ID3DXPRTEngine interface is used to compute a precomputed radiance transfer (PRT) simulation. Its methods are typically used offline, to compute per-vertex or per-texel transfer vectors in advance of real-time 3D modeling.
ms.assetid: d5be657f-2b0c-48fd-a7f0-ddb90107772f
title: ID3DXPRTEngine interface (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPRTEngine
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPRTEngine interface

The ID3DXPRTEngine interface is used to compute a precomputed radiance transfer (PRT) simulation. Its methods are typically used offline, to compute per-vertex or per-texel transfer vectors in advance of real-time 3D modeling.

## Members

The **ID3DXPRTEngine** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXPRTEngine** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXPRTEngine** interface has these methods.



| Method                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClosestRayIntersects**](id3dxprtengine--closestrayintersects.md)                       | Uses efficient ray-tracing in precomputed radiance transfer (PRT) simulations to determine whether a ray intersects a mesh. If an intersection is found, the method returns the index of the closest mesh face hit by the ray and the barycentric coordinates of the intersection point.<br/>                                                                                                                                                                                |
| [**ComputeBounce**](id3dxprtengine--computebounce.md)                                     | Computes the source radiance resulting from a single bounce of interreflected light. This method can be used for any lit scene, including a spherical harmonic (SH)-based precomputed radiance transfer (PRT) model.<br/>                                                                                                                                                                                                                                                    |
| [**ComputeBounceAdaptive**](id3dxprtengine--computebounceadaptive.md)                     | Computes the source radiance resulting from a single bounce of interreflected light, using adaptive sampling. This method generates new vertices and faces on the mesh to more accurately approximate the precomputed radiance transfer (PRT) signal. This method can be used for any lit scene, including a spherical harmonic (SH)-based PRT model.<br/>                                                                                                                   |
| [**ComputeDirectLightingSH**](id3dxprtengine--computedirectlightingsh.md)                 | Computes the direct lighting contribution to 3D objects where the source radiance is represented by a spherical harmonic (SH) approximation.<br/>                                                                                                                                                                                                                                                                                                                            |
| [**ComputeDirectLightingSHAdaptive**](id3dxprtengine--computedirectlightingshadaptive.md) | Computes the direct lighting contribution to 3D objects where the source radiance is represented by a spherical harmonic (SH) approximation, using adaptive sampling. This method generates new vertices and faces on the mesh to more accurately approximate the precomputed radiance transfer (PRT) signal.<br/>                                                                                                                                                           |
| [**ComputeDirectLightingSHGPU**](id3dxprtengine--computedirectlightingshgpu.md)           | Uses the GPU to compute the direct lighting contribution to 3D objects where the source radiance is represented by a spherical harmonic (SH) approximation. Computing the lighting on the GPU will generally be much faster than on the CPU.<br/>                                                                                                                                                                                                                            |
| [**ComputeLDPRTCoeffs**](id3dxprtengine--computeldprtcoeffs.md)                           | Computes locally-deformable precomputed radiance transfer (LDPRT) coefficients relative to per-sample normal vectors to minimize the least-squares error with respect to input [**ID3DXPRTBuffer**](id3dxprtbuffer.md) data. These coefficients can be used with skinned or transformed normal vectors to model global effects on dynamic objects.<br/>                                                                                                                     |
| [**ComputeSS**](id3dxprtengine--computess.md)                                             | Computes the source radiance resulting from subsurface scattering, using material properties set by [**ID3DXPRTEngine::SetMeshMaterials**](id3dxprtengine--setmeshmaterials.md). This method can be used only for materials defined per-vertex in a mesh object.<br/>                                                                                                                                                                                                       |
| [**ComputeSSAdaptive**](id3dxprtengine--computessadaptive.md)                             | Computes a transfer vector that maps source radiance to exit radiance resulting from subsurface scattering, using adaptive sampling and material properties set by [**ID3DXPRTEngine::SetMeshMaterials**](id3dxprtengine--setmeshmaterials.md). The method generates new vertices and faces on the mesh to more accurately approximate the precomputed radiance transfer (PRT) signal. This method can be used only for materials defined per-vertex in a mesh object.<br/> |
| [**ComputeSurfSamplesBounce**](id3dxprtengine--computesurfsamplesbounce.md)               | Computes precomputed radiance transfer (PRT) samples for an arbitrary point (and normal vector).<br/>                                                                                                                                                                                                                                                                                                                                                                        |
| [**ComputeSurfSamplesDirectSH**](id3dxprtengine--computesurfsamplesdirectsh.md)           | Computes, at an arbitrary point not on a mesh, a transfer vector that maps source radiance (represented by a spherical harmonic (SH) approximation) to exit radiance.<br/>                                                                                                                                                                                                                                                                                                   |
| [**ComputeVolumeSamples**](id3dxprtengine--computevolumesamples.md)                       | Computes a projection of the direct lighting from the previous light bounce into spherical harmonic (SH) basis vectors that represent incident radiance at specified locations.<br/>                                                                                                                                                                                                                                                                                         |
| [**ComputeVolumeSamplesDirectSH**](id3dxprtengine--computevolumesamplesdirectsh.md)       | Computes a projection of distant lighting into spherical harmonic (SH) basis vectors that represent incident radiance at specified locations.<br/>                                                                                                                                                                                                                                                                                                                           |
| [**ExtractPerVertexAlbedo**](id3dxprtengine--extractpervertexalbedo.md)                   | Copies per-vertex albedo values from a mesh.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**FreeBounceData**](id3dxprtengine--freebouncedata.md)                                   | Frees memory used for temporary bounced-light simulation data.<br/>                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**FreeSSData**](id3dxprtengine--freessdata.md)                                           | Frees memory used for temporary subsurface light scattering simulation data.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| [**GetAdaptedMesh**](id3dxprtengine--getadaptedmesh.md)                                   | Returns a mesh with modifications resulting from adaptive spatial sampling. The returned mesh contains only positions, normals, and texture coordinates (if defined).<br/>                                                                                                                                                                                                                                                                                                   |
| [**GetNumFaces**](id3dxprtengine--getnumfaces.md)                                         | Retrieves the number of faces in the mesh, including any new faces added as a result of adaptive spatial sampling.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| [**GetNumVerts**](id3dxprtengine--getnumverts.md)                                         | Retrieves the number of vertices in the mesh, including any new vertices added as a result of adaptive spatial sampling.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [**GetVertexAlbedo**](id3dxprtengine--getvertexalbedo.md)                                 | Retrieves albedo values of the mesh vertices.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**MultiplyAlbedo**](id3dxprtengine--multiplyalbedo.md)                                   | Multiplies each precomputed radiance transfer (PRT) vector by the per-vertex albedo.<br/>                                                                                                                                                                                                                                                                                                                                                                                    |
| [**ResampleBuffer**](id3dxprtengine--resamplebuffer.md)                                   | Resamples an input [**ID3DXPRTBuffer**](id3dxprtbuffer.md) buffer and saves it to an output buffer. This method can be used to convert a vertex buffer to a texture buffer and vice-versa. It can also be used to convert single-channel buffers to 3-channel buffers and vice-versa.<br/>                                                                                                                                                                                  |
| [**RobustMeshRefine**](id3dxprtengine--robustmeshrefine.md)                               | Subdivides faces on a mesh, allowing for conservative adaptive sampling that will not eliminate features on the mesh.<br/>                                                                                                                                                                                                                                                                                                                                                   |
| [**ScaleMeshChunk**](id3dxprtengine--scalemeshchunk.md)                                   | Scales all the samples associated with a given submesh. The method is useful for computing subsurface scattering.<br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**SetCallBack**](id3dxprtengine--setcallback.md)                                         | Sets a pointer to an optional callback function that computes the percentage of spherical harmonic (SH) computations completed and gives the caller the option of aborting the simulator.<br/>                                                                                                                                                                                                                                                                               |
| [**SetMeshMaterials**](id3dxprtengine--setmeshmaterials.md)                               | Sets mesh material properties in the 3D scene. Use this method to specify subsurface scattering parameters.<br/>                                                                                                                                                                                                                                                                                                                                                             |
| [**SetMinMaxIntersection**](id3dxprtengine--setminmaxintersection.md)                     | Sets the minimum and maximum distances of intersection between 3D objects. These distance values can be used to control the minimum or maximum distance that objects can shadow or reflect light. For example, the method can be used to limit the shadowing of nearby features of a 3D model.<br/>                                                                                                                                                                          |
| [**SetPerTexelAlbedo**](id3dxprtengine--setpertexelalbedo.md)                             | Sets an albedo value for each texel, overwriting previous albedo values.<br/>                                                                                                                                                                                                                                                                                                                                                                                                |
| [**SetPerTexelNormal**](id3dxprtengine--setpertexelnormal.md)                             | Sets a normal vector for each texel in a texture object. This method is used to store vertex normal vectors from a mesh (or interpolated vertex normals if pixel-based precomputed radiance transfer (PRT) is being computed).<br/>                                                                                                                                                                                                                                          |
| [**SetPerVertexAlbedo**](id3dxprtengine--setpervertexalbedo.md)                           | Sets an albedo value for each mesh vertex, overwriting previous albedo values.<br/>                                                                                                                                                                                                                                                                                                                                                                                          |
| [**SetSamplingInfo**](id3dxprtengine--setsamplinginfo.md)                                 | Sets sampling properties used by the precomputed radiance transfer (PRT) simulator.<br/>                                                                                                                                                                                                                                                                                                                                                                                     |
| [**ShadowRayIntersects**](id3dxprtengine--shadowrayintersects.md)                         | Uses efficient ray-tracing in precomputed radiance transfer (PRT) simulations to determine whether a ray intersects a mesh. Typically used to determine whether a given point is in shadow.<br/>                                                                                                                                                                                                                                                                             |



 

## Remarks

To convert from RGB to luminance values, the following formula is used:


```
Luminance = R * 0.2125 + G * 0.7154 + B * 0.0721
```



The **ID3DXPRTEngine** interface is obtained by calling the [**D3DXCreatePRTEngine**](d3dxcreateprtengine.md) function.

The LPD3DXPRTENGINE type is defined as a pointer to the **ID3DXPRTEngine** interface.


```
typedef interface ID3DXPRTEngine ID3DXPRTEngine;
typedef interface ID3DXPRTEngine *LPD3DXPRTENGINE;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> <dt>

[**D3DXCreatePRTEngine**](d3dxcreateprtengine.md)
</dt> <dt>

[Precomputed Radiance Transfer (Direct3D 9)](precomputed-radiance-transfer.md)
</dt> </dl>

 

 
