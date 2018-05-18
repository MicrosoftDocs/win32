---
title: CD3DX12\_ROOT\_SIGNATURE\_DESC structure
description: A helper structure to enable easy initialization of a D3D12\_ROOT\_SIGNATURE\_DESC structure.
ms.assetid: 'A3B820C1-51E8-4E35-A67F-2C4BE82A6B7F'
keywords: ["CD3DX12_ROOT_SIGNATURE_DESC structure"]
topic_type:
- apiref
api_name:
- CD3DX12_ROOT_SIGNATURE_DESC
api_location:
- d3dx12.h
api_type:
- HeaderDef
---

# CD3DX12\_ROOT\_SIGNATURE\_DESC structure

A helper structure to enable easy initialization of a [**D3D12\_ROOT\_SIGNATURE\_DESC**](d3d12-root-signature-desc.md) structure.

## Syntax


```C++
struct CD3DX12_ROOT_SIGNATURE_DESC  : public D3D12_ROOT_SIGNATURE_DESC{
       CD3DX12_ROOT_SIGNATURE_DESC();
       explicit CD3DX12_ROOT_SIGNATURE_DESC(const D3D12_ROOT_SIGNATURE_DESC &amp;o);
       CD3DX12_ROOT_SIGNATURE_DESC(UINT numParameters, const D3D12_ROOT_PARAMETER* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
       CD3DX12_ROOT_SIGNATURE_DESC(CD3DX12_DEFAULT);
  void inline Init(UINT numParameters, const D3D12_ROOT_PARAMETER* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
  void static inline Init(D3D12_ROOT_SIGNATURE_DESC &amp;desc, UINT numParameters, const D3D12_ROOT_PARAMETER* _pParameters, UINT numStaticSamplers = 0, const D3D12_STATIC_SAMPLER_DESC* _pStaticSamplers = NULL, D3D12_ROOT_SIGNATURE_FLAGS flags = D3D12_ROOT_SIGNATURE_FLAG_NONE);
};
```



## Members

<dl> <dt>

**CD3DX12\_ROOT\_SIGNATURE\_DESC()**
</dt> <dd>

Creates a new, uninitialized, instance of a CD3DX12\_ROOT\_SIGNATURE\_DESC.

</dd> <dt>

**explicit CD3DX12\_ROOT\_SIGNATURE\_DESC(const D3D12\_ROOT\_SIGNATURE\_DESC &o)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_SIGNATURE\_DESC, initialized with the contents of another [**D3D12\_ROOT\_SIGNATURE\_DESC**](d3d12-root-signature-desc.md) structure.

</dd> <dt>

**CD3DX12\_ROOT\_SIGNATURE\_DESC(UINT numParameters, const D3D12\_ROOT\_PARAMETER\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_SIGNATURE\_DESC, initializing the following parameters:

UINT numParameters

[**D3D12\_ROOT\_PARAMETER**](d3d12-root-parameter.md)\* \_pParameters

(opt) UINT numStaticSamplers = 0

(opt) [**D3D12\_STATIC\_SAMPLER\_DESC**](d3d12-static-sampler-desc.md)\* \_pStaticSamplers = NULL

(opt) [**D3D12\_ROOT\_SIGNATURE\_FLAGS**](d3d12-root-signature-flags.md) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> <dt>

**CD3DX12\_ROOT\_SIGNATURE\_DESC(CD3DX12\_DEFAULT)**
</dt> <dd>

Creates a new instance of a CD3DX12\_ROOT\_SIGNATURE\_DESC, initialized with default parameters.

``` syntax
CD3DX12_ROOT_SIGNATURE_DESC(0,NULL,0,NULL,D3D12_ROOT_SIGNATURE_FLAG_NONE)
```

</dd> <dt>

**inline Init(UINT numParameters, const D3D12\_ROOT\_PARAMETER\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

UINT numParameters

[**D3D12\_ROOT\_PARAMETER**](d3d12-root-parameter.md)\* \_pParameters

(opt) UINT numStaticSamplers = 0

(opt) [**D3D12\_STATIC\_SAMPLER\_DESC**](d3d12-static-sampler-desc.md)\* \_pStaticSamplers = NULL

(opt) [**D3D12\_ROOT\_SIGNATURE\_FLAGS**](d3d12-root-signature-flags.md) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> <dt>

**static inline Init(D3D12\_ROOT\_SIGNATURE\_DESC &desc, UINT numParameters, const D3D12\_ROOT\_PARAMETER\* \_pParameters, UINT numStaticSamplers = 0, const D3D12\_STATIC\_SAMPLER\_DESC\* \_pStaticSamplers = NULL, D3D12\_ROOT\_SIGNATURE\_FLAGS flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE)**
</dt> <dd>

Specifies a function that initializes the following parameters:

[**D3D12\_ROOT\_SIGNATURE\_DESC**](d3d12-root-signature-desc.md) &desc

UINT numParameters

[**D3D12\_ROOT\_PARAMETER**](d3d12-root-parameter.md)\* \_pParameters

(opt) UINT numStaticSamplers = 0

(opt) [**D3D12\_STATIC\_SAMPLER\_DESC**](d3d12-static-sampler-desc.md)\* \_pStaticSamplers = NULL

(opt) [**D3D12\_ROOT\_SIGNATURE\_FLAGS**](d3d12-root-signature-flags.md) flags = D3D12\_ROOT\_SIGNATURE\_FLAG\_NONE

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx12.h</dt> </dl> |



## See also

<dl> <dt>

[**D3D12\_ROOT\_SIGNATURE\_DESC**](d3d12-root-signature-desc.md)
</dt> <dt>

[Helper Structures for D3D12](helper-structures-for-d3d12.md)
</dt> </dl>

 

 





