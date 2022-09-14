---
description: Sets the track description.
ms.assetid: bc3324b3-ca23-4035-958d-9763a70071f2
title: ID3DXAnimationController::SetTrackDesc method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.SetTrackDesc
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::SetTrackDesc method

Sets the track description.

## Syntax


```C++
HRESULT SetTrackDesc(
  [in] UINT             Track,
  [in] LPD3DXTRACK_DESC pDesc
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Identifier of the track to modify.

</dd> <dt>

*pDesc* \[in\]
</dt> <dd>

Type: **[**LPD3DXTRACK\_DESC**](d3dxtrack-desc.md)**

Description of the track.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 
