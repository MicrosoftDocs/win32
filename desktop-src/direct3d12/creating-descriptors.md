---
title: Creating descriptors
description: Describes and shows examples for creating index, vertex, and constant buffer views; shader resource, render target, unordered access, stream output, and depth-stencil views; and samplers. All methods for creating descriptors are free-threaded.
ms.assetid: 0D360A7C-8A2F-49E1-A5CC-98C958B59D1C
ms.topic: article
ms.date: 06/14/2022
---

# Creating descriptors

Describes and shows examples for creating index, vertex, and constant buffer views; shader resource, render target, unordered access, stream output, and depth-stencil views; and samplers. All methods for creating descriptors are free-threaded.

## Index buffer view

To create an index buffer view, fill out a [**D3D12_INDEX_BUFFER_VIEW**](/windows/win32/api/d3d12/ns-d3d12-d3d12_index_buffer_view) structure:

``` syntax
typedef struct D3D12_INDEX_BUFFER_VIEW
{
    D3D12_GPU_VIRTUAL_ADDRESS BufferLocation;
    UINT SizeInBytes;
    DXGI_FORMAT Format;
}   D3D12_INDEX_BUFFER_VIEW;
```

Set the location (call [**GetGPUVirtualAddress**](/windows/win32/api/d3d12/nf-d3d12-id3d12resource-getgpuvirtualaddress)) and size of the buffer, noting that **D3D12_GPU_VIRTUAL_ADDRESS** is defined as:

`typedef UINT64 D3D12_GPU_VIRTUAL_ADDRESS;`

Refer to the [**DXGI_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) enum. Typically for an index buffer, the following define might be used:

`const DXGI_FORMAT StandardIndexFormat = DXGI_FORMAT_R32_UINT;`

Finally, call [**ID3D12GraphicsCommandList::IASetIndexBuffer**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-iasetindexbuffer).

For example,

```cpp
// Initialize the index buffer view.
m_indexBufferView.BufferLocation = m_indexBuffer->GetGPUVirtualAddress();
m_indexBufferView.SizeInBytes = SampleAssets::IndexDataSize;
m_indexBufferView.Format = SampleAssets::StandardIndexFormat;
```

## Vertex buffer view

To create a vertex buffer view, fill out a [**D3D12_VERTEX_BUFFER_VIEW**](/windows/win32/api/d3d12/ns-d3d12-d3d12_vertex_buffer_view) structure:

``` syntax
typedef struct D3D12_VERTEX_BUFFER_VIEW {
    D3D12_GPU_VIRTUAL_ADDRESS BufferLocation;  
    UINT SizeInBytes;  
    UINT StrideInBytes;  
} D3D12_VERTEX_BUFFER_VIEW;
```

Set the location (call [**GetGPUVirtualAddress**](/windows/win32/api/d3d12/nf-d3d12-id3d12resource-getgpuvirtualaddress)) and size of the buffer, noting that **D3D12_GPU_VIRTUAL_ADDRESS** is defined as:

`typedef UINT64 D3D12_GPU_VIRTUAL_ADDRESS;`

The stride is typically the size of a single vertex data structure, such as `sizeof(Vertex);`. Then call [**ID3D12GraphicsCommandList::IASetVertexBuffers**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-iasetvertexbuffers).

For example,

```cpp
// Initialize the vertex buffer view.
m_vertexBufferView.BufferLocation = m_vertexBuffer->GetGPUVirtualAddress();
m_vertexBufferView.SizeInBytes = SampleAssets::VertexDataSize;
m_vertexBufferView.StrideInBytes = SampleAssets::StandardVertexStride;
```

## Shader resource view

To create a shader resource view, fill out a [**D3D12_SHADER_RESOURCE_VIEW_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_shader_resource_view_desc) structure:

