---
Description: Gets a description of a specified animation event.
ms.assetid: 7fb3def5-8df2-458d-b68e-5d540fd0a738
title: ID3DXAnimationControllerGetEventDesc method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationController::GetEventDesc method

Gets a description of a specified animation event.

## Syntax


```C++
HRESULT GetEventDesc(
  [in]  D3DXEVENTHANDLE  hEvent,
  [out] LPD3DXEVENT_DESC pDesc
);
```



## Parameters

<dl> <dt>

*hEvent* \[in\]
</dt> <dd>

Type: **[**D3DXEVENTHANDLE**](id3dxanimationcontroller.md)**

Event handle to an animation event to describe.

</dd> <dt>

*pDesc* \[out\]
</dt> <dd>

Type: **[**LPD3DXEVENT\_DESC**](d3dxevent-desc.md)**

Pointer to a [**D3DXEVENT\_DESC**](d3dxevent-desc.md) structure that contains a description of the animation event.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is S\_OK. If the method fails, the following value will be returned: D3DERR\_INVALIDCALL.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationController](id3dxanimationcontroller.md)
</dt> </dl>

 

 




