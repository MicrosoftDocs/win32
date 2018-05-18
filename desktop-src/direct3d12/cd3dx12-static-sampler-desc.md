---
title: CD3DX12\_STATIC\_SAMPLER\_DESC structure
description: A helper structure to enable easy initialization of a D3D12\_STATIC\_SAMPLER\_DESC structure.
ms.assetid: 'C402415D-7BD5-4E23-82C9-B29B0B5669B8'
keywords: ["CD3DX12_STATIC_SAMPLER_DESC structure"]
topic_type:
- apiref
api_name:
- CD3DX12_STATIC_SAMPLER_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
---

# CD3DX12\_STATIC\_SAMPLER\_DESC structure

A helper structure to enable easy initialization of a [**D3D12\_STATIC\_SAMPLER\_DESC**](d3d12-static-sampler-desc.md) structure.

## Syntax


```C++
struct CD3DX12_STATIC_SAMPLER_DESC  : public D3D12_STATIC_SAMPLER_DESC{
       CD3DX12_STATIC_SAMPLER_DESC();
       explicit CD3DX12_STATIC_SAMPLER_DESC(const D3D12_STATIC_SAMPLER_DESC &amp;o);
       CD3DX12_STATIC_SAMPLER_DESC(UINT shaderRegister, D3D12_FILTER filter = D3D12_FILTER_ANISOTROPIC, D3D12_TEXTURE_ADDRESS_MODE addressU = D3D12_TEXTURE_ADDRESS_MODE_WRAP, D3D12_TEXTURE_ADDRESS_MODE addressV = D3D12_TEXTURE_ADDRESS_MODE_WRAP, D3D12_TEXTURE_ADDRESS_MODE addressW = D3D12_TEXTURE_ADDRESS_MODE_WRAP, FLOAT mipLODBias = 0, UINT maxAnisotropy = 16, D3D12_COMPARISON_FUNC comparisonFunc = D3D12_COMPARISON_FUNC_LESS_EQUAL, D3D12_STATIC_BORDER_COLOR borderColor = D3D12_STATIC_BORDER_COLOR_OPAQUE_WHITE, FLOAT minLOD = 0.f, FLOAT maxLOD = D3D12_FLOAT32_MAX, D3D12_SHADER_VISIBILITY shaderVisibility = D3D12_SHADER_VISIBILITY_ALL, UINT registerSpace = 0);
  void static inline Init(D3D12_STATIC_SAMPLER_DESC &amp;samplerDesc, UINT shaderRegister, D3D12_FILTER filter = D3D12_FILTER_ANISOTROPIC, D3D12_TEXTURE_ADDRESS_MODE addressU = D3D12_TEXTURE_ADDRESS_MODE_WRAP, D3D12_TEXTURE_ADDRESS_MODE addressV = D3D12_TEXTURE_ADDRESS_MODE_WRAP, D3D12_TEXTURE_ADDRESS_MODE addressW = D3D12_TEXTURE_ADDRESS_MODE_WRAP, FLOAT mipLODBias = 0, UINT maxAnisotropy = 16, D3D12_COMPARISON_FUNC comparisonFunc = D3D12_COMPARISON_FUNC_LESS_EQUAL, D3D12_STATIC_BORDER_COLOR borderColor = D3D12_STATIC_BORDER_COLOR_OPAQUE_WHITE, FLOAT minLOD = 0.f, FLOAT maxLOD = D3D12_FLOAT32_MAX, D3D12_SHADER_VISIBILITY shaderVisibility = D3D12_SHADER_VISIBILITY_ALL, UINT registerSpace = 0);
  void inline Init(UINT shaderRegister, D3D12_FILTER filter = D3D12_FILTER_ANISOTROPIC, D3D12_TEXTURE_ADDRESS_MODE addressU = D3D12_TEXTURE_ADDRESS_MODE_WRAP, D3D12_TEXTURE_ADDRESS_MODE addressV = D3D12_TEXTURE_ADDRESS_MODE_WRAP, D3D12_TEXTURE_ADDRESS_MODE addressW = D3D12_TEXTURE_ADDRESS_MODE_WRAP, FLOAT mipLODBias = 0, UINT maxAnisotropy = 16, D3D12_COMPARISON_FUNC comparisonFunc = D3D12_COMPARISON_FUNC_LESS_EQUAL, D3D12_STATIC_BORDER_COLOR borderColor = D3D12_STATIC_BORDER_COLOR_OPAQUE_WHITE, FLOAT minLOD = 0.f, FLOAT maxLOD = D3D12_FLOAT32_MAX, D3D12_SHADER_VISIBILITY shaderVisibility = D3D12_SHADER_VISIBILITY_ALL, UINT registerSpace = 0);
};
```



