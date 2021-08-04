---
title: CD3DX12_RESOURCE_DESC1 structure (D3dx12.h)
description: A helper structure to enable easy initialization of a [**D3DX12_RESOURCE_DESC1**](/windows/win32/api/d3d12/ns-d3d12-d3d12_view_instancing_desc) structure.
keywords:
- CD3DX12_RESOURCE_DESC1 structure
topic_type:
- apiref
api_name:
- CD3DX12_RESOURCE_DESC1
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 07/29/2021
---

# CD3DX12_RESOURCE_DESC1 structure

A helper structure to enable easy initialization of a [**D3DX12_RESOURCE_DESC1**](/windows/win32/api/d3d12/D3DX12_RESOURCE_DESC1/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_desc1) structure.

## Syntax

```cpp
struct CD3DX12_RESOURCE_DESC1 : public D3D12_RESOURCE_DESC1
{
    CD3DX12_RESOURCE_DESC1();
    explicit CD3DX12_RESOURCE_DESC1(const D3D12_RESOURCE_DESC1& o) noexcept;
    CD3DX12_RESOURCE_DESC1(
        D3D12_RESOURCE_DIMENSION dimension,
        UINT64 alignment,
        UINT64 width,
        UINT height,
        UINT16 depthOrArraySize,
        UINT16 mipLevels,
        DXGI_FORMAT format,
        UINT sampleCount,
        UINT sampleQuality,
        D3D12_TEXTURE_LAYOUT layout,
        D3D12_RESOURCE_FLAGS flags,
        UINT samplerFeedbackMipRegionWidth = 0,
        UINT samplerFeedbackMipRegionHeight = 0,
        UINT samplerFeedbackMipRegionDepth = 0) noexcept;
    static inline CD3DX12_RESOURCE_DESC1 Buffer(
        const D3D12_RESOURCE_ALLOCATION_INFO& resAllocInfo,
        D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE) noexcept;
    static inline CD3DX12_RESOURCE_DESC1 Buffer(
        UINT64 width,
        D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE,
        UINT64 alignment = 0) noexcept;
    static inline CD3DX12_RESOURCE_DESC1 Tex1D(
        DXGI_FORMAT format,
        UINT64 width,
        UINT16 arraySize = 1,
        UINT16 mipLevels = 0,
        D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE,
        D3D12_TEXTURE_LAYOUT layout = D3D12_TEXTURE_LAYOUT_UNKNOWN,
        UINT64 alignment = 0) noexcept;
    static inline CD3DX12_RESOURCE_DESC1 Tex2D(
        DXGI_FORMAT format,
        UINT64 width,
        UINT height,
        UINT16 arraySize = 1,
        UINT16 mipLevels = 0,
        UINT sampleCount = 1,
        UINT sampleQuality = 0,
        D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE,
        D3D12_TEXTURE_LAYOUT layout = D3D12_TEXTURE_LAYOUT_UNKNOWN,
        UINT64 alignment = 0,
        UINT samplerFeedbackMipRegionWidth = 0,
        UINT samplerFeedbackMipRegionHeight = 0,
        UINT samplerFeedbackMipRegionDepth = 0) noexcept;
    static inline CD3DX12_RESOURCE_DESC1 Tex3D(
        DXGI_FORMAT format,
        UINT64 width,
        UINT height,
        UINT16 depth,
        UINT16 mipLevels = 0,
        D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE,
        D3D12_TEXTURE_LAYOUT layout = D3D12_TEXTURE_LAYOUT_UNKNOWN,
        UINT64 alignment = 0) noexcept;
    inline UINT16 Depth() const noexcept;
    inline UINT16 ArraySize() const noexcept;
    inline UINT8 PlaneCount(_In_ ID3D12Device* pDevice) const noexcept;
    inline UINT Subresources(_In_ ID3D12Device* pDevice) const noexcept;
    inline UINT CalcSubresource(UINT MipSlice, UINT ArraySlice, UINT PlaneSlice) noexcept;
};
inline bool operator==(const D3D12_RESOURCE_DESC1& l, const D3D12_RESOURCE_DESC1& r) noexcept;
inline bool operator!=(const D3D12_RESOURCE_DESC1& l, const D3D12_RESOURCE_DESC1& r) noexcept;
```

