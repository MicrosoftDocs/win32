---
description: Checks whether a specified event handle is valid and the animation event has not yet completed.
ms.assetid: 242ad1e2-4b04-4ce1-9cdf-f66da9f83f06
title: ID3DXAnimationController::ValidateEvent method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.ValidateEvent
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::ValidateEvent method

Checks whether a specified event handle is valid and the animation event has not yet completed.

## Syntax


```C++
HRESULT ValidateEvent(
  [in] D3DXEVENTHANDLE hEvent
);
```



## Parameters

<dl> <dt>

*hEvent* \[in\]
</dt> <dd>

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to an animation event.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

Returns S\_OK if the event handle is valid and the event has not yet completed.

Returns E\_FAIL if the event handle is invalid and/or the event has completed.

## Remarks

The method will indicate that an event handle is valid even if the event is running but has not yet completed.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