## Members

<dl> <dt>

**CD3DX12\_STATIC\_SAMPLER\_DESC()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_STATIC\_SAMPLER\_DESC.

</dd> <dt>

**explicit CD3DX12\_STATIC\_SAMPLER\_DESC(const D3D12\_STATIC\_SAMPLER\_DESC &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_STATIC\_SAMPLER\_DESC, initialized with the contents of another [**D3D12\_STATIC\_SAMPLER\_DESC**](d3d12-static-sampler-desc.md) structure.

</dd> <dt>

**CD3DX12\_STATIC\_SAMPLER\_DESC(UINT shaderRegister, D3D12\_FILTER filter = D3D12\_FILTER\_ANISOTROPIC, D3D12\_TEXTURE\_ADDRESS\_MODE addressU = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, D3D12\_TEXTURE\_ADDRESS\_MODE addressV = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, D3D12\_TEXTURE\_ADDRESS\_MODE addressW = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, FLOAT mipLODBias = 0, UINT maxAnisotropy = 16, D3D12\_COMPARISON\_FUNC comparisonFunc = D3D12\_COMPARISON\_FUNC\_LESS\_EQUAL, D3D12\_STATIC\_BORDER\_COLOR borderColor = D3D12\_STATIC\_BORDER\_COLOR\_OPAQUE\_WHITE, FLOAT minLOD = 0.f, FLOAT maxLOD = D3D12\_FLOAT32\_MAX, D3D12\_SHADER\_VISIBILITY shaderVisibility = D3D12\_SHADER\_VISIBILITY\_ALL, UINT registerSpace = 0)**
</dt> <dd>

Creates a new instance of a CD3DX12\_STATIC\_SAMPLER\_DESC, initializing the following parameters:

UINT shaderRegister

(opt) [**D3D12\_FILTER**](d3d12-filter.md) filter = D3D12\_FILTER\_ANISOTROPIC

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressU = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressV = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressW = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) FLOAT mipLODBias = 0

(opt) UINT maxAnisotropy = 16

(opt) [**D3D12\_COMPARISON\_FUNC**](d3d12-comparison-func.md) comparisonFunc = D3D12\_COMPARISON\_FUNC\_LESS\_EQUAL

(opt) [**D3D12\_STATIC\_BORDER\_COLOR**](d3d12-static-border-color.md) borderColor = D3D12\_STATIC\_BORDER\_COLOR\_OPAQUE\_WHITE

(opt) FLOAT minLOD = 0.f

(opt) FLOAT maxLOD = D3D12\_FLOAT32\_MAX

(opt) [**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) shaderVisibility = D3D12\_SHADER\_VISIBILITY\_ALL

(opt) UINT registerSpace = 0

</dd> <dt>

