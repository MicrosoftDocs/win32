---
Description: 'Removes the scale data at the specified key frame.'
ms.assetid: 'b0bf5665-ccfb-4b87-8e88-9a717ef57955'
title: 'ID3DXKeyframedAnimationSet::UnregisterScaleKey method'
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

Type: **[**UINT**](winprog.windows_data_types)**

Animation identifier.

</dd> <dt>

*Key* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Key frame.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

This method is slow and should not be used after an animation has begun to play.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXKeyframedAnimationSet](id3dxkeyframedanimationset.md)
</dt> </dl>

 

 




