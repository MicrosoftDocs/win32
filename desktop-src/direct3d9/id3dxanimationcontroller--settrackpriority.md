---
description: Sets the priority blending weight for the specified animation track.
ms.assetid: 8d40b0f6-d79a-42c1-99fb-3f76bd46f30c
title: ID3DXAnimationController::SetTrackPriority method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.SetTrackPriority
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::SetTrackPriority method

Sets the priority blending weight for the specified animation track.

## Syntax


```C++
HRESULT SetTrackPriority(
  [in] UINT              Track,
  [in] D3DXPRIORITY_TYPE Priority
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Track identifier.

</dd> <dt>

*Priority* \[in\]
</dt> <dd>

Type: **[**D3DXPRIORITY\_TYPE**](./d3dxpriority-type.md)**

Track priority. This parameter should be set to one of the constants from [**D3DXPRIORITY\_TYPE**](./d3dxpriority-type.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 
