---
title: CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC structure (D3dx12.h)
description: A helper structure to enable easy initialization of a D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC structure.
ms.assetid: 4505C1CE-CAA5-4092-B990-75740A2B194C
keywords:
- CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC structure
topic_type:
- apiref
api_name:
- CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC structure

A helper structure to enable easy initialization of a [**D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) structure.

## Syntax


```C++
struct CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC  : public D3D12_VERSIONED_ROOT_SIGNATURE_DESC{
       CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC();
       explicit CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC(const D3D12_VERSIONED_ROOT_SIGNATURE_DESC &o);
       explicit CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC(const D3D12_ROOT_SIGNATURE_DESC &o);
       explicit CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC(const D3D12_ROOT_SIGNATURE_DESC1 &o);
       CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC(UINT numParameters, const D3D12_ROOT_PARAMETER* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
       CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC(UINT numParameters, const D3D12_ROOT_PARAMETER1* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
       CD3DX12_VERSIONED_ROOT_SIGNATURE_DESC(CD3DX12_DEFAULT);
  void inline Init_1_0(UINT numParameters, const D3D12_ROOT_PARAMETER* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
  void static inline Init_1_0(D3D12_VERSIONED_ROOT_SIGNATURE_DESC &desc, UINT numParameters, const D3D12_ROOT_PARAMETER* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
  void inline Init_1_1(UINT numParameters, const D3D12_ROOT_PARAMETER1* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
  void static inline Init_1_1(D3D12_VERSIONED_ROOT_SIGNATURE_DESC &desc, UINT numParameters, const D3D12_ROOT_PARAMETER1* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
};
```



## Members

<dl> <dt>

**CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC.

</dd> <dt>

**explicit CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC(const D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC, initialized with the contents of a [**D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) structure.

</dd> <dt>

**explicit CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC(const D3D12\_ROOT\_SIGNATURE\_DESC &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC, initialized with the contents of a [**D3D12\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_signature_desc) structure.

</dd> <dt>

**explicit CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC(const D3D12\_ROOT\_SIGNATURE\_DESC1 &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC, initialized with the contents of a [**D3D12\_ROOT\_SIGNATURE\_DESC1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_signature_desc1) structure.

</dd> <dt>

**CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC(UINT numParameters, const D3D12\_ROOT\_PARAMETER\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC, initializing the following parameters:

UINT numParameters

const [**D3D12\_ROOT\_PARAMETER**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_parameter)\* \_pParameters

UINT numStaticSamplers = 0

const [**D3D12\_STATIC\_SAMPLER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_static_sampler_desc)\* \_pStaticSamplers = NULL

[**D3D12\_ROOT\_SIGNATURE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_signature_flags) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> <dt>

**CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC(UINT numParameters, const D3D12\_ROOT\_PARAMETER1\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC, initializing the following parameters:

UINT numParameters

const [**D3D12\_ROOT\_PARAMETER1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_parameter1)\* \_pParameters

UINT numStaticSamplers = 0

const [**D3D12\_STATIC\_SAMPLER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_static_sampler_desc)\* \_pStaticSamplers = NULL

[**D3D12\_ROOT\_SIGNATURE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_signature_flags) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> <dt>

**CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC(CD3DX12\_DEFAULT)**
</dt> <dd>

Creates a new instance of a CD3DX12\_VERSIONED\_ROOT\_SIGNATURE\_DESC, initialized with the default parameters:

UINT numParameters = 0

const [**D3D12\_ROOT\_PARAMETER1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_parameter1)\* \_pParameters = NULL

UINT numStaticSamplers = 0

const [**D3D12\_STATIC\_SAMPLER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_static_sampler_desc)\* \_pStaticSamplers = NULL

[**D3D12\_ROOT\_SIGNATURE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_signature_flags) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> <dt>

**inline Init\_1\_0(UINT numParameters, const D3D12\_ROOT\_PARAMETER\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT numParameters

const [**D3D12\_ROOT\_PARAMETER**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_parameter)\* \_pParameters

UINT numStaticSamplers = 0

const [**D3D12\_STATIC\_SAMPLER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_static_sampler_desc)\* \_pStaticSamplers = NULL

[**D3D12\_ROOT\_SIGNATURE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_signature_flags) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> <dt>

**static inline Init\_1\_0(D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC &desc, UINT numParameters, const D3D12\_ROOT\_PARAMETER\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) &desc

UINT numParameters

const [**D3D12\_ROOT\_PARAMETER**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_parameter)\* \_pParameters

UINT numStaticSamplers = 0

const [**D3D12\_STATIC\_SAMPLER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_static_sampler_desc)\* \_pStaticSamplers = NULL

[**D3D12\_ROOT\_SIGNATURE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_signature_flags) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> <dt>

**inline Init\_1\_1(UINT numParameters, const D3D12\_ROOT\_PARAMETER1\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT numParameters

const [**D3D12\_ROOT\_PARAMETER1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_parameter1)\* \_pParameters

UINT numStaticSamplers = 0

const [**D3D12\_STATIC\_SAMPLER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_static_sampler_desc)\* \_pStaticSamplers = NULL

[**D3D12\_ROOT\_SIGNATURE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_signature_flags) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> <dt>

**static inline Init\_1\_1(D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC &desc, UINT numParameters, const D3D12\_ROOT\_PARAMETER1\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc) &desc

UINT numParameters

const [**D3D12\_ROOT\_PARAMETER1**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_root_parameter1)\* \_pParameters

UINT numStaticSamplers = 0

const [**D3D12\_STATIC\_SAMPLER\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_static_sampler_desc)\* \_pStaticSamplers = NULL

[**D3D12\_ROOT\_SIGNATURE\_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_root_signature_flags) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_VERSIONED\_ROOT\_SIGNATURE\_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_versioned_root_signature_desc)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





