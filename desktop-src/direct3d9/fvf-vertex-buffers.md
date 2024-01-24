---
description: Setting the FVF parameter of the IDirect3DDevice9::CreateVertexBuffer method to a nonzero value, which must be a valid FVF code, indicates that the buffer content is to be characterized by an FVF code.
ms.assetid: 7cab559f-3e9d-46bd-b00f-439e0922aeeb
title: FVF Vertex Buffers (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# FVF Vertex Buffers (Direct3D 9)

Setting the FVF parameter of the [**IDirect3DDevice9::CreateVertexBuffer**](/windows/desktop/api) method to a nonzero value, which must be a valid FVF code, indicates that the buffer content is to be characterized by an FVF code. A vertex buffer that is created with an FVF code is referred to as an FVF vertex buffer. Some methods or uses of [**IDirect3DDevice9**](/windows/desktop/api) require FVF vertex buffers, and others require non-FVF vertex buffers. FVF vertex buffers are required as the destination vertex buffer argument for [**IDirect3DDevice9::ProcessVertices**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-processvertices).

FVF vertex buffers can be bound to a source data stream for any stream number.

The presence of the D3DFVF\_XYZRHW component on FVF vertex buffers indicates that the vertices in that buffer have been processed. Vertex buffers used for [**IDirect3DDevice9::ProcessVertices**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-processvertices) destination vertex buffers must be post-processed. Vertex buffers used for fixed function shader inputs can be either preprocessed or postprocessed. If the vertex buffer is post-processed, then the shader is effectively bypassed and the data is passed directly to the primitive clipping and setup module.

FVF vertex buffers can be used with vertex shaders. Also, vertex streams can represent the same vertex formats that non-FVF vertex buffers can. They do not have to be used to input data from separate vertex buffers. The additional flexibility of the new vertex streams enables applications that need to keep their data separate to work better, but it is not required. If the application can maintain interleaved data in advance, then that is a performance boost. If the application will only interleave the data before every rendering call, then it should enable the API or hardware to do this with multiple streams.

The most important things with vertex performance is to use a 32-byte vertex, and to maintain good cache ordering.

## Related topics

<dl> <dt>

[Vertex Buffers](vertex-buffers.md)
</dt> </dl>

 

 
