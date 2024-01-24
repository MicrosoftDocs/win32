---
description: To determine if Direct3D supports vertex tweening, check for the D3DVTXPCAPS\_TWEENING flag in the VertexProcessingCaps member of the D3DCAPS9 structure.
ms.assetid: b60c7f96-3752-4703-9059-486d9906c508
title: Using Vertex Tweening (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Using Vertex Tweening (Direct3D 9)

To determine if Direct3D supports vertex tweening, check for the D3DVTXPCAPS\_TWEENING flag in the VertexProcessingCaps member of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure. The following code example uses the [**IDirect3DDevice9::GetDeviceCaps**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getdevicecaps) method to determine if tweening is supported.


```
// This example assumes that m_pD3DDevice is 
// a valid pointer to a IDirect3DDevice9 interface.
//
D3DCAPS9 d3dCaps;

m_pD3DDevice->GetDeviceCaps( &d3dCaps );
if( 0 != (d3dCaps.VertexProcessingCaps & D3DVTXPCAPS_TWEENING) )
    // Vertex tweening is supported.
```



To use vector tweening, you must first set up a custom vertex type that uses a second normal or a second position. The following code example shows a sample declaration that includes both a second point and a second position.


```
struct TEX_VERTEX
{
    D3DVECTOR position;
    D3DVECTOR normal;
    D3DVECTOR position2;
    D3DVECTOR normal2;
};

//Create a vertex buffer with the type TEX_VERTEX.
```



The next step is to set the current declaration. The code example below shows how to do this.


```
// Create the shader declaration.
D3DVERTEXELEMENT9 decl[] = 
{
    { 0, 0,  D3DDECLTYPE_FLOAT3, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_POSITION, 0 },
    { 0, 12, D3DDECLTYPE_FLOAT3, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_NORMAL, 0 },
    { 0, 24, D3DDECLTYPE_FLOAT3, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_POSITION, 1 },
    { 0, 36, D3DDECLTYPE_FLOAT3, D3DDECLMETHOD_DEFAULT, D3DDECLUSAGE_NORMAL, 1 },
    D3DDECL_END()
};
```



For more information about creating a custom vertex type and a vertex buffer, see [Creating a Vertex Buffer (Direct3D 9)](creating-a-vertex-buffer.md).

> [!Note]  
> When vertex tweening is enabled, a second position or a second normal must be present in the current declaration.

 

## Related topics

<dl> <dt>

[Vertex Tweening](vertex-tweening.md)
</dt> </dl>

 

 