``` syntax
typedef struct D3D12_SHADER_RESOURCE_VIEW_DESC  
    {  
    DXGI_FORMAT Format;  
    D3D12_SRV_DIMENSION ViewDimension;  
    UINT Shader4ComponentMapping;  
    union   
        {  
        D3D12_BUFFER_SRV Buffer;  
        D3D12_TEX1D_SRV Texture1D;  
        D3D12_TEX1D_ARRAY_SRV Texture1DArray;  
        D3D12_TEX2D_SRV Texture2D;  
        D3D12_TEX2D_ARRAY_SRV Texture2DArray;  
        D3D12_TEX2DMS_SRV Texture2DMS;  
        D3D12_TEX2DMS_ARRAY_SRV Texture2DMSArray;  
        D3D12_TEX3D_SRV Texture3D;  
        D3D12_TEXCUBE_SRV TextureCube;  
        D3D12_TEXCUBE_ARRAY_SRV TextureCubeArray;  
        }   ;  
    }   D3D12_SHADER_RESOURCE_VIEW_DESC; 
```

The *ViewDimension* field is set to a value of the [**D3D12_SRV_DIMENSION**](/windows/win32/api/d3d12/ne-d3d12-d3d12_srv_dimension) enum.

The enums and structures referenced by [**D3D12_SHADER_RESOURCE_VIEW_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_shader_resource_view_desc) are:

-   [**DXGI_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)
-   [**D3D12_BUFFER_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_buffer_srv)
-   [**D3D12_TEX1D_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex1d_srv)
-   [**D3D12_TEX1D_ARRAY_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex1d_array_srv)
-   [**D3D12_TEX2D_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2d_srv)
-   [**D3D12_TEX2D_ARRAY_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2d_array_srv)
-   [**D3D12_TEX2DMS_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2dms_srv)
-   [**D3D12_TEX2DMS_ARRAY_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2dms_array_srv)
-   [**D3D12_TEX3D_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex3d_srv)
-   [**D3D12_TEXCUBE_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_texcube_srv)
-   [**D3D12_TEXCUBE_ARRAY_SRV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_texcube_array_srv)

> [!NOTE]
> In the code example below, float *ResourceMinLODClamp* is part of SRVs for Tex1D/2D/3D/Cube. In Direct3D 11, it was a property of a resource; but that didn't match how it was implemented in hardware. *StructureByteStride* is part of buffer SRVs; whereas in Direct3D 11 it was a property of the resource. If the stride is non-zero, then that indicates a structured buffer view, and the format must be set to **DXGI_FORMAT_UNKNOWN**.

Finally, to create the shader resource view, call [**ID3D12Device::CreateShaderResourceView**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createshaderresourceview).

For example,

```cpp
// Describe and create an SRV.
D3D12_SHADER_RESOURCE_VIEW_DESC srvDesc = {};
srvDesc.ViewDimension = D3D12_SRV_DIMENSION_TEXTURE2D;
srvDesc.Shader4ComponentMapping = D3D12_DEFAULT_SHADER_4_COMPONENT_MAPPING;
srvDesc.Format = tex.Format;
srvDesc.Texture2D.MipLevels = tex.MipLevels;
srvDesc.Texture2D.MostDetailedMip = 0;
srvDesc.Texture2D.ResourceMinLODClamp = 0.0f;
m_device->CreateShaderResourceView(m_textures[i].Get(), &srvDesc, cbvSrvHandle);
```

## Constant buffer view

To create a constant buffer view, fill out a [**D3D12_CONSTANT_BUFFER_VIEW_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_constant_buffer_view_desc) structure:

``` syntax
typedef struct D3D12_CONSTANT_BUFFER_VIEW_DESC {
  D3D12_GPU_VIRTUAL_ADDRESS BufferLocation;
  UINT   SizeInBytes;
} D3D12_CONSTANT_BUFFER_VIEW_DESC;
```

Then call [**ID3D12Device::CreateConstantBufferView**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createconstantbufferview).

For example,

