---
title: CD3DX12_BLEND_DESC structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_BLEND\_DESC structure.
ms.assetid: D37BB62E-904B-4953-9119-21F3B37570C0
keywords:
- CD3DX12_BLEND_DESC structure
topic_type:
- apiref
api_name:
- CD3DX12_BLEND_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_BLEND\_DESC structure

A helper structure to enable easy initialization of a [**D3D12\_BLEND\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_blend_desc) structure.

## Syntax


```C++
struct CD3DX12_BLEND_DESC  : public D3D12_BLEND_DESC{
   CD3DX12_BLEND_DESC();
   explicit CD3DX12_BLEND_DESC(const D3D12_BLEND_DESC& o);
   explicit CD3DX12_BLEND_DESC(CD3DX12_DEFAULT);
   ~CD3DX12_BLEND_DESC();
   operator const D3D12_BLEND_DESC&() const;
};
```



## Members

<dl> <dt>

**CD3DX12\_BLEND\_DESC()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_BLEND\_DESC.

</dd> <dt>

**explicit CD3DX12\_BLEND\_DESC(const D3D12\_BLEND\_DESC& o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_BLEND\_DESC, initialized with the contents of another [**D3D12\_BLEND\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_blend_desc) structure.

</dd> <dt>

**explicit CD3DX12\_BLEND\_DESC(CD3DX12\_DEFAULT)**
</dt> <dd>

Creates a new instance of a CD3DX12\_BLEND\_DESC, initialized with default parameters.



| State                                   | Default Value                    |
|-----------------------------------------|----------------------------------|
| AlphaToCoverageEnable                   | **FALSE**                        |
| IndependentBlendEnable                  | **FALSE**                        |
| RenderTarget\[0\].BlendEnable           | **FALSE**                        |
| RenderTarget\[0\].LogicOpEnable         | **FALSE**                        |
| RenderTarget\[0\].SrcBlend              | D3D12\_BLEND\_ONE                |
| RenderTarget\[0\].DestBlend             | D3D12\_BLEND\_ZERO               |
| RenderTarget\[0\].BlendOp               | D3D12\_BLEND\_OP\_ADD            |
| RenderTarget\[0\].SrcBlendAlpha         | D3D12\_BLEND\_ONE                |
| RenderTarget\[0\].DestBlendAlpha        | D3D12\_BLEND\_ZERO               |
| RenderTarget\[0\].BlendOpAlpha          | D3D12\_BLEND\_OP\_ADD            |
| RenderTarget\[0\].LogicOp               | D3D12\_LOGIC\_OP\_NOOP           |
| RenderTarget\[0\].RenderTargetWriteMask | D3D12\_COLOR\_WRITE\_ENABLE\_ALL |



 

</dd> <dt>

**~CD3DX12\_BLEND\_DESC()**
</dt> <dd>

Destroys an instance of a CD3DX12\_BLEND\_DESC.

</dd> <dt>

**operator const D3D12\_BLEND\_DESC&() const**
</dt> <dd>

Defines the & pass-by-reference operator for the parent structure type.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_BLEND\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_blend_desc)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





