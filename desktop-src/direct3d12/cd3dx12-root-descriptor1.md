---
title: CD3DX12\_ROOT\_DESCRIPTOR1 structure
description: A helper structure to enable easy initialization of a D3D12\_ROOT\_DESCRIPTOR1 structure.
ms.assetid: '664822BF-5C27-4541-953F-219894547A6C'
keywords: ["CD3DX12_ROOT_DESCRIPTOR1 structure"]
topic_type:
- apiref
api_name:
- CD3DX12_ROOT_DESCRIPTOR1
api_location:
- d3dx12.h
api_type:
- HeaderDef
---

# CD3DX12\_ROOT\_DESCRIPTOR1 structure

A helper structure to enable easy initialization of a [**D3D12\_ROOT\_DESCRIPTOR1**](d3d12-root-descriptor1.md) structure.

## Syntax


```C++
struct CD3DX12_ROOT_DESCRIPTOR1  : public D3D12_ROOT_DESCRIPTOR1{
       CD3DX12_ROOT_DESCRIPTOR1();
       explicit CD3DX12_ROOT_DESCRIPTOR1(const D3D12_ROOT_DESCRIPTOR1 &amp;o);
       CD3DX12_ROOT_DESCRIPTOR1(UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE);
  void inline Init(UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE);
  void static inline Init(D3D12_ROOT_DESCRIPTOR1 &amp;table, UINT shaderRegister, UINT registerSpace = 0, D3D12_ROOT_DESCRIPTOR_FLAGS flags = D3D12_ROOT_DESCRIPTOR_FLAG_NONE);
};
```



## Members

<dl> <dt>

**CD3DX12\_ROOT\_DESCRIPTOR1()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_ROOT\_DESCRIPTOR1.

</dd> <dt>

**explicit CD3DX12\_ROOT\_DESCRIPTOR1(const D3D12\_ROOT\_DESCRIPTOR1 &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_DESCRIPTOR1, initialized with the contents of another [**D3D12\_ROOT\_DESCRIPTOR1**](d3d12-root-descriptor1.md) structure.

</dd> <dt>

**CD3DX12\_ROOT\_DESCRIPTOR1(UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_DESCRIPTOR1, initializing the following parameters:

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

</dd> <dt>

**inline Init(UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

</dd> <dt>

**static inline Init(D3D12\_ROOT\_DESCRIPTOR1 &table, UINT shaderRegister, UINT registerSpace = 0, D3D12\_ROOT\_DESCRIPTOR\_FLAGS flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_DESCRIPTOR1**](d3d12-root-descriptor1.md) &table

UINT shaderRegister

UINT registerSpace = 0

[**D3D12\_ROOT\_DESCRIPTOR\_FLAGS**](d3d12-root-descriptor-flags.md) flags = D3D12\_ROOT\_DESCRIPTOR\_FLAG\_NONE

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_ROOT\_DESCRIPTOR1**](d3d12-root-descriptor1.md)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





