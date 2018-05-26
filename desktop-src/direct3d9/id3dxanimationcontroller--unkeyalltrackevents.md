---
Description: Removes all events from a specified animation track.
ms.assetid: 25c4d04a-0d75-4113-ad90-db84aa937098
title: ID3DXAnimationControllerUnkeyAllTrackEvents method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::UnkeyAllTrackEvents method

Removes all events from a specified animation track.

## Syntax


```C++
HRESULT UnkeyAllTrackEvents(
  [in] UINT Track
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Identifier of the track on which all events should be removed.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Remarks

This method prevents the execution of all events previously scheduled on the track, and discards all data associated with those events.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




