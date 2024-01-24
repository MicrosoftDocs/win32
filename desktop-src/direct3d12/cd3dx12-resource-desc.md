---
title: CD3DX12_RESOURCE_DESC structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_RESOURCE\_DESC structure.
ms.assetid: F18D41BE-8AEF-444E-AC8B-EC57C63BF083
keywords:
- CD3DX12_RESOURCE_DESC structure
topic_type:
- apiref
api_name:
- CD3DX12_RESOURCE_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_RESOURCE\_DESC structure

A helper structure to enable easy initialization of a [**D3D12\_RESOURCE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_desc) structure.

## Syntax


```C++
struct CD3DX12_RESOURCE_DESC  : public D3D12_RESOURCE_DESC{
                        CD3DX12_RESOURCE_DESC();
                        explicit CD3DX12_RESOURCE_DESC(const D3D12_RESOURCE_DESC& o);
                        CD3DX12_RESOURCE_DESC(D3D12_RESOURCE_DIMENSION dimension, UINT64 alignment, UINT64 width, UINT height, UINT16 depthOrArraySize, UINT16 mipLevels, DXGI_FORMAT format, UINT sampleCount, UINT sampleQuality, D3D12_TEXTURE_LAYOUT layout, D3D12_RESOURCE_FLAGS flags);
  CD3DX12_RESOURCE_DESC static inline Buffer(const D3D12_RESOURCE_ALLOCATION_INFO& resAllocInfo, D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE);
  CD3DX12_RESOURCE_DESC static inline Buffer(UINT64 width, D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE, UINT64 alignment = 0);
  CD3DX12_RESOURCE_DESC static inline Tex1D(DXGI_FORMAT format, UINT64 width, UINT16 arraySize = 1, UINT16 mipLevels = 0, D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE, D3D12_TEXTURE_LAYOUT layout = D3D12_TEXTURE_LAYOUT_UNKNOWN, UINT64 alignment = 0);
  CD3DX12_RESOURCE_DESC static inline Tex2D(DXGI_FORMAT format, UINT64 width, UINT height, UINT16 arraySize = 1, UINT16 mipLevels = 0, UINT sampleCount = 1, UINT sampleQuality = 0, D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE, D3D12_TEXTURE_LAYOUT layout = D3D12_TEXTURE_LAYOUT_UNKNOWN, UINT64 alignment = 0);
  CD3DX12_RESOURCE_DESC static inline Tex3D(DXGI_FORMAT format, UINT64 width, UINT height, UINT16 depth, UINT16 mipLevels = 0, D3D12_RESOURCE_FLAGS flags = D3D12_RESOURCE_FLAG_NONE, D3D12_TEXTURE_LAYOUT layout = D3D12_TEXTURE_LAYOUT_UNKNOWN, UINT64 alignment = 0);
  UINT16                inline Depth() const;
  UINT16                inline ArraySize() const;
  UINT8                 inline PlaneCount(ID3D12Device* pDevice) const;
  UINT                  inline Subresources(ID3D12Device* pDevice) const;
  UINT                  inline CalcSubresource(UINT MipSlice, UINT ArraySlice, UINT PlaneSlice);
                        operator const D3D12_RESOURCE_DESC&() const;
                        operator == (const D3D12_RESOURCE_DESC& l, const D3D12_RESOURCE_DESC& r);
                        operator !=  (const D3D12_RESOURCE_DESC& l, const D3D12_RESOURCE_DESC& r);
};
```



## Members

<dl> <dt>

**CD3DX12\_RESOURCE\_DESC()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_RESOURCE\_DESC.

</dd> <dt>

