---
description: Returns an event handle to a priority blend event that is currently running.
ms.assetid: a7184459-7644-4e65-a8ea-13019889e02b
title: ID3DXAnimationController::GetCurrentPriorityBlend method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.GetCurrentPriorityBlend
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::GetCurrentPriorityBlend method

Returns an event handle to a priority blend event that is currently running.

## Syntax


```C++
D3DXEVENTHANDLE GetCurrentPriorityBlend();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to the currently running priority blend event. **NULL** is returned if no priority blend event is currently running.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




