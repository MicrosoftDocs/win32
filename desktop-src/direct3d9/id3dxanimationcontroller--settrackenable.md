---
Description: Enables or disables a track in the animation controller.
ms.assetid: 8d06287b-e076-4553-962c-5c423e355101
title: ID3DXAnimationControllerSetTrackEnable method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::SetTrackEnable method

Enables or disables a track in the animation controller.

## Syntax


```C++
HRESULT SetTrackEnable(
  [in] UINT Track,
  [in] BOOL Enable
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Identifier of the track to be mixed.

</dd> <dt>

*Enable* \[in\]
</dt> <dd>

Type: **[**BOOL**](winprog.windows_data_types)**

Enable value. Set to **TRUE** to enable this track in the controller, or to **FALSE** to prevent it from being mixed.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following values: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

To mix a track with other tracks, the Enable flag must be set to **TRUE**. Conversely, setting the flag to **FALSE** will prevent the track from being mixed with other tracks.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