## Members

### CD3DX12_RESOURCE_DESC1

Default constructor. Creates a new, uninitialized, instance of a **CD3DX12_RESOURCE_DESC1**.

### CD3DX12_RESOURCE_DESC1(const D3D12_RESOURCE_DESC1&)

Constructor that creates a new instance of a **CD3DX12_RESOURCE_DESC1** initialized with the contents of a [**D3DX12_RESOURCE_DESC1**](/windows/win32/api/d3d12/D3DX12_RESOURCE_DESC1/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_desc1) structure.

### CD3DX12_RESOURCE_DESC1(D3D12_RESOURCE_DIMENSION, UINT64, UINT64, UINT, UINT16, UINT16, DXGI_FORMAT, UINT, UINT, D3D12_TEXTURE_LAYOUT, D3D12_RESOURCE_FLAGS, UINT = 0, UINT = 0, UINT = 0)

Constructor that creates a new instance of a **CD3DX12_RESOURCE_DESC1** initialized with the parameters passed to it.

### Buffer(const D3D12_RESOURCE_ALLOCATION_INFO&, D3D12_RESOURCE_FLAGS = D3D12_RESOURCE_FLAG_NONE)

A static function that constructs and returns a new instance of a **CD3DX12_RESOURCE_DESC1** initialized with these values.

|Data member|value|
|-|-|
|Dimension|D3D12_RESOURCE_DIMENSION_BUFFER|
|Alignment|*resAllocInfo*.Alignment|
|Width|*resAllocInfo*.SizeInBytes|
|Height|1|
|DepthOrArraySize|1|
|MipLevels|1|
|Format|DXGI_FORMAT_UNKNOWN|
|SampleDesc.Count|1|
|SampleDesc.Quality|0|
|Layout|D3D12_TEXTURE_LAYOUT_ROW_MAJOR|
|Flags|*flags*|
|SamplerFeedbackMipRegion.Width|0|
|SamplerFeedbackMipRegion.Height|0|
|SamplerFeedbackMipRegion.Depth|0|

### Buffer(UINT64, D3D12_RESOURCE_FLAGS = D3D12_RESOURCE_FLAG_NONE, UINT64 = 0)

A static function that constructs and returns a new instance of a **CD3DX12_RESOURCE_DESC1** initialized with these values.

|Data member|value|
|-|-|
|Dimension|D3D12_RESOURCE_DIMENSION_BUFFER|
|Alignment|*alignment*|
|Width|*width*|
|Height|1|
|DepthOrArraySize|1|
|MipLevels|1|
|Format|DXGI_FORMAT_UNKNOWN|
|SampleDesc.Count|1|
|SampleDesc.Quality|0|
|Layout|D3D12_TEXTURE_LAYOUT_ROW_MAJOR|
|Flags|*flags*|
|SamplerFeedbackMipRegion.Width|0|
|SamplerFeedbackMipRegion.Height|0|
|SamplerFeedbackMipRegion.Depth|0|

### Tex1D(DXGI_FORMAT, UINT64, UINT16 = 1, UINT16 = 0, D3D12_RESOURCE_FLAGS D3D12_RESOURCE_FLAG_NONE, D3D12_TEXTURE_LAYOUT = D3D12_TEXTURE_LAYOUT_UNKNOWN, UINT64 = 0)

A static function that constructs and returns a new instance of a **CD3DX12_RESOURCE_DESC1** initialized with these values.

