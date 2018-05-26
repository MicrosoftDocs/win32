---
Description: Fills an array with rotational key data used for key frame animation.
ms.assetid: 9ae8bc28-d231-4d50-98f0-762b2d2c04e8
title: ID3DXKeyframedAnimationSetGetRotationKeys method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXKeyframedAnimationSet::GetRotationKeys method

Fills an array with rotational key data used for key frame animation.

## Syntax


```C++
HRESULT GetRotationKeys(
  [in] UINT                 Animation,
  [in] LPD3DXKEY_QUATERNION pRotationKeys
);
```



## Parameters

<dl> <dt>

*Animation* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Animation index.

</dd> <dt>

*pRotationKeys* \[in\]
</dt> <dd>

Type: **[**LPD3DXKEY\_QUATERNION**](d3dxkey-quaternion.md)**

Pointer to a user-allocated array of [**D3DXKEY\_QUATERNION**](d3dxkey-quaternion.md) quaternions that the method is to fill with animation rotation data.

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
</dt> <dt>

[**ID3DXKeyframedAnimationSet::GetNumRotationKeys**](id3dxkeyframedanimationset--getnumrotationkeys.md)
</dt> </dl>

 

 




