---
title: Direct3D 11 Return Codes
description: The return codes from API functions.
ms.assetid: c0856a58-b760-44e5-8acf-145720b403d1
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 11 Return Codes

The return codes from API functions.



| HRESULT                                                                  | Description                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D11\_ERROR\_FILE\_NOT\_FOUND                                           | The file was not found.                                                                                                                                                                                                                                                                                                  |
| D3D11\_ERROR\_TOO\_MANY\_UNIQUE\_STATE\_OBJECTS                          | There are too many unique instances of a particular type of state object.                                                                                                                                                                                                                                                |
| D3D11\_ERROR\_TOO\_MANY\_UNIQUE\_VIEW\_OBJECTS                           | There are too many unique instances of a particular type of view object.                                                                                                                                                                                                                                                 |
| D3D11\_ERROR\_DEFERRED\_CONTEXT\_MAP\_WITHOUT\_INITIAL\_DISCARD          | The first call to [**ID3D11DeviceContext::Map**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-map) after either [**ID3D11Device::CreateDeferredContext**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createdeferredcontext) or [**ID3D11DeviceContext::FinishCommandList**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-finishcommandlist) per Resource was not D3D11\_MAP\_WRITE\_DISCARD. |
| D3DERR\_INVALIDCALL (replaced with DXGI\_ERROR\_INVALID\_CALL)           | The method call is invalid. For example, a method's parameter may not be a valid pointer.                                                                                                                                                                                                                                |
| D3DERR\_WASSTILLDRAWING (replaced with DXGI\_ERROR\_WAS\_STILL\_DRAWING) | The previous blit operation that is transferring information to or from this surface is incomplete.                                                                                                                                                                                                                      |
| E\_FAIL                                                                  | Attempted to create a device with the debug layer enabled and the layer is not installed.                                                                                                                                                                                                                                |
| E\_INVALIDARG                                                            | An invalid parameter was passed to the returning function.                                                                                                                                                                                                                                                               |
| E\_OUTOFMEMORY                                                           | Direct3D could not allocate sufficient memory to complete the call.                                                                                                                                                                                                                                                      |
| E\_NOTIMPL                                                               | The method call isn't implemented with the passed parameter combination.                                                                                                                                                                                                                                                 |
| S\_FALSE                                                                 | Alternate success value, indicating a successful but nonstandard completion (the precise meaning depends on context).                                                                                                                                                                                                    |
| S\_OK                                                                    | No error occurred.                                                                                                                                                                                                                                                                                                       |



 

For more return codes, see [DXGI\_ERROR](https://msdn.microsoft.com/library/windows/desktop/bb509553).

## Related topics

<dl> <dt>

[Direct3D 11 Reference](d3d11-graphics-reference.md)
</dt> </dl>

 

 




