---
description: The performance of vertex processing operations, including transformation and lighting, depends heavily on where the vertex buffer exists in memory and what type of rendering device is being used.
ms.assetid: 4f9ca83d-c9d6-4749-944d-78f831b0f44e
title: Device Types and Vertex Processing Requirements (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Device Types and Vertex Processing Requirements (Direct3D 9)

The performance of vertex processing operations, including transformation and lighting, depends heavily on where the vertex buffer exists in memory and what type of rendering device is being used. Applications control the memory allocation for vertex buffers when they are created. When the D3DPOOL\_SYSTEMMEM memory flag is set, the vertex buffer is created in system memory. When the D3DPOOL\_DEFAULT memory flag is used, the device driver determines where the memory for the vertex buffer is best allocated, often referred to as driver-optimal memory. Driver-optimal memory can be local video memory, nonlocal video memory, or system memory.

Setting the D3DUSAGE\_SOFTWAREPROCESSING constant with [**IDirect3DDevice9::CreateVertexBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createvertexbuffer) enables software vertex processing on the vertex buffer data. This flag is required for software vertex processing while in mixed mode. The flag may not be used for hardware vertex processing mode. Vertex buffers used with software vertex processing include the following:

-   All input streams for [**IDirect3DDevice9::ProcessVertices**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-processvertices).
-   All input streams for [**IDirect3DDevice9::DrawPrimitive**](/windows/desktop/api) and [**IDirect3DDevice9::DrawIndexedPrimitive**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawindexedprimitive).

The reasoning you use to determine the memory location - system or driver optimal - for vertex buffers is the same as that for textures. Vertex processing, including transformation and lighting, in hardware works best when the vertex buffers are allocated in driver-optimal memory, while software vertex processing works best with vertex buffers allocated in system memory. For textures, hardware rasterization works best when textures are allocated in driver-optimal memory, while software rasterization works best with system-memory textures.

Microsoft Direct3D 9 supports standalone processing of vertices, without rendering any primitive with the [**IDirect3DDevice9::ProcessVertices**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-processvertices) method. This standalone vertex processing is always performed in software on the host processor. Because of this, vertex buffers used as sources set with [**IDirect3DDevice9::SetStreamSource**](/windows/desktop/api) must be created with the D3DUSAGE\_SOFTWAREPROCESSING flag. The functionality provided by **IDirect3DDevice9::ProcessVertices** is identical to that of the [**IDirect3DDevice9::DrawPrimitive**](/windows/desktop/api) and [**IDirect3DDevice9::DrawIndexedPrimitive**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-drawindexedprimitive) methods while using software vertex processing.

If your application performs its own vertex processing and passes transformed, lit, and clipped vertices to rendering methods, then the application can directly write vertices to a vertex buffer allocated in driver-optimal memory. This technique prevents a redundant copy operation later. Note that this technique will not work well if your application reads data back from a vertex buffer, because read operations done by the host from driver-optimal memory can be very slow. Therefore, if your application needs to read during processing or writes data to the buffer erratically, a system-memory vertex buffer is a better choice.

When using the Direct3D vertex processing features (by passing untransformed vertices to vertex-buffer rendering methods), processing can occur in either hardware or software depending on the device type and device creation flags. It is recommended that vertex buffers be allocated in pool D3DPOOL\_DEFAULT for best performance in virtually all cases. When a device is using hardware vertex processing, there are a number of additional optimizations that may be done based on the flags D3DUSAGE\_DYNAMIC and D3DUSAGE\_WRITEONLY. See IDirect3DDevice9::CreateVertexBuffer for more information about using these flags.

## Related topics

<dl> <dt>

[Vertex Buffers](vertex-buffers.md)
</dt> </dl>

 

 
