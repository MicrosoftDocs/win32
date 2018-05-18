---
Description: 'Get rotation information for a specific key frame in the animation set.'
ms.assetid: 'd62b8d5e-328e-4227-b2e8-cb6e5ccc4b3f'
title: 'ID3DXKeyframedAnimationSet::GetRotationKey method'
---

# ID3DXKeyframedAnimationSet::GetRotationKey method

Get rotation information for a specific key frame in the animation set.

## Syntax


```C++
HRESULT GetRotationKey(
  [in] UINT                 Animation,
  [in] UINT                 Key,
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

*Key* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Key frame.

</dd> <dt>

*pRotationKeys* \[in\]
</dt> <dd>

Type: **[**LPD3DXKEY\_QUATERNION**](d3dxkey-quaternion.md)**

Pointer to the rotation data. See [**D3DXKEY\_QUATERNION**](d3dxkey-quaternion.md).

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

 

 




