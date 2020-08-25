---
title: How to Create a Constant Buffer
description: This topic shows how to initialize a constant buffer in preparation for rendering.
ms.assetid: 78694ac2-e850-402d-8c99-6afb0bd5d660
keywords:
- constant buffer, creating
ms.topic: article
ms.date: 05/31/2018
---

# How to: Create a Constant Buffer

[Constant buffers](overviews-direct3d-11-resources-buffers-intro.md) contain shader constant data. This topic shows how to initialize a [constant buffer](overviews-direct3d-11-resources-buffers-intro.md) in preparation for rendering.

**To initialize a constant buffer**

1.  Define a structure that describes the vertex shader constant data.
2.  Allocate memory for the structure that you defined in step one. Fill this buffer with vertex shader constant data. You can use **malloc** or **new** to allocate the memory, or you can allocate memory for the structure from the stack.
3.  Create a buffer description by filling in a [**D3D11\_BUFFER\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_buffer_desc) structure. Pass the D3D11\_BIND\_CONSTANT\_BUFFER flag to the **BindFlags** member and pass the size of the constant buffer description structure in bytes to the **ByteWidth** member.

    > [!Note]  
    > The D3D11\_BIND\_CONSTANT\_BUFFER flag cannot be combined with any other flags.

     

4.  Create a subresource data description by filling in a [**D3D11\_SUBRESOURCE\_DATA**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_subresource_data) structure. The **pSysMem** member of the **D3D11\_SUBRESOURCE\_DATA** structure must point directly to the vertex shader constant data that you created in step two.
5.  Call [**ID3D11Device::CreateBuffer**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createbuffer) while passing the [**D3D11\_BUFFER\_DESC**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_buffer_desc) structure, the [**D3D11\_SUBRESOURCE\_DATA**](/windows/desktop/api/D3D11/ns-d3d11-d3d11_subresource_data) structure, and the address of a pointer to the [**ID3D11Buffer**](/windows/desktop/api/D3D11/nn-d3d11-id3d11buffer) interface to initialize.

These code examples demonstrate how to create a constant buffer.

This example assumes that **g\_pd3dDevice** is a valid [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) object and that **g\_pd3dContext** is a valid [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) object.


```C++
ID3D11Buffer*   g_pConstantBuffer11 = NULL;

// Define the constant data used to communicate with shaders.
struct VS_CONSTANT_BUFFER
{
    XMFLOAT4X4 mWorldViewProj;                              
    XMFLOAT4 vSomeVectorThatMayBeNeededByASpecificShader;
    float fSomeFloatThatMayBeNeededByASpecificShader;
    float fTime;                                            
    float fSomeFloatThatMayBeNeededByASpecificShader2;
    float fSomeFloatThatMayBeNeededByASpecificShader3;
} VS_CONSTANT_BUFFER;

// Supply the vertex shader constant data.
VS_CONSTANT_BUFFER VsConstData;
VsConstData.mWorldViewProj = {...};
VsConstData.vSomeVectorThatMayBeNeededByASpecificShader = XMFLOAT4(1,2,3,4);
VsConstData.fSomeFloatThatMayBeNeededByASpecificShader = 3.0f;
VsConstData.fTime = 1.0f;
VsConstData.fSomeFloatThatMayBeNeededByASpecificShader2 = 2.0f;
VsConstData.fSomeFloatThatMayBeNeededByASpecificShader3 = 4.0f;

// Fill in a buffer description.
D3D11_BUFFER_DESC cbDesc;
cbDesc.ByteWidth = sizeof( VS_CONSTANT_BUFFER );
cbDesc.Usage = D3D11_USAGE_DYNAMIC;
cbDesc.BindFlags = D3D11_BIND_CONSTANT_BUFFER;
cbDesc.CPUAccessFlags = D3D11_CPU_ACCESS_WRITE;
cbDesc.MiscFlags = 0;
cbDesc.StructureByteStride = 0;

// Fill in the subresource data.
D3D11_SUBRESOURCE_DATA InitData;
InitData.pSysMem = &VsConstData;
InitData.SysMemPitch = 0;
InitData.SysMemSlicePitch = 0;

// Create the buffer.
hr = g_pd3dDevice->CreateBuffer( &cbDesc, &InitData, 
                                 &g_pConstantBuffer11 );

if( FAILED( hr ) )
   return hr;

// Set the buffer.
g_pd3dContext->VSSetConstantBuffers( 0, 1, &g_pConstantBuffer11 );
    
```



This example shows the associated HLSL cbuffer definition.

``` syntax
cbuffer VS_CONSTANT_BUFFER : register(b0)
{
    matrix mWorldViewProj;
    float4  vSomeVectorThatMayBeNeededByASpecificShader;
    float fSomeFloatThatMayBeNeededByASpecificShader;
    float fTime;
    float fSomeFloatThatMayBeNeededByASpecificShader2;
    float fSomeFloatThatMayBeNeededByASpecificShader3;
};
```

> [!Note]  
> Make sure to match the VS\_CONSTANT\_BUFFER memory layout in C++ with the HLSL layout. For info about how HLSL handles layout in memory, see [Packing Rules for Constant Variables](/windows/desktop/direct3dhlsl/dx-graphics-hlsl-packing-rules).

 

## Related topics

<dl> <dt>

[Buffers](overviews-direct3d-11-resources-buffers.md)
</dt> <dt>

[How to Use Direct3D 11](how-to-use-direct3d-11.md)
</dt> </dl>

 

 