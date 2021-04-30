---
description: Returns an event handle to the next priority blend event scheduled to occur after a specified event.
ms.assetid: 64fa6fca-dc4a-4534-ab8e-b11b3c7ed23c
title: ID3DXAnimationController::GetUpcomingPriorityBlend method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.GetUpcomingPriorityBlend
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::GetUpcomingPriorityBlend method

Returns an event handle to the next priority blend event scheduled to occur after a specified event.

## Syntax


```C++
D3DXEVENTHANDLE GetUpcomingPriorityBlend(
  [in] D3DXEVENTHANDLE hEvent
);
```



## Parameters

<dl> <dt>

*hEvent* \[in\]
</dt> <dd>

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to a specified event after which to search for a following priority blend event. If set to **NULL**, then the method will return the next scheduled priority blend event.

</dd> </dl>

## Return value

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to the next scheduled priority blend event. **NULL** is returned if no new priority blend event is scheduled.

## Remarks

This method can be used iteratively to locate a desired priority blend event by repeatedly passing in **NULL** for hEvent.

> [!Note]  
> Do not iterate further after the method has returned **NULL**.

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




