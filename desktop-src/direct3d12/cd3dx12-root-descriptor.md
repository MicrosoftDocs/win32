---
title: CD3DX12_ROOT_DESCRIPTOR structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_ROOT\_DESCRIPTOR structure.
ms.assetid: DB05BAB7-DD30-4EC7-8D66-C0B2D8DD7BAC
keywords:
- CD3DX12_ROOT_DESCRIPTOR structure
topic_type:
- apiref
api_name:
- CD3DX12_ROOT_DESCRIPTOR
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_ROOT\_DESCRIPTOR structure

A helper structure to enable easy initialization of a [**D3D12\_ROOT\_DESCRIPTOR**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor) structure.

## Syntax


```C++
struct CD3DX12_ROOT_DESCRIPTOR  : public D3D12_ROOT_DESCRIPTOR{
       CD3DX12_ROOT_DESCRIPTOR();
       explicit CD3DX12_ROOT_DESCRIPTOR(const D3D12_ROOT_DESCRIPTOR &o);
       CD3DX12_ROOT_DESCRIPTOR(UINT shaderRegister, UINT registerSpace = 0);
  void inline Init(UINT shaderRegister, UINT registerSpace = 0);
  void static inline Init(D3D12_ROOT_DESCRIPTOR &table, UINT shaderRegister, UINT registerSpace = 0);
};
```



## Members

<dl> <dt>

**CD3DX12\_ROOT\_DESCRIPTOR()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_ROOT\_DESCRIPTOR.

</dd> <dt>

**explicit CD3DX12\_ROOT\_DESCRIPTOR(const D3D12\_ROOT\_DESCRIPTOR &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_DESCRIPTOR, initialized with the contents of another [**D3D12\_ROOT\_DESCRIPTOR**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor) structure.

</dd> <dt>

**CD3DX12\_ROOT\_DESCRIPTOR(UINT shaderRegister, UINT registerSpace = 0)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_DESCRIPTOR, initializing the following parameters:

UINT shaderRegister

(opt) UINT registerSpace = 0

</dd> <dt>

**inline Init(UINT shaderRegister, UINT registerSpace = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT shaderRegister

(opt) UINT registerSpace = 0

</dd> <dt>

**static inline Init(D3D12\_ROOT\_DESCRIPTOR &table, UINT shaderRegister, UINT registerSpace = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_DESCRIPTOR**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor) &table

UINT shaderRegister

(opt) UINT registerSpace = 0

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_ROOT\_DESCRIPTOR**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_descriptor)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





