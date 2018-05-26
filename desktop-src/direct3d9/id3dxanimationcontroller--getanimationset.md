---
Description: Gets an animation set.
ms.assetid: 61785f60-82c1-4ddc-b4cd-2e7f665cfe8c
title: ID3DXAnimationControllerGetAnimationSet method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::GetAnimationSet method

Gets an animation set.

## Syntax


```C++
HRESULT GetAnimationSet(
  [in]  UINT               Index,
  [out] LPD3DXANIMATIONSET *ppAnimSet
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Index of the animation set.

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

The animation controller contains an array of animation sets. This method returns one of them at the given index.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




