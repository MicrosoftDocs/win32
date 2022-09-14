---
description: Removes a specified event from an animation track, preventing the execution of the event.
ms.assetid: 658ffe91-44ba-4bde-b78c-c545dff27ab1
title: ID3DXAnimationController::UnkeyEvent method (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController.UnkeyEvent
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController::UnkeyEvent method

Removes a specified event from an animation track, preventing the execution of the event.

## Syntax


```C++
HRESULT UnkeyEvent(
  [in] D3DXEVENTHANDLE hEvent
);
```



## Parameters

<dl> <dt>

*hEvent* \[in\]
</dt> <dd>

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to the event to be removed from the animation track.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




