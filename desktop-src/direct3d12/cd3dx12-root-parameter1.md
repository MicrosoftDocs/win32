---
title: CD3DX12\_ROOT\_PARAMETER1 structure
description: A helper structure to enable easy initialization of a D3D12\_ROOT\_PARAMETER1 structure.
ms.assetid: 'CDE0C02E-0112-4FD9-A4A2-36E8C326715C'
keywords: ["CD3DX12_ROOT_PARAMETER1 structure"]
topic_type:
- apiref
api_name:
- CD3DX12_ROOT_PARAMETER1
api_location:
- d3dx12.h
api_type:
- HeaderDef
---

# CD3DX12\_ROOT\_PARAMETER1 structure

A helper structure to enable easy initialization of a [**D3D12\_ROOT\_PARAMETER1**](d3d12-root-parameter1.md) structure.

## Syntax


```C++
struct CD3DX12_ROOT_PARAMETER1  : public D3D12_ROOT_PARAMETER1{
       CD3DX12_ROOT_PARAMETER1();
       explicit CD3DX12_ROOT_PARAMETER1(const D3D12_ROOT_PARAMETER1 &amp;o);
  void static inline InitAsDescriptorTable(D3D12_ROOT_PARAMETER1 &amp;rootParam, UINT numDescriptorRanges, const D3D12_DESCRIPTOR_RANGE1* pDescriptorRanges, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void static inline InitAsConstants(D3D12_ROOT_PARAMETER1 &amp;rootParam, UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void static inline InitAsConstantBufferView(D3D12_ROOT_PARAMETER1 &amp;rootParam, UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void static inline InitAsShaderResourceView(D3D12_ROOT_PARAMETER1 &amp;rootParam, UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void static inline InitAsUnorderedAccessView(D3D12_ROOT_PARAMETER1 &amp;rootParam, UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void inline InitAsDescriptorTable(UINT numDescriptorRanges, const D3D12_DESCRIPTOR_RANGE1* pDescriptorRanges, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void inline InitAsConstants(UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void inline InitAsConstantBufferView(UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void inline InitAsShaderResourceView(UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
  void inline InitAsUnorderedAccessView(UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE, D3D12_SHADER_VISIBILITY visibility = D3D12_SHADER_VISIBILITY_ALL);
};
```



## Members

<dl> <dt>

**CD3DX12\_ROOT\_PARAMETER1()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_ROOT\_PARAMETER1.

</dd> <dt>

**explicit CD3DX12\_ROOT\_PARAMETER1(const D3D12\_ROOT\_PARAMETER1 &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_PARAMETER1, initialized with the contents of another [**D3D12\_ROOT\_PARAMETER1**](d3d12-root-parameter1.md) structure.

</dd> <dt>

**static inline InitAsDescriptorTable(D3D12\_ROOT\_PARAMETER1 &rootParam, UINT numDescriptorRanges, const D3D12\_DESCRIPTOR\_RANGE1\* pDescriptorRanges, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_PARAMETER1**](d3d12-root-parameter1.md) &rootParam

UINT numDescriptorRanges

const [**D3D12\_DESCRIPTOR\_RANGE1**](d3d12-descriptor-range1.md)\* pDescriptorRanges

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**static inline InitAsConstants(D3D12\_ROOT\_PARAMETER1 &rootParam, UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_PARAMETER1**](d3d12-root-parameter1.md) &rootParam

UINT num32BitValues

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**static inline InitAsConstantBufferView(D3D12\_ROOT\_PARAMETER1 &rootParam, UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_PARAMETER1**](d3d12-root-parameter1.md) &rootParam

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**static inline InitAsShaderResourceView(D3D12\_ROOT\_PARAMETER1 &rootParam, UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_PARAMETER1**](d3d12-root-parameter1.md) &rootParam

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**static inline InitAsUnorderedAccessView(D3D12\_ROOT\_PARAMETER1 &rootParam, UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_PARAMETER1**](d3d12-root-parameter1.md) &rootParam

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**inline InitAsDescriptorTable(UINT numDescriptorRanges, const D3D12\_DESCRIPTOR\_RANGE1\* pDescriptorRanges, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT numDescriptorRanges

const [**D3D12\_DESCRIPTOR\_RANGE1**](d3d12-descriptor-range1.md)\* pDescriptorRanges

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**inline InitAsConstants(UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT num32BitValues

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**inline InitAsConstantBufferView(UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**inline InitAsShaderResourceView(UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> <dt>

**inline InitAsUnorderedAccessView(UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE, D3D12\_SHADER\_VISIBILITY visibility = D3D12\_SHADER\_VISIBILITY\_ALL)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

[**D3D12\_SHADER\_VISIBILITY**](d3d12-shader-visibility.md) visibility = D3D12\_SHADER\_VISIBILITY\_ALL

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_ROOT\_PARAMETER1**](d3d12-root-parameter1.md)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