```cpp
// Describe and create a constant buffer view.
D3D12_CONSTANT_BUFFER_VIEW_DESC cbvDesc = {};
cbvDesc.BufferLocation = m_constantBuffer->GetGPUVirtualAddress();
cbvDesc.SizeInBytes = (sizeof(ConstantBuffer) + 255) & ~255;    // CB size is required to be 256-byte aligned.
m_device->CreateConstantBufferView(&cbvDesc, m_cbvHeap->GetCPUDescriptorHandleForHeapStart());
```

## Sampler

To create a sample, fill out a [**D3D12_SAMPLER_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_sampler_desc) structure:

``` syntax
typedef struct D3D12_SAMPLER_DESC
{
    D3D12_FILTER Filter;
    D3D12_TEXTURE_ADDRESS_MODE AddressU;
    D3D12_TEXTURE_ADDRESS_MODE AddressV;
    D3D12_TEXTURE_ADDRESS_MODE AddressW;
    FLOAT MipLODBias;
    UINT MaxAnisotropy;
    D3D12_COMPARISON_FUNC ComparisonFunc;
    FLOAT BorderColor[4]; // RGBA
    FLOAT MinLOD;
    FLOAT MaxLOD;
} D3D12_SAMPLER_DESC;
```

To fill out this structure, refer to the following enums:

-   [**D3D12_FILTER**](/windows/win32/api/d3d12/ne-d3d12-d3d12_filter)
-   [**D3D12_FILTER_TYPE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_filter_type)
-   [**D3D12_FILTER_REDUCTION_TYPE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_filter_reduction_type)
-   [**D3D12_TEXTURE_ADDRESS_MODE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_texture_address_mode)
-   [**D3D12_COMPARISON_FUNC**](/windows/win32/api/d3d12/ne-d3d12-d3d12_comparison_func)

Finally, call [**ID3D12Device::CreateSampler**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createsampler).

For example,

```cpp
// Describe and create a sampler.
D3D12_SAMPLER_DESC samplerDesc = {};
samplerDesc.Filter = D3D12_FILTER_MIN_MAG_MIP_LINEAR;
samplerDesc.AddressU = D3D12_TEXTURE_ADDRESS_MODE_WRAP;
samplerDesc.AddressV = D3D12_TEXTURE_ADDRESS_MODE_WRAP;
samplerDesc.AddressW = D3D12_TEXTURE_ADDRESS_MODE_WRAP;
samplerDesc.MinLOD = 0;
samplerDesc.MaxLOD = D3D12_FLOAT32_MAX;
samplerDesc.MipLODBias = 0.0f;
samplerDesc.MaxAnisotropy = 1;
samplerDesc.ComparisonFunc = D3D12_COMPARISON_FUNC_ALWAYS;
m_device->CreateSampler(&samplerDesc, m_samplerHeap->GetCPUDescriptorHandleForHeapStart());
```

## Unordered access view

To create an unordered access view, fill out a [**D3D12_UNORDERED_ACCESS_VIEW_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_unordered_access_view_desc) structure:

``` syntax
typedef struct D3D12_UNORDERED_ACCESS_VIEW_DESC
{
    DXGI_FORMAT Format;
    D3D12_UAV_DIMENSION ViewDimension;

    union
    {
        D3D12_BUFFER_UAV Buffer;
        D3D12_TEX1D_UAV Texture1D;
        D3D12_TEX1D_ARRAY_UAV Texture1DArray;
        D3D12_TEX2D_UAV Texture2D;
        D3D12_TEX2D_ARRAY_UAV Texture2DArray;
        D3D12_TEX3D_UAV Texture3D;
    };
} D3D12_UNORDERED_ACCESS_VIEW_DESC;
```

The *ViewDimension* field is set to zero or one value of the [**D3D12_BUFFER_UAV_FLAGS**](/windows/win32/api/d3d12/ne-d3d12-d3d12_buffer_uav_flags) enum.

Refer to the following enums and structures:

