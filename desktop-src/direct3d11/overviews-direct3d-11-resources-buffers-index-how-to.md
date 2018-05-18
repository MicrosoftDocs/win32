---
title: How to Create an Index Buffer
description: This topic shows how to initialize an index buffer in preparation for rendering.
ms.assetid: '4b33d32a-27fd-4652-87ac-3b7268881f89'
keywords: ["index buffer, creating"]
---

# How to: Create an Index Buffer

[Index buffers](overviews-direct3d-11-resources-buffers-intro.md) contain index data. This topic shows how to initialize an [index buffer](overviews-direct3d-11-resources-buffers-intro.md) in preparation for rendering.

**To initialize an index buffer**

1.  Create a buffer that contains your index information.
2.  Create a buffer description by filling in a [**D3D11\_BUFFER\_DESC**](d3d11-buffer-desc.md) structure. Pass the D3D11\_BIND\_INDEX\_BUFFER flag to the **BindFlags** member and pass the size of the buffer in bytes to the **ByteWidth** member.
3.  Create a subresource data description by filling in a [**D3D11\_SUBRESOURCE\_DATA**](d3d11-subresource-data.md) structure. The **pSysMem** member should point directly to the index data created in step one.
4.  Call [**ID3D11Device::CreateBuffer**](id3d11device-createbuffer.md) while passing the [**D3D11\_BUFFER\_DESC**](d3d11-buffer-desc.md) structure, the [**D3D11\_SUBRESOURCE\_DATA**](d3d11-subresource-data.md) structure, and the address of a pointer to the [**ID3D11Buffer**](id3d11buffer.md) interface to initialize.

The following code example demonstrates how to create an index buffer. This example assumes that


```
g_pd3dDevice
```



is a valid [**ID3D11Device**](id3d11device.md) object and that


```
g_pd3dContext
```



is a valid [**ID3D11DeviceContext**](id3d11devicecontext.md) object.


```
ID3D11Buffer *g_pIndexBuffer = NULL;

// Create indices.
unsigned int indices[] = { 0, 1, 2 };

// Fill in a buffer description.
D3D11_BUFFER_DESC bufferDesc;
bufferDesc.Usage           = D3D11_USAGE_DEFAULT;
bufferDesc.ByteWidth       = sizeof( unsigned int ) * 3;
bufferDesc.BindFlags       = D3D11_BIND_INDEX_BUFFER;
bufferDesc.CPUAccessFlags  = 0;
bufferDesc.MiscFlags       = 0;

// Define the resource data.
D3D11_SUBRESOURCE_DATA InitData;
InitData.pSysMem = indices;
InitData.SysMemPitch = 0;
InitData.SysMemSlicePitch = 0;

// Create the buffer with the device.
hr = g_pd3dDevice->CreateBuffer( &amp;bufferDesc, &amp;InitData, &amp;g_pIndexBuffer );
if( FAILED( hr ) )
    return hr;

// Set the buffer.
g_pd3dContext->IASetIndexBuffer( g_pIndexBuffer, DXGI_FORMAT_R32_UINT, 0 );
    
```



## Related topics

<dl> <dt>

[Buffers](overviews-direct3d-11-resources-buffers.md)
</dt> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> </dl>

 

 




