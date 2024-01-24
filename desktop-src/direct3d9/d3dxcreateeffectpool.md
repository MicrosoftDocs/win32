---
description: Create an effect pool. A pool is used to share parameters between effects.
ms.assetid: 5b202f85-b32b-4041-8873-0de535c2f59f
title: D3DXCreateEffectPool function (D3DX9Effect.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXCreateEffectPool
api_type: 
- LibDef
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# D3DXCreateEffectPool function

Create an effect pool. A pool is used to share parameters between effects.

## Syntax


```C++
HRESULT D3DXCreateEffectPool(
  _Out_ LPD3DXEFFECTPOOL *ppPool
);
```



## Parameters

<dl> <dt>

*ppPool* \[out\]
</dt> <dd>

Type: **[**LPD3DXEFFECTPOOL**](id3dxeffectpool.md)\***

Returns a pointer to the created pool.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK.

If the arguments are invalid, the method will return D3DERR\_INVALIDCALL.

If the method fails, the return value will be E\_FAIL.

## Remarks

For effects within a pool, shared parameters with the same name share values.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Effect.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>     |



## See also

<dl> <dt>

[Effect Functions](dx9-graphics-reference-effects-functions.md)
</dt> </dl>

 

 




