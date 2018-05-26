---
Description: Returns an event handle to the next event scheduled to occur after a specified event on an animation track.
ms.assetid: 616b2de1-6107-4d18-ad2e-de2ef4560aee
title: ID3DXAnimationControllerGetUpcomingTrackEvent method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::GetUpcomingTrackEvent method

Returns an event handle to the next event scheduled to occur after a specified event on an animation track.

## Syntax


```C++
D3DXEVENTHANDLE GetUpcomingTrackEvent(
  [in] UINT            Track,
  [in] D3DXEVENTHANDLE hEvent
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Track identifier.

</dd> <dt>

*hEvent* \[in\]
</dt> <dd>

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to a specified event after which to search for a following event. If set to **NULL**, then the method will return the next scheduled event.

</dd> </dl>

## Return value

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to the next event scheduled to run on the specified track. **NULL** is returned if no new event is scheduled.

## Remarks

This method can be used iteratively to locate a desired event by repeatedly passing in **NULL** for hEvent.

> [!Note]  
> Do not iterate further after the method has returned **NULL**.

 

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




