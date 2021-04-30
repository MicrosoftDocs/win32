---
description: Vertex buffers, represented by the IDirect3DVertexBuffer9 interface, are memory buffers that contain vertex data.
ms.assetid: 'vs|directx_sdk|~\vertex_buffers.htm'
title: Vertex Buffers (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Vertex Buffers (Direct3D 9)

Vertex buffers, represented by the [**IDirect3DVertexBuffer9**](/windows/desktop/api) interface, are memory buffers that contain vertex data. Vertex buffers can contain any vertex type - transformed or untransformed, lit or unlit - that can be rendered through the use of the rendering methods in the [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) interface. You can process the vertices in a vertex buffer to perform operations such as transformation, lighting, or generating clipping flags. Transformation is always performed.

The flexibility of vertex buffers make them ideal staging points for reusing transformed geometry. You could create a single vertex buffer, transform, light, and clip the vertices in it, and render the model in the scene as many times as needed without re-transforming it, even with interleaved render state changes. This is useful when rendering models that use multiple textures: the geometry is transformed only once, and then portions of it can be rendered as needed, interleaved with the required texture changes. Render state changes made after vertices are processed take effect the next time the vertices are processed.

-   [Description](#description)
-   [Memory Pool and Usage](#memory-pool-and-usage)

## Description

A vertex buffer is described in terms of its capabilities: if it can exist only in system memory, if it is only used for write operations, and the type and number of vertices it can contain. All these traits are held in a [**D3DVERTEXBUFFER\_DESC**](d3dvertexbuffer-desc.md) structure.

The Format member is set to D3DFMT\_VERTEXDATA to indicate that this is a vertex buffer. The Type identifies the resource type of the vertex buffer. The Usage structure member contains general capability flags. The D3DUSAGE\_SOFTWAREPROCESSING flag indicates that the vertex buffer is to be used with software vertex processing. The presence of the D3DUSAGE\_WRITEONLY flag in Usage indicates that the vertex buffer memory is used only for write operations. This frees the driver to place the vertex data in the best memory location to enable fast processing and rendering. If the D3DUSAGE\_WRITEONLY flag is not used, the driver is less likely to put the data in a location that is inefficient for read operations. This sacrifices some processing and rendering speed. If this flag is not specified, it is assumed that applications perform read and write operations on the data within the vertex buffer.

Pool specifies the memory class that is allocated for the vertex buffer. The D3DPOOL\_SYSTEMMEM flag indicates that the system created the vertex buffer in system memory.

The Size member stores the size, in bytes, of the vertex buffer data. The FVF member contains a combination of [D3DFVF](d3dfvf.md) that identify the type of vertices that the buffer contains.

## Memory Pool and Usage

You can create vertex buffers with the [**IDirect3DDevice9::CreateVertexBuffer**](/windows/desktop/api) method, which takes pool (memory class) and usage parameters. **IDirect3DDevice9::CreateVertexBuffer** can also be created with a specified FVF code for use in fixed function vertex processing, or as the output of process vertices. For details, see [FVF Vertex Buffers (Direct3D 9)](fvf-vertex-buffers.md).

The D3DUSAGE\_SOFTWAREPROCESSING flag can be set when mixed-mode or software vertex processing (D3DCREATE\_MIXED\_VERTEXPROCESSING / D3DCREATE\_SOFTWARE\_VERTEXPROCESSING) is enabled for that device. D3DUSAGE\_SOFTWAREPROCESSING must be set for buffers to be used with software vertex processing in mixed mode, but it should not be set for the best possible performance when using hardware vertex processing in mixed mode.(D3DCREATE\_HARDWARE\_VERTEXPROCESSING). However, setting D3DUSAGE\_SOFTWAREPROCESSING is the only option when a single buffer is to be used with both hardware and software vertex processing. D3DUSAGE\_SOFTWAREPROCESSING is allowed for mixed as well as for software devices.

It is possible to force vertex and index buffers into system memory by specifying D3DPOOL\_SYSTEMMEM, even when the vertex processing is done in hardware. This is a way to avoid overly large amounts of page-locked memory when a driver is putting these buffers into AGP memory.

This section introduces the concepts necessary to understand and use vertex buffers in a Direct3D application. Information is divided into the following sections.

-   [Creating a Vertex Buffer (Direct3D 9)](creating-a-vertex-buffer.md)
-   [Accessing the Contents of a Vertex Buffer (Direct3D 9)](accessing-the-contents-of-a-vertex-buffer.md)
-   [Rendering from a Vertex Buffer (Direct3D 9)](rendering-from-a-vertex-buffer.md)
-   [FVF Vertex Buffers (Direct3D 9)](fvf-vertex-buffers.md)
-   [Fixed Function Vertex Processing (Direct3D 9)](fixed-function-vertex-processing.md)
-   [Programmable Vertex Processing (Direct3D 9)](programmable-vertex-processing.md)
-   [Device Types and Vertex Processing Requirements (Direct3D 9)](device-types-and-vertex-processing-requirements.md)

## Related topics

<dl> <dt>

[Direct3D Resources](direct3d-resources.md)
</dt> <dt>

[Rendering from Vertex and Index Buffers (Direct3D 9)](rendering-from-vertex-and-index-buffers.md)
</dt> <dt>

[Index Buffers (Direct3D 9)](index-buffers.md)
</dt> </dl>

 

 