-   [**DXGI_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)
-   [**D3D12_BUFFER_UAV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_buffer_uav)
-   [**D3D12_TEX1D_UAV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex1d_uav)
-   [**D3D12_TEX1D_ARRAY_UAV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex1d_array_uav)
-   [**D3D12_TEX2D_UAV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2d_uav)
-   [**D3D12_TEX2D_ARRAY_UAV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2d_array_uav)
-   [**D3D12_TEX3D_UAV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex3d_uav)

*StructureByteStride* is part of buffer UAVs; whereas in Direct3D 11 it was a property of the resource. If the stride is non-zero, then that indicates a structured buffer view, and the format must be set to **DXGI_FORMAT_UNKNOWN**.

Finally call [**ID3D12Device::CreateUnorderedAccessView**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createunorderedaccessview).

For example,

```cpp
// Create the unordered access views (UAVs) that store the results of the compute work.
CD3DX12_CPU_DESCRIPTOR_HANDLE processedCommandsHandle(m_cbvSrvUavHeap->GetCPUDescriptorHandleForHeapStart(), ProcessedCommandsOffset, m_cbvSrvUavDescriptorSize);
for (UINT frame = 0; frame < FrameCount; frame++)
{
    // Allocate a buffer large enough to hold all of the indirect commands
    // for a single frame as well as a UAV counter.
    commandBufferDesc = CD3DX12_RESOURCE_DESC::Buffer(CommandBufferSizePerFrame + sizeof(UINT), D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS);
    ThrowIfFailed(m_device->CreateCommittedResource(
        &CD3DX12_HEAP_PROPERTIES(D3D12_HEAP_TYPE_DEFAULT),
        D3D12_HEAP_FLAG_NONE,
        &commandBufferDesc,
        D3D12_RESOURCE_STATE_COPY_DEST,
        nullptr,
        IID_PPV_ARGS(&m_processedCommandBuffers[frame])));

    D3D12_UNORDERED_ACCESS_VIEW_DESC uavDesc = {};
    uavDesc.Format = DXGI_FORMAT_UNKNOWN;
    uavDesc.ViewDimension = D3D12_UAV_DIMENSION_BUFFER;
    uavDesc.Buffer.FirstElement = 0;
    uavDesc.Buffer.NumElements = TriangleCount;
    uavDesc.Buffer.StructureByteStride = sizeof(IndirectCommand);
    uavDesc.Buffer.CounterOffsetInBytes = CommandBufferSizePerFrame;
    uavDesc.Buffer.Flags = D3D12_BUFFER_UAV_FLAG_NONE;

    m_device->CreateUnorderedAccessView(            
        m_processedCommandBuffers[frame].Get(),
        m_processedCommandBuffers[frame].Get(),
        &uavDesc,
        processedCommandsHandle);

    processedCommandsHandle.Offset(CbvSrvUavDescriptorCountPerFrame, m_cbvSrvUavDescriptorSize);
}

// Allocate a buffer that can be used to reset the UAV counters and initialize it to 0.
ThrowIfFailed(m_device->CreateCommittedResource(
    &CD3DX12_HEAP_PROPERTIES(D3D12_HEAP_TYPE_UPLOAD),
    D3D12_HEAP_FLAG_NONE,
    &CD3DX12_RESOURCE_DESC::Buffer(sizeof(UINT)),
    D3D12_RESOURCE_STATE_GENERIC_READ,
    
    nullptr,
    IID_PPV_ARGS(&m_processedCommandBufferCounterReset)));

UINT8* pMappedCounterReset = nullptr;
CD3DX12_RANGE readRange(0, 0);        // We do not intend to read from this resource on the CPU.
ThrowIfFailed(m_processedCommandBufferCounterReset->Map(0, &readRange, reinterpret_cast<void**>(&pMappedCounterReset)));
ZeroMemory(pMappedCounterReset, sizeof(UINT));
m_processedCommandBufferCounterReset->Unmap(0, nullptr);
```

