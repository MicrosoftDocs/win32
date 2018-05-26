---
Description: Sets the track description.
ms.assetid: bc3324b3-ca23-4035-958d-9763a70071f2
title: ID3DXAnimationControllerSetTrackDesc method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Type: **[**UINT**](winprog.windows_data_types)**

Identifier of the track to modify.

</dd> <dt>

*pDesc* \[in\]
</dt> <dd>

Type: **[**LPD3DXTRACK\_DESC**](d3dxtrack-desc.md)**

Description of the track.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




