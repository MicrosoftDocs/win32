---
description: Gets an animation set, given its name.
ms.assetid: 4c3f3002-45f6-49b2-8a42-18d5824fb36f
title: ID3DXAnimationController::GetAnimationSetByName method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.GetAnimationSetByName
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::GetAnimationSetByName method

Gets an animation set, given its name.

## Syntax


```C++
HRESULT GetAnimationSetByName(
  [in]  LPCSTR             pName,
  [out] LPD3DXANIMATIONSET *ppAnimSet
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](../winprog/windows-data-types.md)**

String containing the name of the animation set.

</dd> <dt>

*ppAnimSet* \[out\]
</dt> <dd>

Type: **[**LPD3DXANIMATIONSET**](id3dxanimationset.md)\***

Pointer to the [**ID3DXAnimationSet**](id3dxanimationset.md) animation set.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

The animation controller contains an array of animation sets. This method returns an animation set that has the given name.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 