## Stream output view

To create a stream output view, fill out a [**D3D12_STREAM_OUTPUT_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_stream_output_desc) structure.

``` syntax
typedef struct D3D12_STREAM_OUTPUT_DESC  
    {  
    _Field_size_full_(NumEntries)  const D3D12_SO_DECLARATION_ENTRY *pSODeclaration;  
    UINT NumEntries;  
    _Field_size_full_(NumStrides)  const UINT *pBufferStrides;  
    UINT NumStrides;  
    UINT RasterizedStream;  
    }   D3D12_STREAM_OUTPUT_DESC;  
```

Then call [**ID3D12GraphicsCommandList::SOSetTargets**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-sosettargets).

## Render target view

To create a render target view, fill out a [**D3D12_RENDER_TARGET_VIEW_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_render_target_view_desc) structure.

``` syntax
typedef struct D3D12_RENDER_TARGET_VIEW_DESC
{
    DXGI_FORMAT Format;
    D3D12_RTV_DIMENSION ViewDimension;

    union
    {
        D3D12_BUFFER_RTV Buffer;
        D3D12_TEX1D_RTV Texture1D;
        D3D12_TEX1D_ARRAY_RTV Texture1DArray;
        D3D12_TEX2D_RTV Texture2D;
        D3D12_TEX2D_ARRAY_RTV Texture2DArray;
        D3D12_TEX2DMS_RTV Texture2DMS;
        D3D12_TEX2DMS_ARRAY_RTV Texture2DMSArray;
        D3D12_TEX3D_RTV Texture3D;
    };
} D3D12_RENDER_TARGET_VIEW_DESC;
```

The *ViewDimension* field is set to zero, or one value of the [**D3D12_RTV_DIMENSION**](/windows/win32/api/d3d12/ne-d3d12-d3d12_rtv_dimension) enum.

Refer to the following enums and structures:

-   [**DXGI_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)
-   [**D3D12_BUFFER_RTV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_buffer_rtv)
-   [**D3D12_TEX1D_RTV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex1d_rtv)
-   [**D3D12_TEX1D_ARRAY_RTV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex1d_array_rtv)
-   [**D3D12_TEX2D_RTV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2d_rtv)
-   [**D3D12_TEX2DMS_RTV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2dms_rtv)
-   [**D3D12_TEX2D_ARRAY_RTV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2d_array_rtv)
-   [**D3D12_TEX2DMS_ARRAY_RTV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2dms_array_rtv)
-   [**D3D12_TEX3D_RTV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex3d_rtv)

Finally, call [**ID3D12Device::CreateRenderTargetView**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createrendertargetview).

For example,

```cpp
// Create descriptor heaps.
{
    // Describe and create a render target view (RTV) descriptor heap.
    D3D12_DESCRIPTOR_HEAP_DESC rtvHeapDesc = {};
    rtvHeapDesc.NumDescriptors = FrameCount;
    rtvHeapDesc.Type = D3D12_DESCRIPTOR_HEAP_TYPE_RTV;
    rtvHeapDesc.Flags = D3D12_DESCRIPTOR_HEAP_FLAG_NONE;
    ThrowIfFailed(m_device->CreateDescriptorHeap(&rtvHeapDesc, IID_PPV_ARGS(&m_rtvHeap)));

    m_rtvDescriptorSize = m_device->GetDescriptorHandleIncrementSize(D3D12_DESCRIPTOR_HEAP_TYPE_RTV);
}

// Create frame resources.
{
    CD3DX12_CPU_DESCRIPTOR_HANDLE rtvHandle(m_rtvHeap->GetCPUDescriptorHandleForHeapStart());

    // Create a RTV for each frame.
    for (UINT n = 0; n < FrameCount; n++)
    {
        ThrowIfFailed(m_swapChain->GetBuffer(n, IID_PPV_ARGS(&m_renderTargets[n])));
        m_device->CreateRenderTargetView(m_renderTargets[n].Get(), nullptr, rtvHandle);
        rtvHandle.Offset(1, m_rtvDescriptorSize);
    }
```

