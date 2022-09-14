---
title: CD3DX12_DEFAULT structure (D3dx12.h)
description: Passes D3D12\_DEFAULT into a constructor for each helper structure. This structure is simply used as a mechanism to set default parameters on the other helper structures.
ms.assetid: AD41FD7B-9172-400E-9292-374FFAEDE145
keywords:
- CD3DX12_DEFAULT structure
topic_type:
- apiref
api_name:
- CD3DX12_DEFAULT
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_DEFAULT structure

Passes D3D12\_DEFAULT into a constructor for each helper structure. This structure is simply used as a mechanism to set default parameters on the other helper structures.

## Remarks

This struct is declared as follows:

``` syntax
struct CD3DX12_DEFAULT {};
extern const DECLSPEC_SELECTANY CD3DX12_DEFAULT D3D12_DEFAULT;
```

Passes D3D12\_DEFAULT into a constructor for each helper struct. For example, the following constructor is declared in d3dx12.h:

CD3DX12\_CPU\_DESCRIPTOR\_HANDLE(CD3DX12\_DEFAULT) { ptr = 0; }

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





