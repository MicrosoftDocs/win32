---
description: Rendering vertex data from a vertex buffer requires a few steps. First, you need to set the stream source by calling the IDirect3DDevice9::SetStreamSource method, as shown in the following example.
ms.assetid: a0435a3d-e1dd-4365-904d-8e5713e379ce
title: Rendering from a Vertex Buffer (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Rendering from a Vertex Buffer (Direct3D 9)

Rendering vertex data from a vertex buffer requires a few steps. First, you need to set the stream source by calling the [**IDirect3DDevice9::SetStreamSource**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setstreamsource) method, as shown in the following example.


```
d3dDevice->SetStreamSource( 0, g_pVB, 0, sizeof(CUSTOMVERTEX) );
```



The first parameter of [**IDirect3DDevice9::SetStreamSource**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setstreamsource) tells Direct3D the source of the device data stream. The second parameter is the vertex buffer to bind to the data stream. The third parameter is the offset from the beginning of the stream to the beginning of the vertex data, in bytes. The fourth parameter is the stride of the component, in bytes. In the sample code above, the size of a CUSTOMVERTEX is used for the stride of the component.

The next step is to inform Direct3D which vertex shader to use by calling the [**IDirect3DDevice9::SetVertexShader**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setvertexshader) method. The following sample code sets an FVF code for the vertex shader. This informs Direct3D of the types of vertices it is dealing with.


```
d3dDevice->SetFVF( D3DFVF_CUSTOMVERTEX );
```



After setting the stream source and vertex shader, any draw methods will use the vertex buffer. The code example below shows how to render vertices from a vertex buffer with the [**IDirect3DDevice9::DrawPrimitive**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawprimitive) method.


```
d3dDevice->DrawPrimitive( D3DPT_TRIANGLELIST, 0, 1 );
```



The second parameter that [**IDirect3DDevice9::DrawPrimitive**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawprimitive) accepts is the index of the first vector in the vertex buffer to load.

## Related topics

<dl> <dt>

[Vertex Buffers](vertex-buffers.md)
</dt> <dt>

[Rendering from Vertex and Index Buffers (Direct3D 9)](rendering-from-vertex-and-index-buffers.md)
</dt> </dl>

 

 
