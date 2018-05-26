---
Description: The application implements this method. This method is called when a callback occurs for an animation set in one of the tracks during a call to ID3DXAnimationControllerAdvanceTime.
ms.assetid: eb606fb0-d6b9-456d-97e1-b595306e6463
title: ID3DXAnimationCallbackHandlerHandleCallback method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DXAnimationCallbackHandler::HandleCallback method

The application implements this method. This method is called when a callback occurs for an animation set in one of the tracks during a call to [**ID3DXAnimationController::AdvanceTime**](id3dxanimationcontroller--advancetime.md).

## Syntax


```C++
HRESULT HandleCallback(
  [in] UINT   Track,
  [in] LPVOID pCallbackData
);
```



## Parameters

<dl> <dt>

*Track* \[in\]
</dt> <dd>

Type: **[**UINT**](winprog.windows_data_types)**

Identifier of the track on which the callback occurs.

</dd> <dt>

*pCallbackData* \[in\]
</dt> <dd>

Type: **[**LPVOID**](winprog.windows_data_types)**

Pointer to user-owned callback data.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return values of this method are implemented by an application programmer. In general, if no error occurs, program the method to return D3D\_OK. Otherwise, program the method to return an appropriate error message from [D3DERR](d3derr.md) or [**D3DXERR**](direct3d9.d3dxerr).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXAnimationCallbackHandler](id3dxanimationcallbackhandler.md)
</dt> </dl>

 

 