## Depth stencil view

To create a depth stencil view, fill out a [**D3D12_DEPTH_STENCIL_VIEW_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_depth_stencil_view_desc) structure:

``` syntax
typedef struct D3D12_DEPTH_STENCIL_VIEW_DESC  
    {  
    DXGI_FORMAT Format;  
    D3D12_DSV_DIMENSION ViewDimension;  
    D3D12_DSV_FLAGS Flags;  
    union   
        {  
        D3D12_TEX1D_DSV Texture1D;  
        D3D12_TEX1D_ARRAY_DSV Texture1DArray;  
        D3D12_TEX2D_DSV Texture2D;  
        D3D12_TEX2D_ARRAY_DSV Texture2DArray;  
        D3D12_TEX2DMS_DSV Texture2DMS;  
        D3D12_TEX2DMS_ARRAY_DSV Texture2DMSArray;  
        }   ;  
    }   D3D12_DEPTH_STENCIL_VIEW_DESC;  
```

The *ViewDimension* field is set to zero or one value of the [**D3D12_DSV_DIMENSION**](/windows/win32/api/d3d12/ne-d3d12-d3d12_dsv_dimension) enum. Refer to the [**D3D12_DSV_FLAGS**](/windows/win32/api/d3d12/ne-d3d12-d3d12_dsv_flags) enum for the flag settings.

Refer to the following enums and structures:

-   [**DXGI_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)
-   [**D3D12_TEX1D_DSV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex1d_dsv)
-   [**D3D12_TEX1D_ARRAY_DSV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex1d_array_dsv)
-   [**D3D12_TEX2D_DSV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2d_dsv)
-   [**D3D12_TEX2D_ARRAY_DSV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2d_array_dsv)
-   [**D3D12_TEX2DMS_DSV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2dms_dsv)
-   [**D3D12_TEX2DMS_ARRAY_DSV**](/windows/win32/api/d3d12/ns-d3d12-d3d12_tex2dms_array_dsv)

Finally, call [**ID3D12Device::CreateDepthStencilView**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createdepthstencilview).

For example,

```cpp
// Create the depth stencil view.
{
    D3D12_DEPTH_STENCIL_VIEW_DESC depthStencilDesc = {};
    depthStencilDesc.Format = DXGI_FORMAT_D32_FLOAT;
    depthStencilDesc.ViewDimension = D3D12_DSV_DIMENSION_TEXTURE2D;
    depthStencilDesc.Flags = D3D12_DSV_FLAG_NONE;

    D3D12_CLEAR_VALUE depthOptimizedClearValue = {};
    depthOptimizedClearValue.Format = DXGI_FORMAT_D32_FLOAT;
    depthOptimizedClearValue.DepthStencil.Depth = 1.0f;
    depthOptimizedClearValue.DepthStencil.Stencil = 0;

    ThrowIfFailed(m_device->CreateCommittedResource(
        &CD3DX12_HEAP_PROPERTIES(D3D12_HEAP_TYPE_DEFAULT),
        D3D12_HEAP_FLAG_NONE,
        &CD3DX12_RESOURCE_DESC::Tex2D(DXGI_FORMAT_D32_FLOAT, m_width, m_height, 1, 0, 1, 0, D3D12_RESOURCE_FLAG_ALLOW_DEPTH_STENCIL),
        D3D12_RESOURCE_STATE_DEPTH_WRITE,
        &depthOptimizedClearValue,
        IID_PPV_ARGS(&m_depthStencil)
        ));

    m_device->CreateDepthStencilView(m_depthStencil.Get(), &depthStencilDesc, m_dsvHeap->GetCPUDescriptorHandleForHeapStart());
}
```

## Related topics

* [Descriptors](descriptors.md)
* [Descriptor heaps](descriptor-heaps.md)