|Data member|value|
|-|-|
|Dimension|D3D12_RESOURCE_DIMENSION_TEXTURE1D|
|Alignment|*alignment*|
|Width|*width*|
|Height|1|
|DepthOrArraySize|*arraySize*|
|MipLevels|*mipLevels*|
|Format|*format*|
|SampleDesc.Count|1|
|SampleDesc.Quality|0|
|Layout|*layout*|
|Flags|*flags*|
|SamplerFeedbackMipRegion.Width|0|
|SamplerFeedbackMipRegion.Height|0|
|SamplerFeedbackMipRegion.Depth|0|

### Tex2D(DXGI_FORMAT, UINT64, UINT, UINT16 = 1, UINT16 = 0, UINT = 1, UINT = 0, D3D12_RESOURCE_FLAGS = D3D12_RESOURCE_FLAG_NONE, D3D12_TEXTURE_LAYOUT = D3D12_TEXTURE_LAYOUT_UNKNOWN, UINT64 = 0, UINT = 0, UINT = 0, UINT = 0)

A static function that constructs and returns a new instance of a **CD3DX12_RESOURCE_DESC1** initialized with these values.

|Data member|value|
|-|-|
|Dimension|D3D12_RESOURCE_DIMENSION_TEXTURE2D|
|Alignment|*alignment*|
|Width|*width*|
|Height|*height*|
|DepthOrArraySize|*arraySize*|
|MipLevels|*mipLevels*|
|Format|*format*|
|SampleDesc.Count|*sampleCount*|
|SampleDesc.Quality|*sampleQuality*|
|Layout|*layout*|
|Flags|*flags*|
|SamplerFeedbackMipRegion.Width|*samplerFeedbackMipRegionWidth*|
|SamplerFeedbackMipRegion.Height|*samplerFeedbackMipRegionHeight*|
|SamplerFeedbackMipRegion.Depth|*samplerFeedbackMipRegionDepth*|

### Tex3D(DXGI_FORMAT, UINT64, UINT, UINT16, UINT16 = 0, D3D12_RESOURCE_FLAGS = D3D12_RESOURCE_FLAG_NONE, D3D12_TEXTURE_LAYOUT = D3D12_TEXTURE_LAYOUT_UNKNOWN, UINT64 = 0)

A static function that constructs and returns a new instance of a **CD3DX12_RESOURCE_DESC1** initialized with these values.

|Data member|value|
|-|-|
|Dimension|D3D12_RESOURCE_DIMENSION_TEXTURE3D|
|Alignment|*alignment*|
|Width|*width*|
|Height|*height*|
|DepthOrArraySize|*depth*|
|MipLevels|*mipLevels*|
|Format|*format*|
|SampleDesc.Count|1|
|SampleDesc.Quality|0|
|Layout|*layout*|
|Flags|*flags*|
|SamplerFeedbackMipRegion.Width|0|
|SamplerFeedbackMipRegion.Height|0|
|SamplerFeedbackMipRegion.Depth|0|

### Depth

Returns a **UINT16** containing the depth of the resource.

### ArraySize

Returns a **UINT16** containing the array size of the resource.

### PlaneCount(ID3D12Device*)

Returns a **UINT8** containing the plane count for the resource's format.

### Subresources(ID3D12Device*)

Returns a **UINT** containing the number of subresources in the resource.

### CalcSubresource(UINT, UINT, UINT)

Caculates and returns a **UINT** containing a subresource index for the resource based on the parameters passed to it.

### operator==(const D3D12_RESOURCE_DESC1&, const D3D12_RESOURCE_DESC1&)

A free function that returns `true` if the two parameters are member-wise equal; otherwise `false`.

### operator!=(const D3D12_RESOURCE_DESC1&, const D3D12_RESOURCE_DESC1&)

A free function that returns `true` if the two parameters are member-wise not equal; otherwise `false`.

## Requirements

| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header | [D3dx12.h](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/master/Libraries/D3DX12) |

## See also

* [D3DX12_RESOURCE_DESC1](/windows/win32/api/d3d12/D3DX12_RESOURCE_DESC1/windows/win32/api/d3d12/ns-d3d12-d3d12_resource_desc1)
* [Helper structures for Direct3D 12](helper-structures-for-d3d12.md)
