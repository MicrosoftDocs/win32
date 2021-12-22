---
title: CD3DX12_BOX structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_BOX structure.
ms.assetid: 7E1A352C-D664-4538-BA78-91493980559D
keywords:
- CD3DX12_BOX structure
topic_type:
- apiref
api_name:
- CD3DX12_BOX
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_BOX structure

A helper structure to enable easy initialization of a [**D3D12\_BOX**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_box) structure.

## Syntax


```C++
struct CD3DX12_BOX  : public D3D12_BOX{
   CD3DX12_BOX();
   explicit CD3DX12_BOX(const D3D12_BOX& o);
   explicit CD3DX12_BOX(LONG Left, LONG Right);
   explicit CD3DX12_BOX(LONG Left, LONG Top, LONG Right, LONG Bottom);
   explicit CD3DX12_BOX(LONG Left, LONG Top, LONG Front, LONG Right, LONG Bottom, LONG Back);
   ~CD3DX12_BOX();
   operator const D3D12_BOX&() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_BOX()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_BOX.

</dd> <dt>

**explicit CD3DX12\_BOX(const D3D12\_BOX& o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_BOX, initialized with the contents of another [**D3D12\_BOX**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_box) structure.

</dd> <dt>

**explicit CD3DX12\_BOX(LONG Left, LONG Right)**
</dt> <dd>

Creates a new instance of a CD3DX12\_BOX, initializing the following parameters:

LONG Left

LONG Right

</dd> <dt>

**explicit CD3DX12\_BOX(LONG Left, LONG Top, LONG Right, LONG Bottom)**
</dt> <dd>

Creates a new instance of a CD3DX12\_BOX, initializing the following parameters:

LONG Left

LONG Top

LONG Right

LONG Bottom

</dd> <dt>

**explicit CD3DX12\_BOX(LONG Left, LONG Top, LONG Front, LONG Right, LONG Bottom, LONG Back)**
</dt> <dd>

Creates a new instance of a CD3DX12\_BOX, initializing the following parameters:

LONG Left

LONG Top

LONG Front

LONG Right

LONG Bottom

LONG Back

</dd> <dt>

**~CD3DX12\_BOX()**
</dt> <dd>

Destroys an instance of a CD3DX12\_BOX.

</dd> <dt>

**operator const D3D12\_BOX&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_BOX**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_box)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





