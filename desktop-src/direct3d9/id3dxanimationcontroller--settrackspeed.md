---
Description: Sets the track speed. The track speed is similar to a multiplier that is used to speed up or slow down the playback of the track.
ms.assetid: b3946b61-0676-4690-9844-639fabd8fd7c
title: ID3DXAnimationControllerSetTrackSpeed method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::SetTrackSpeed method

Sets the track speed. The track speed is similar to a multiplier that is used to speed up or slow down the playback of the track.

## Syntax


```C++
HRESULT SetTrackSpeed(
  [in] UINT  Track,
  [in] FLOAT Speed
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Identifier of the track to set the speed on.

</dd> <dt>

*Speed* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

New speed.

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

 

 




