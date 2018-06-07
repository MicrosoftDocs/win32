---
Description: Returns an event handle to the event currently running on the specified animation track.
ms.assetid: 2e3d4b85-42f0-463f-9eca-d9b1fa8932f6
title: ID3DXAnimationController::GetCurrentTrackEvent method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**UINT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Track identifier.

</dd> <dt>

*EventType* \[in\]
</dt> <dd>

Type: **[**D3DXEVENT\_TYPE**](https://msdn.microsoft.com/VS|directx_sdk|~\d3dxevent_type.htm)**

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

 

 




