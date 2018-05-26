---
Description: Remove the animation data from the animation set.
ms.assetid: 9821d21e-fe8f-4742-b4f3-63b2578d29ec
title: ID3DXKeyframedAnimationSetUnregisterAnimation method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXKeyframedAnimationSet::UnregisterAnimation method

Remove the animation data from the animation set.

## Syntax


```C++
HRESULT UnregisterAnimation(
  [in] UINT Index
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

The animation index.

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

 

 




