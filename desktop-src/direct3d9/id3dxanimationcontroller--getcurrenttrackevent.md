---
Description: Returns an event handle to the event currently running on the specified animation track.
ms.assetid: 2e3d4b85-42f0-463f-9eca-d9b1fa8932f6
title: ID3DXAnimationControllerGetCurrentTrackEvent method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::GetCurrentTrackEvent method

Returns an event handle to the event currently running on the specified animation track.

## Syntax


```C++
D3DXEVENTHANDLE GetCurrentTrackEvent(
  [in] UINT           Track,
  [in] D3DXEVENT_TYPE EventType
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Track identifier.

</dd> <dt>

*EventType* \[in\]
</dt> <dd>

Type: **[**D3DXEVENT\_TYPE**](direct3d9.d3dxevent_type)**

Type of event to query.

</dd> </dl>

## Return value

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to the event currently running on the specified track. **NULL** is returned if no event is running on the specified track.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




