---
Description: Set translation information for a specific key frame in the animation set.
ms.assetid: 4a926c0f-6d57-48d4-bb3b-60766fc78e40
title: ID3DXKeyframedAnimationSetSetTranslationKey method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXKeyframedAnimationSet::SetTranslationKey method

Set translation information for a specific key frame in the animation set.

## Syntax


```C++
HRESULT SetTranslationKey(
  [in] UINT              Animation,
  [in] UINT              Key,
  [in] LPD3DXKEY_VECTOR3 pTranslationKey
);
```



## Parameters

<dl> <dt>

*Animation* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Animation index.

</dd> <dt>

*Key* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Key Frame.

</dd> <dt>

*pTranslationKey* \[in\]
</dt> <dd>

Type: **[**LPD3DXKEY\_VECTOR3**](d3dxkey-vector3.md)**

Pointer to the translation data. See [**D3DXKEY\_VECTOR3**](d3dxkey-vector3.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXKeyframedAnimationSet](id3dxkeyframedanimationset.md)
</dt> </dl>

 

 