**static inline Init(D3D12\_STATIC\_SAMPLER\_DESC &samplerDesc, UINT shaderRegister, D3D12\_FILTER filter = D3D12\_FILTER\_ANISOTROPIC, D3D12\_TEXTURE\_ADDRESS\_MODE addressU = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, D3D12\_TEXTURE\_ADDRESS\_MODE addressV = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, D3D12\_TEXTURE\_ADDRESS\_MODE addressW = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, FLOAT mipLODBias = 0, UINT maxAnisotropy = 16, D3D12\_COMPARISON\_FUNC comparisonFunc = D3D12\_COMPARISON\_FUNC\_LESS\_EQUAL, D3D12\_STATIC\_BORDER\_COLOR borderColor = D3D12\_STATIC\_BORDER\_COLOR\_OPAQUE\_WHITE, FLOAT minLOD = 0.f, FLOAT maxLOD = D3D12\_FLOAT32\_MAX, D3D12\_SHADER\_VISIBILITY shaderVisibility = D3D12\_SHADER\_VISIBILITY\_ALL, UINT registerSpace = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_STATIC\_SAMPLER\_DESC**](d3d12-static-sampler-desc.md) &samplerDesc

UINT shaderRegister

(opt) [**D3D12\_FILTER**](d3d12-filter.md) filter = D3D12\_FILTER\_ANISOTROPIC

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressU = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressV = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressW = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) FLOAT mipLODBias = 0

(opt) UINT maxAnisotropy = 16

(opt) [**D3D12\_COMPARISON\_FUNC**](d3d12-comparison-func.md) comparisonFunc = D3D12\_COMPARISON\_FUNC\_LESS\_EQUAL

(opt) [**D3D12\_STATIC\_BORDER\_COLOR**](d3d12-static-border-color.md) borderColor = D3D12\_STATIC\_BORDER\_COLOR\_OPAQUE\_WHITE

(opt) FLOAT minLOD = 0.f

(opt) FLOAT maxLOD = D3D12\_FLOAT32\_MAX

(opt) [**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) shaderVisibility = D3D12\_SHADER\_VISIBILITY\_ALL

(opt) UINT registerSpace = 0

</dd> <dt>

**inline Init(UINT shaderRegister, D3D12\_FILTER filter = D3D12\_FILTER\_ANISOTROPIC, D3D12\_TEXTURE\_ADDRESS\_MODE addressU = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, D3D12\_TEXTURE\_ADDRESS\_MODE addressV = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, D3D12\_TEXTURE\_ADDRESS\_MODE addressW = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP, FLOAT mipLODBias = 0, UINT maxAnisotropy = 16, D3D12\_COMPARISON\_FUNC comparisonFunc = D3D12\_COMPARISON\_FUNC\_LESS\_EQUAL, D3D12\_STATIC\_BORDER\_COLOR borderColor = D3D12\_STATIC\_BORDER\_COLOR\_OPAQUE\_WHITE, FLOAT minLOD = 0.f, FLOAT maxLOD = D3D12\_FLOAT32\_MAX, D3D12\_SHADER\_VISIBILITY shaderVisibility = D3D12\_SHADER\_VISIBILITY\_ALL, UINT registerSpace = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT shaderRegister

(opt) [**D3D12\_FILTER**](d3d12-filter.md) filter = D3D12\_FILTER\_ANISOTROPIC

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressU = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressV = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) [**D3D12\_TEXTURE\_ADDRESS\_MODE**](d3d12-texture-address-mode.md) addressW = D3D12\_TEXTURE\_ADDRESS\_MODE\_WRAP

(opt) FLOAT mipLODBias = 0

(opt) UINT maxAnisotropy = 16

(opt) [**D3D12\_COMPARISON\_FUNC**](d3d12-comparison-func.md) comparisonFunc = D3D12\_COMPARISON\_FUNC\_LESS\_EQUAL

(opt) [**D3D12\_STATIC\_BORDER\_COLOR**](d3d12-static-border-color.md) borderColor = D3D12\_STATIC\_BORDER\_COLOR\_OPAQUE\_WHITE

(opt) FLOAT minLOD = 0.f

(opt) FLOAT maxLOD = D3D12\_FLOAT32\_MAX

(opt) [**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) shaderVisibility = D3D12\_SHADER\_VISIBILITY\_ALL

(opt) UINT registerSpace = 0

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_STATIC\_SAMPLER\_DESC**](d3d12-static-sampler-desc.md)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





