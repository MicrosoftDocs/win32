---
title: CD3DX12_ROOT_CONSTANTS structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_ROOT\_CONSTANTS structure.
ms.assetid: 2F517DCE-BC0C-4678-9C25-D826036F99A8
keywords:
- CD3DX12_ROOT_CONSTANTS structure
topic_type:
- apiref
api_name:
- CD3DX12_ROOT_CONSTANTS
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_ROOT\_CONSTANTS structure

A helper structure to enable easy initialization of a [**D3D12\_ROOT\_CONSTANTS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_constants) structure.

## Syntax


```C++
struct CD3DX12_ROOT_CONSTANTS  : public D3D12_ROOT_CONSTANTS{
       CD3DX12_ROOT_CONSTANTS();
       explicit CD3DX12_ROOT_CONSTANTS(const D3D12_ROOT_CONSTANTS &o);
       CD3DX12_ROOT_CONSTANTS(UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0);
  void inline Init(UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0);
  void static inline Init(D3D12_ROOT_CONSTANTS &rootConstants, UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0);
};
```



## Members

<dl> <dt>

**CD3DX12\_ROOT\_CONSTANTS()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_ROOT\_CONSTANTS.

</dd> <dt>

**explicit CD3DX12\_ROOT\_CONSTANTS(const D3D12\_ROOT\_CONSTANTS &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_CONSTANTS, initialized with the contents of another [**D3D12\_ROOT\_CONSTANTS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_constants) structure.

</dd> <dt>

**CD3DX12\_ROOT\_CONSTANTS(UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_CONSTANTS, initializing the following parameters:

UINT num32BitValues

UINT shaderRegister

(opt) UINT registerSpace = 0

</dd> <dt>

**inline Init(UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT num32BitValues

UINT shaderRegister

(opt) UINT registerSpace = 0

</dd> <dt>

**static inline Init(D3D12\_ROOT\_CONSTANTS &rootConstants, UINT num32BitValues, UINT shaderRegister, UINT registerSpace = 0)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_CONSTANTS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_constants) &rootConstants

UINT num32BitValues

UINT shaderRegister

(opt) UINT registerSpace = 0

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_ROOT\_CONSTANTS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_constants)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





