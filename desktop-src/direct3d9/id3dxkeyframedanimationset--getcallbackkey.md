---
Description: Gets information about a specific callback in the animation set.
ms.assetid: a1d3ca96-2852-420a-aa5c-a434970e5523
title: ID3DXKeyframedAnimationSetGetCallbackKey method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXKeyframedAnimationSet::GetCallbackKey method

Gets information about a specific callback in the animation set.

## Syntax


```C++
HRESULT GetCallbackKey(
  [in]  UINT               Animation,
  [out] LPD3DXKEY_CALLBACK pCallbackKeys
);
```



## Parameters

<dl> <dt>

*Animation* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Animation index.

</dd> <dt>

*pCallbackKeys* \[out\]
</dt> <dd>

Type: **[**LPD3DXKEY\_CALLBACK**](d3dxkey-callback.md)**

Pointer to the [**callback function**](d3dxkey-callback.md).

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

 

 




