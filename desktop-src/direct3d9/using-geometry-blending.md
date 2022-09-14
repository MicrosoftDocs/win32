---
description: The following user-defined structure can be used for vertices that will be blended between two matrices.
ms.assetid: 6bcabcf9-d14e-446a-8dd2-e741211cc704
title: Using Geometry Blending (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Using Geometry Blending (Direct3D 9)

The following user-defined structure can be used for vertices that will be blended between two matrices.


```
// The flexible vertex format (FVF) descriptor for this vertex would be:
//   FVF = D3DFVF_XYZB1 | D3DFVF_NORMAL | D3DFVF_TEX1; 

struct D3DBLENDVERTEX {
    D3DVECTOR v;
    FLOAT     blend; 
    D3DVECTOR n;
    FLOAT     tu, tv;
};
```



The blend weight must appear after the position and RHW data in the FVF, and before the vertex normal.

Notice that the preceding vertex format contains only one blending weight value. This is because there will be two world matrices, defined in the [**D3DTS\_WORLDMATRIX**](d3dts-worldmatrix.md)(0) and **D3DTS\_WORLDMATRIX**(1) transform states. The system blends each vertex between these two matrices using the single weight value. For three matrices, only two weights are required, and so on.

> [!Note]
>
> Defining skin weights is easy. Using a linear function of the distance between joints is good start, but a smoother sigmoid function looks better. Choosing a skin-weight distribution function can result in sharp creases at joints, if desired, by using a large variation in skin weight over a short distance.

 

## Setting Blending Matrices

You set the transformation matrices between which the system blends by calling the [**IDirect3DDevice9::SetTransform**](/windows/desktop/api) method. Set the first parameter to a value defined by the [**D3DTS\_WORLDMATRIX**](d3dts-worldmatrix.md) macro, and set the second parameter to the address of the matrix to be set.

The following C++ code example sets two world matrices, between which geometry is blended to create the illusion of a jointed arm.


```
// For this example, the d3dDevice variable is assumed to be a valid pointer
//   to an IDirect3DDevice9 interface for an initialized 3D scene.

float     BendAngle = 3.1415926f / 4.0f; // 45 degrees
D3DMATRIX matUpperArm, matLowerArm;

// The upper arm is immobile. Use the identity matrix.
D3DXMatrixIdentity( matUpperArm );
d3dDevice->SetTransform( D3DTS_WORLDMATRIX(0), &matUpperArm );

// The lower arm rotates about the x-axis, attached to the upper arm.
D3DXMatrixRotationX( matLowerArm, -BendAngle ); 
d3dDevice->SetTransform( D3DTS_WORLDMATRIX(1), &matLowerArm );
```



Setting a blending matrix merely causes the system to cache the matrix for later use; it doesn't instruct the system to begin blending vertices.

## Enabling Geometry Blending

Geometry blending is disabled by default. To enable geometry blending, call the [**IDirect3DDevice9::SetRenderState**](/windows/desktop/api) method to set the D3DRS\_VERTEXBLEND render state to a value from the [**D3DVERTEXBLENDFLAGS**](./d3dvertexblendflags.md) enumerated type. The following code example shows what this call might look like when setting the render state for a blend between two world matrices.


```
d3dDevice->SetRenderState( D3DRS_VERTEXBLEND, D3DVBF_1WEIGHTS );
```



When D3DRS\_VERTEXBLEND is set to any value other than D3DVBF\_DISABLE, the system assumes that the appropriate number of blending weights will be included in the vertex format. It is your responsibility to provide a compliant vertex format, and to provide a proper description of that format to the Direct3D rendering methods.

When enabled, the system performs geometry blending for all objects rendered by the DrawPrimitive rendering methods.

## See Also

[Fixed Function FVF Codes (Direct3D 9)](fixed-function-fvf-codes.md)


## Related topics

<dl> <dt>

[Geometry Blending](geometry-blending.md)
</dt> </dl>

 

 
