---
description: Fills an array with scale key data used for key frame animation.
ms.assetid: 0d595510-6d8c-4bc9-b5ca-0d6f73be3439
title: ID3DXKeyframedAnimationSet::GetScaleKeys method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXKeyframedAnimationSet.GetScaleKeys
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXKeyframedAnimationSet::GetScaleKeys method

Fills an array with scale key data used for key frame animation.

## Syntax


```C++
HRESULT GetScaleKeys(
  [in] UINT              Animation,
  [in] LPD3DXKEY_VECTOR3 pScaleKeys
);
```



## Parameters

<dl> <dt>

*Animation* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Animation index.

</dd> <dt>

*pScaleKeys* \[in\]
</dt> <dd>

Type: **[**LPD3DXKEY\_VECTOR3**](d3dxkey-vector3.md)**

Pointer to a user-allocated array of [**D3DXKEY\_VECTOR3**](d3dxkey-vector3.md) vectors that the method is to fill with animation scale data.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXKeyframedAnimationSet](id3dxkeyframedanimationset.md)
</dt> <dt>

[**ID3DXKeyframedAnimationSet::GetNumScaleKeys**](id3dxkeyframedanimationset--getnumscalekeys.md)
</dt> </dl>

 

 
