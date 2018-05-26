---
Description: Gets an animation set, given its name.
ms.assetid: 4c3f3002-45f6-49b2-8a42-18d5824fb36f
title: ID3DXAnimationControllerGetAnimationSetByName method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**LPCSTR**](winprog.windows_data_types)**

String containing the name of the animation set.

</dd> <dt>

*ppAnimSet* \[out\]
</dt> <dd>

Type: **[**LPD3DXANIMATIONSET**](id3dxanimationset.md)\***

Pointer to the [**ID3DXAnimationSet**](id3dxanimationset.md) animation set.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

The animation controller contains an array of animation sets. This method returns an animation set that has the given name.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




