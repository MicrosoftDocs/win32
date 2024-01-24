---
description: Transform states 256-511 are reserved to store up to 256 matrices that can be indexed using 8-bit indices.
ms.assetid: 4c15cfc5-afdf-48d4-8fd1-b10cbe596a1c
title: Using Indexed Vertex Blending (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Using Indexed Vertex Blending (Direct3D 9)

Transform states 256-511 are reserved to store up to 256 matrices that can be indexed using 8-bit indices. Use the macro [**D3DTS\_WORLDMATRIX**](d3dts-worldmatrix.md) to map indices 0-255 to the corresponding transform states. The following code example shows how to use the [**IDirect3DDevice9::SetTransform**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settransform) method to set the matrix at transform state number 256 to an identity matrix.


```
D3DMATRIX matBlend1;
D3DXMatrixIdentity( &matBlend1 );
m_pD3DDevice->SetTransform( D3DTS_WORLDMATRIX(0), &matBlend );
```



To enable or disable indexed vertex blending, set the D3DRS\_INDEXEDVERTEXBLENDENABLE render state to **TRUE**. When the render state is enabled ,you must pass matrix indices as packed DWORDs with every vertex. When this render state is disabled and vertex blending is enabled, it is equivalent to having the matrix indices 0, 1, 2, and 3 in every vertex. The code example below uses the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) method to enable indexed vertex blending.


```
m_pD3DDevice->SetRenderState( D3DRS_INDEXEDVERTEXBLENDENABLE, TRUE );
```



To enable or disable vertex blending, set the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) render state to a value other than D3DRS\_DISABLE from the [**D3DVERTEXBLENDFLAGS**](./d3dvertexblendflags.md) enumerated type. If this render state is not set to D3DRS\_DISABLE, then you must pass the required number of weights for each vertex. The following code example uses **IDirect3DDevice9::SetRenderState** to enable vertex blending with three weights for each vertex.


```
m_pD3DDevice->SetRenderState( D3DRS_VERTEXBLEND, D3DVBF_3WEIGHTS );
```



## Determining Indexed Vertex Blending Support

To determine the maximum size for the indexed vertex blending matrix, check the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure's MaxVertexBlendMatrixIndex member. The code example below uses the [**IDirect3DDevice9::GetDeviceCaps**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getdevicecaps) method to retrieve this size.


```
D3DCAPS9 d3dCaps;
    
m_pD3DDevice->GetDeviceCaps( &d3dCaps );
IndexedMatrixMaxSize = d3dCaps.MaxVertexBlendMatrixIndex;
```



If the value set in MaxVertexBlendMatrixIndex is 0, the device does not support indexed matrices.

> [!Note]  
> When software vertex processing is used, 256 matrices can be used for indexed vertex blending, with or without normal blending.

 

## Passing Matrix Indices to Direct3D

World matrix indices can be passed to Direct3D by using legacy vertex shaders - FVF - or declarations.

The code example below shows how to use legacy vertex shaders.


```
struct VERTEX
{
    float x,y,z;
    float weight;
    DWORD matrixIndices;
    float normal[3];
};
    
#define D3DFVF_CUSTOMVERTEX (D3DFVF_XYZB2 | D3DFVF_LASTBETA_UBYTE4 |
                             D3DFVF_NORMAL);
```



When a legacy vertex shader is used, matrix indices are passed together with vertex positions using D3DFVF\_XYZBn flags. Matrix indices are passed as bytes inside a DWORD and must be present immediately after the last vertex weight. Vertex weights are also passed using D3DFVF\_XYZBn. A packed DWORD contains index3, index2, index1, and index0, where index0 is located in the lowest byte of the DWORD. The number of used world-matrix indices is equal to the number passed to the number of matrices used for blending as defined by [**D3DRS\_VERTEXBLEND**](./d3drenderstatetype.md).

When a declaration is used, D3DVSDE\_BLENDINDICES defines the input vertex register to get matrix indices from. Matrix indices must be passed as D3DVSDT\_UBYTE4.

The code example below shows how to use declarations. Note that the order of the components is no longer important unless using a fixed-function vertex shader.

Here is the vertex declaration.


```
struct VERTEX
{
    float x,y,z;
    float weight;
    DWORD matrixIndices;
    float normal[3];
}
```



Here is the corresponding register declaration.


```
// Create the shader declaration.
D3DVERTEXELEMENT9 decl[] = 
{
    { 0, 0,  D3DDECLTYPE_FLOAT3, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_POSITION, 0 },
    { 0, 12, D3DDECLTYPE_FLOAT1, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_BLENDWEIGHT, 0 },
    { 0, 16, D3DDECLTYPE_UBYTE4, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_BLENDINDICES, 0 },
    { 0, 20, D3DDECLTYPE_FLOAT3, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_NORMAL, 0 },
    D3DDECL_END()
};
```



## Related topics

<dl> <dt>

[Indexed Vertex Blending](indexed-vertex-blending.md)
</dt> </dl>

 

 
