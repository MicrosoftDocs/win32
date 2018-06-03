---
title: Direct3D 12 Return Codes
description: The following are return codes from API functions.
ms.assetid: 5F6CC962-7DB7-489F-82A4-9388313014D3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 12 Return Codes

The following are return codes from API functions. For more return codes, see [DXGI\_ERROR](https://msdn.microsoft.com/library/windows/desktop/bb509553).



| HRESULT                                                                  | Description                                                                                                           |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| D3D12\_ERROR\_FILE\_NOT\_FOUND                                           | The file was not found.                                                                                               |
| D3D12\_ERROR\_TOO\_MANY\_UNIQUE\_STATE\_OBJECTS                          | There are too many unique instances of a particular type of state object.                                             |
| D3D12\_ERROR\_TOO\_MANY\_UNIQUE\_VIEW\_OBJECTS                           | There are too many unique instances of a particular type of view object.                                              |
| D3DERR\_INVALIDCALL (replaced with DXGI\_ERROR\_INVALID\_CALL)           | The method call is invalid. For example, a method's parameter may not be a valid pointer.                             |
| D3DERR\_WASSTILLDRAWING (replaced with DXGI\_ERROR\_WAS\_STILL\_DRAWING) | The previous blit operation that is transferring information to or from this surface is incomplete.                   |
| E\_FAIL                                                                  | Attempted to create a device with the debug layer enabled and the layer is not installed.                             |
| E\_INVALIDARG                                                            | An invalid parameter was passed to the returning function.                                                            |
| E\_OUTOFMEMORY                                                           | Direct3D could not allocate sufficient memory to complete the call.                                                   |
| E\_NOTIMPL                                                               | The method call isn't implemented with the passed parameter combination.                                              |
| S\_FALSE                                                                 | Alternate success value, indicating a successful but nonstandard completion (the precise meaning depends on context). |
| S\_OK                                                                    | No error occurred.                                                                                                    |



 

## Related topics

<dl> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 




