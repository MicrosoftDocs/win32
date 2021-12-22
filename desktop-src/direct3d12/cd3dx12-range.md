---
title: CD3DX12_RANGE structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_RANGE structure.
ms.assetid: 5D5192BF-D14C-487B-A214-F8428E82AF0E
keywords:
- CD3DX12_RANGE structure
topic_type:
- apiref
api_name:
- CD3DX12_RANGE
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_RANGE structure

A helper structure to enable easy initialization of a [**D3D12\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_range) structure.

## Syntax


```C++
struct CD3DX12_RANGE  : public D3D12_RANGE{
   CD3DX12_RANGE();
   explicit CD3DX12_RANGE(const D3D12_RANGE &o);
   CD3DX12_RANGE(SIZE_T begin, SIZE_T end);
   operator const D3D12_RANGE&() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_RANGE()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_RANGE.

</dd> <dt>

**explicit CD3DX12\_RANGE(const D3D12\_RANGE &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_RANGE, initialized with the contents of another [**D3D12\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_range) structure.

</dd> <dt>

**CD3DX12\_RANGE(SIZE\_T begin, SIZE\_T end)**
</dt> <dd>

Creates a new instance of a CD3DX12\_RANGE, initializing the following parameters:

SIZE\_T begin

SIZE\_T end

</dd> <dt>

**operator const D3D12\_RANGE&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_RANGE**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_range)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





