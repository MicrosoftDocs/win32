---
title: CD3DX12\_RASTERIZER\_DESC structure
description: A helper structure to enable easy initialization of a D3D12\_RASTERIZER\_DESC structure.
ms.assetid: '28AA8256-1CAF-484F-B219-0F0461BA947C'
keywords: ["CD3DX12_RASTERIZER_DESC structure"]
topic_type:
- apiref
api_name:
- CD3DX12_RASTERIZER_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
---

# CD3DX12\_RASTERIZER\_DESC structure

A helper structure to enable easy initialization of a [**D3D12\_RASTERIZER\_DESC**](d3d12-rasterizer-desc.md) structure.

## Syntax


```C++
struct CD3DX12_RASTERIZER_DESC  : public D3D12_RASTERIZER_DESC{
   CD3DX12_RASTERIZER_DESC();
   explicit CD3DX12_RASTERIZER_DESC(const D3D12_RASTERIZER_DESC&amp; o);
   explicit CD3DX12_RASTERIZER_DESC(CD3DX12_DEFAULT);
   explicit CD3DX12_RASTERIZER_DESC(D3D12_FILL_MODE fillMode, D3D12_CULL_MODE cullMode, BOOL frontCounterClockwise, INT depthBias, FLOAT depthBiasClamp, FLOAT slopeScaledDepthBias, BOOL depthClipEnable, BOOL multisampleEnable, BOOL antialiasedLineEnable, UINT forcedSampleCount, D3D12_CONSERVATIVE_RASTERIZATION_MODE conservativeRaster);
   ~CD3DX12_RASTERIZER_DESC();
   operator const D3D12_RASTERIZER_DESC&amp;() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_RASTERIZER\_DESC()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_RASTERIZER\_DESC.

</dd> <dt>

**explicit CD3DX12\_RASTERIZER\_DESC(const D3D12\_RASTERIZER\_DESC& o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_RASTERIZER\_DESC, initialized with the contents of another [**D3D12\_RASTERIZER\_DESC**](d3d12-rasterizer-desc.md) structure.

</dd> <dt>

**explicit CD3DX12\_RASTERIZER\_DESC(CD3DX12\_DEFAULT)**
</dt> <dd>

Creates a new instance of a CD3DX12\_RASTERIZER\_DESC, initialized with default parameters.

``` syntax
        FillMode = D3D12_FILL_MODE_SOLID;  
        CullMode = D3D12_CULL_MODE_BACK;  
        FrontCounterClockwise = FALSE;  
        DepthBias = D3D12_DEFAULT_DEPTH_BIAS;  
        DepthBiasClamp = D3D12_DEFAULT_DEPTH_BIAS_CLAMP;  
        SlopeScaledDepthBias = D3D12_DEFAULT_SLOPE_SCALED_DEPTH_BIAS;  
        DepthClipEnable = TRUE;  
        MultisampleEnable = FALSE;  
        AntialiasedLineEnable = FALSE;  
        ForcedSampleCount = 0;  
        ConservativeRaster = D3D12_CONSERVATIVE_RASTERIZATION_MODE_OFF;  
```

</dd> <dt>

**explicit CD3DX12\_RASTERIZER\_DESC(D3D12\_FILL\_MODE fillMode, D3D12\_CULL\_MODE cullMode, BOOL frontCounterClockwise, INT depthBias, FLOAT depthBiasClamp, FLOAT slopeScaledDepthBias, BOOL depthClipEnable, BOOL multisampleEnable, BOOL antialiasedLineEnable, UINT forcedSampleCount, D3D12\_CONSERVATIVE\_RASTERIZATION\_MODE conservativeRaster)**
</dt> <dd>

Creates a new instance of a CD3DX12\_RASTERIZER\_DESC, initializing the following parameters:

[**D3D12\_FILL\_MODE**](d3d12-fill-mode.md) fillMode

[**D3D12\_CULL\_MODE**](d3d12-cull-mode.md) cullMode

BOOL frontCounterClockwise

INT depthBias

FLOAT depthBiasClamp

FLOAT slopeScaledDepthBias

BOOL depthClipEnable

BOOL multisampleEnable

BOOL antialiasedLineEnable

UINT forcedSampleCount

[**D3D12\_CONSERVATIVE\_RASTERIZATION\_MODE**](d3d12-conservative-rasterization-mode.md) conservativeRaster

</dd> <dt>

**~CD3DX12\_RASTERIZER\_DESC()**
</dt> <dd>

Destroys an instance of a CD3DX12\_RASTERIZER\_DESC.

</dd> <dt>

**operator const D3D12\_RASTERIZER\_DESC&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_RASTERIZER\_DESC**](d3d12-rasterizer-desc.md)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





