---
description: Removes the scale data at the specified key frame.
ms.assetid: b0bf5665-ccfb-4b87-8e88-9a717ef57955
title: ID3DXKeyframedAnimationSet::UnregisterScaleKey method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXKeyframedAnimationSet.UnregisterScaleKey
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXKeyframedAnimationSet::UnregisterScaleKey method

Removes the scale data at the specified key frame.

## Syntax


```C++
HRESULT UnregisterScaleKey(
  [in] UINT Animation,
  [in] UINT Key
);
```



## Parameters

<dl> <dt>

*Animation* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Animation identifier.

</dd> <dt>

*Key* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Key frame.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

This method is slow and should not be used after an animation has begun to play.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXKeyframedAnimationSet](id3dxkeyframedanimationset.md)
</dt> </dl>

 

 