**explicit CD3DX12\_RESOURCE\_DESC(const D3D12\_RESOURCE\_DESC& o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_RESOURCE\_DESC, initialized with the contents of another [**D3D12\_RESOURCE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_desc) structure.

</dd> <dt>

**CD3DX12\_RESOURCE\_DESC(D3D12\_RESOURCE\_DIMENSION dimension, UINT64 alignment, UINT64 width, UINT height, UINT16 depthOrArraySize, UINT16 mipLevels, DXGI\_FORMAT format, UINT sampleCount, UINT sampleQuality, D3D12\_TEXTURE\_LAYOUT layout, D3D12\_RESOURCE\_FLAGS flags)**
</dt> <dd>

Creates a new instance of a CD3DX12\_RESOURCE\_DESC, initializing the following parameters:

[**D3D12\_RESOURCE\_DIMENSION**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_dimension) dimension

UINT64 alignment

UINT64 width

UINT height

UINT16 depthOrArraySize

UINT16 mipLevels

[**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) format

UINT sampleCount

UINT sampleQuality

[**D3D12\_TEXTURE\_LAYOUT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_texture_layout) layout

[**D3D12\_RESOURCE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_flags) flags

</dd> <dt>

**static inline Buffer(const D3D12\_RESOURCE\_ALLOCATION\_INFO& resAllocInfo, D3D12\_RESOURCE\_FLAGS flags = D3D12\_RESOURCE\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_RESOURCE\_ALLOCATION\_INFO**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_allocation_info)& resAllocInfo

(opt) [**D3D12\_RESOURCE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_flags) flags = D3D12\_RESOURCE\_FLAG\_NONE

</dd> <dt>

**static inline Buffer(UINT64 width, D3D12\_RESOURCE\_FLAGS flags = D3D12\_RESOURCE\_FLAG\_NONE, UINT64 alignment = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT64 width

(opt) [**D3D12\_RESOURCE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_flags) flags = D3D12\_RESOURCE\_FLAG\_NONE

(opt) UINT64 alignment = 0

</dd> <dt>

**static inline Tex1D(DXGI\_FORMAT format, UINT64 width, UINT16 arraySize = 1, UINT16 mipLevels = 0, D3D12\_RESOURCE\_FLAGS flags = D3D12\_RESOURCE\_FLAG\_NONE, D3D12\_TEXTURE\_LAYOUT layout = D3D12\_TEXTURE\_LAYOUT\_UNKNOWN, UINT64 alignment = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) format

UINT64 width

(opt) UINT16 arraySize = 1

(opt) UINT16 mipLevels = 0

(opt) [**D3D12\_RESOURCE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_flags) flags = D3D12\_RESOURCE\_FLAG\_NONE

(opt) [**D3D12\_TEXTURE\_LAYOUT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_texture_layout) layout = D3D12\_TEXTURE\_LAYOUT\_UNKNOWN

(opt) UINT64 alignment = 0

</dd> <dt>

**static inline Tex2D(DXGI\_FORMAT format, UINT64 width, UINT height, UINT16 arraySize = 1, UINT16 mipLevels = 0, UINT sampleCount = 1, UINT sampleQuality = 0, D3D12\_RESOURCE\_FLAGS flags = D3D12\_RESOURCE\_FLAG\_NONE, D3D12\_TEXTURE\_LAYOUT layout = D3D12\_TEXTURE\_LAYOUT\_UNKNOWN, UINT64 alignment = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) format

UINT64 width

UINT height

(opt) UINT16 arraySize = 1

(opt) UINT16 mipLevels = 0

(opt) UINT sampleCount = 1

(opt) UINT sampleQuality = 0

(opt) [**D3D12\_RESOURCE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_flags) flags = D3D12\_RESOURCE\_FLAG\_NONE

(opt) [**D3D12\_TEXTURE\_LAYOUT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_texture_layout) layout = D3D12\_TEXTURE\_LAYOUT\_UNKNOWN

(opt) UINT64 alignment = 0

</dd> <dt>

**static inline Tex3D(DXGI\_FORMAT format, UINT64 width, UINT height, UINT16 depth, UINT16 mipLevels = 0, D3D12\_RESOURCE\_FLAGS flags = D3D12\_RESOURCE\_FLAG\_NONE, D3D12\_TEXTURE\_LAYOUT layout = D3D12\_TEXTURE\_LAYOUT\_UNKNOWN, UINT64 alignment = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**DXGI\_FORMAT**](/windows/desktop/api/dxgiformat/ne-dxgiformat-dxgi_format) format

UINT64 width

UINT height

UINT16 depth

(opt) UINT16 mipLevels = 0

(opt) [**D3D12\_RESOURCE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_flags) flags = D3D12\_RESOURCE\_FLAG\_NONE

(opt) [**D3D12\_TEXTURE\_LAYOUT**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_texture_layout) layout = D3D12\_TEXTURE\_LAYOUT\_UNKNOWN

(opt) UINT64 alignment = 0

</dd> <dt>

**inline Depth() const**
</dt> <dd>

If Dimension == [**D3D12\_RESOURCE\_DIMENSION**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_dimension)\_TEXTURE3D, returns DepthOrArraySize. If Dimension != D3D12\_RESOURCE\_DIMENSION\_TEXTURE3D, returns 1.

</dd> <dt>

**inline ArraySize() const**
</dt> <dd>

If Dimension != D3D12\_RESOURCE\_DIMENSION\_TEXTURE3D, returns DepthOrArraySize. If Dimension == D3D12\_RESOURCE\_DIMENSION\_TEXTURE3D, returns 1. See [**D3D12\_RESOURCE\_DIMENSION**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_dimension)\_TEXTURE3D.

</dd> <dt>

**inline PlaneCount(ID3D12Device\* pDevice) const**
</dt> <dd>

Returns D3D12GetFormatPlaneCount(pDevice, Format). See [**D3D12GetFormatPlaneCount**](d3d12getformatplanecount.md) and [**ID3D12Device**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device).

</dd> <dt>

**inline Subresources(ID3D12Device\* pDevice) const**
</dt> <dd>

Returns the number of subresources, calculated as MipLevels \* ArraySize() \* PlaneCount(pDevice).

</dd> <dt>

**inline CalcSubresource(UINT MipSlice, UINT ArraySlice, UINT PlaneSlice)**
</dt> <dd>

Calculates a subresource index, by using [**D3D12CalcSubresource**](d3d12calcsubresource.md).

</dd> <dt>

**operator const D3D12\_RESOURCE\_DESC&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> <dt>

**operator == (const D3D12\_RESOURCE\_DESC& l, const D3D12\_RESOURCE\_DESC& r)**
</dt> <dd>

Returns true if all members of each structure are identical.

</dd> <dt>

**operator != (const D3D12\_RESOURCE\_DESC& l, const D3D12\_RESOURCE\_DESC& r)**
</dt> <dd>

Returns false if all members of each structure are identical.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_RESOURCE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_resource_desc)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

