---
description: Shadow Volumes are used for drawing shadows with the stencil buffer.
ms.assetid: 8b71d871-ee66-47c4-8190-5c75419b28b2
title: Two-Sided Stencil (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Two-Sided Stencil (Direct3D 9)

Shadow Volumes are used for drawing shadows with the stencil buffer. The application computes the shadow volumes cast by occluding geometry, by computing the silhouette edges and extruding them away from the light into a set of 3D volumes. These volumes are then rendered twice into the stencil buffer.

The first render draws forward-facing polygons, and increments the stencil-buffer values. The second render draws the back-facing polygons of the shadow volume, and decrements the stencil buffer values. Normally, all incremented and decremented values cancel each other out. However, the scene was already rendered with normal geometry causing some pixels to fail the z-buffer test as the shadow volume is rendered. Values left in the stencil buffer correspond to pixels that are in the shadow. These remaining stencil-buffer contents are used as a mask, to alpha-blend a large, all-encompassing black quad into the scene. With the stencil buffer acting as a mask, the result is to darken pixels that are in the shadows.

This means that the shadow geometry is drawn twice per light source, hence putting pressure on the vertex throughput of the GPU. The two-sided stencil feature has been designed to mitigate this situation. In this approach, there are two sets of stencil state (named below), one set each for the front-facing triangles and the other for the back-facing triangles. This way, only a single pass is drawn per shadow volume, per light.

The API changes are restricted to a new set of render states. The new render state D3DRS\_Two\_Sided\_StencilMODE can be set to **TRUE** or **FALSE**. It is **FALSE** by default, meaning current (DirectX 8) behavior. When this is set to **TRUE** (it will work only if D3DSTENCILCAPS\_TWOSIDED is set), the following render states will apply only to the front-facing (clockwise) triangles.



| Render state        | Description                                                                              |
|---------------------|------------------------------------------------------------------------------------------|
| D3DRS\_STENCILFAIL  | D3DSTENCILOP to do if stencil test fails.                                                |
| D3DRS\_STENCILZFAIL | D3DSTENCILOP to do if stencil test passes and z-test fails.                              |
| D3DRS\_STENCILPASS  | D3DSTENCILOP to do if both stencil and z-tests pass.                                     |
| D3DRS\_STENCILFUNC  | D3DCMPFUNC fn. Stencil Test passes if ((ref & mask) stencilfn (stencil & mask)) is true. |



 

A new set of render states apply to the back-facing (counterclockwise) triangles.



| Render state             | Description                                                                                    |
|--------------------------|------------------------------------------------------------------------------------------------|
| D3DRS\_CCW\_STENCILFAIL  | D3DSTENCILOP to do if stencil test fails.                                                      |
| D3DRS\_CCW\_STENCILZFAIL | D3DSTENCILOP to do if stencil test passes and z-test fails.                                    |
| D3DRS\_CCW\_STENCILPASS  | D3DSTENCILOP to do if both stencil and z-tests pass.                                           |
| D3DRS\_CCW\_STENCILFUNC  | D3DCMPFUNC function. Stencil test passes if ((ref & mask) stencilfn (stencil & mask)) is true. |



 

The remaining stencil render states always apply to both clockwise and counterclockwise triangles.

D3DRS\_Two\_Sided\_StencilMODE is ignored for lines and point sprites, which means that the behavior is unchanged from DirectX 8. The D3DRS\_CCW\_STENCIL\* render states are ignored.

A new cap bit indicates if the device supports this feature. Drivers that do not support this feature are expected to ignore these new render states. All other stencil cap bits apply to both modes of stencil buffering. Because Two\_Sided\_Stencil implies the ability to draw with D3DCULLMODE\_NONE set, the corresponding cap must be set by the driver if it supports this new stencil mode. Microsoft Windows Hardware Quality Labs (WHQL) should enforce this.

New render states:


```
D3DRS_Two_Sided_StencilMODE // BOOL (default is FALSE)
D3DRS_CCW_STENCILFAIL     // Same default as D3DRS_STENCILFAIL
D3DRS_CCW_STENCILZFAIL    // Same default as D3DRS_STENCILZFAIL
D3DRS_CCW_STENCILPASS     // Same default as D3DRS_STENCILPASS
D3DRS_CCW_STENCILFUNC     // Same default as D3DRS_STENCILFUNC
```



New cap:


```
D3DSTENCILCAPS_TWOSIDED // a flag on D3DCAPS9.StencilCaps
```



## Related topics

<dl> <dt>

[Stencil Buffer Techniques](stencil-buffer-techniques.md)
</dt> <dt>

[**D3DRENDERSTATETYPE**](./d3drenderstatetype.md)
</dt> </dl>

 

 
