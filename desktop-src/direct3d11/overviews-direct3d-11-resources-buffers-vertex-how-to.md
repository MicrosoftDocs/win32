---
title: How to Create a Vertex Buffer
description: This topic shows how to initialize a static vertex buffer, that is, a vertex buffer that does not change.
ms.assetid: 584a39d1-7629-429a-b451-64b1432cb48f
keywords:
- vertex buffer, creating
ms.topic: article
ms.date: 05/31/2018
---

# How to: Create a Vertex Buffer

[Vertex buffers](overviews-direct3d-11-resources-buffers-intro.md) contain per vertex data. This topic shows how to initialize a static [vertex buffer](overviews-direct3d-11-resources-buffers-intro.md), that is, a vertex buffer that does not change. For help initializing a non-static buffer, see the [remarks](#remarks) section.

**To initialize a static vertex buffer**

1.  Define a structure that describes a vertex. For example, if your vertex data contains position data and color data, your structure would have one vector that describes the position and another that describes the color.
2.  Allocate memory (using malloc or new) for the structure that you defined in step one. Fill this buffer with the actual vertex data that describes your geometry.
3.  Create a buffer description by filling in a [**D3D11\_BUFFER\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_buffer_desc) structure. Pass the D3D11\_BIND\_VERTEX\_BUFFER flag to the **BindFlags** member and pass the size of the structure from step one to the **ByteWidth** member.
4.  Create a subresource data description by filling in a [**D3D11\_SUBRESOURCE\_DATA**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_subresource_data) structure. The **pSysMem** member of the [**D3D11\_SUBRESOURCE\_DATA**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_subresource_data) structure should point directly to the resource data created in step two.
5.  Call [**ID3D11Device::CreateBuffer**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createbuffer) while passing the [**D3D11\_BUFFER\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_buffer_desc) structure, the [**D3D11\_SUBRESOURCE\_DATA**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_subresource_data) structure, and the address of a pointer to the [**ID3D11Buffer**](/windows/desktop/api/D3D11/nn-d3d11-id3d11buffer) interface to initialize.

The following code example demonstrates how to create a vertex buffer. This example assumes that **g\_pd3dDevice** is a valid [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) object.


```
ID3D11Buffer*      g_pVertexBuffer;

// Define the data-type that
// describes a vertex.
struct SimpleVertexCombined
{
    XMFLOAT3 Pos;  
    XMFLOAT3 Col;  
};

// Supply the actual vertex data.
SimpleVertexCombined verticesCombo[] =
{
    XMFLOAT3( 0.0f, 0.5f, 0.5f ),
    XMFLOAT3( 0.0f, 0.0f, 0.5f ),
    XMFLOAT3( 0.5f, -0.5f, 0.5f ),
    XMFLOAT3( 0.5f, 0.0f, 0.0f ),
    XMFLOAT3( -0.5f, -0.5f, 0.5f ),
    XMFLOAT3( 0.0f, 0.5f, 0.0f ),
};

// Fill in a buffer description.
D3D11_BUFFER_DESC bufferDesc;
bufferDesc.Usage            = D3D11_USAGE_DEFAULT;
bufferDesc.ByteWidth        = sizeof( SimpleVertexCombined ) * 3;
bufferDesc.BindFlags        = D3D11_BIND_VERTEX_BUFFER;
bufferDesc.CPUAccessFlags   = 0;
bufferDesc.MiscFlags        = 0;

// Fill in the subresource data.
D3D11_SUBRESOURCE_DATA InitData;
InitData.pSysMem = verticesCombo;
InitData.SysMemPitch = 0;
InitData.SysMemSlicePitch = 0;

// Create the vertex buffer.
hr = g_pd3dDevice->CreateBuffer( &bufferDesc, &InitData, &g_pVertexBuffer );
    
```



## Remarks

Here are some ways to initialize a vertex buffer that changes over time.

1.  Create a 2nd buffer with [**D3D11\_USAGE\_STAGING**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_usage); fill the second buffer using [**ID3D11DeviceContext::Map**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-map), [**ID3D11DeviceContext::Unmap**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-unmap); use [**ID3D11DeviceContext::CopyResource**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-copyresource) to copy from the staging buffer to the default buffer.
2.  Use [**ID3D11DeviceContext::UpdateSubresource**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-updatesubresource) to copy data from memory.
3.  Create a buffer with [**D3D11\_USAGE\_DYNAMIC**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_usage), and fill it with [**ID3D11DeviceContext::Map**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-map), [**ID3D11DeviceContext::Unmap**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-unmap) (using the Discard and NoOverwrite flags appropriately).

\#1 and \#2 are useful for content that changes less than once per frame. In general, GPU reads will be fast and CPU updates will be slower.

\#3 is useful for content that changes more than once per frame. In general, GPU reads will be slower, but CPU updates will be faster.

## Related topics

<dl> <dt>

[Buffers](overviews-direct3d-11-resources-buffers.md)
</dt> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> </dl>

 

 




