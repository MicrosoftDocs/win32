---
title: Direct3D 11 Return Codes
description: The return codes from API functions.
ms.assetid: c0856a58-b760-44e5-8acf-145720b403d1
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 11 Return Codes

Return codes from API functions.

| HRESULT | Description |
|-|-|
| D3D11_ERROR_FILE_NOT_FOUND (0x887C0002) | The file was not found. |
| D3D11_ERROR_TOO_MANY_UNIQUE_STATE_OBJECTS (0x887C0001) | There are too many unique instances of a particular type of state object. |
| D3D11_ERROR_TOO_MANY_UNIQUE_VIEW_OBJECTS (0x887C0003) | There are too many unique instances of a particular type of view object. |
| D3D11_ERROR_DEFERRED_CONTEXT_MAP_WITHOUT_INITIAL_DISCARD (0x887C0004) | The first call to [**ID3D11DeviceContext::Map**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-map) after either [**ID3D11Device::CreateDeferredContext**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createdeferredcontext) or [**ID3D11DeviceContext::FinishCommandList**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-finishcommandlist) per Resource was not D3D11_MAP_WRITE_DISCARD. |
| D3DERR_INVALIDCALL (replaced with DXGI_ERROR_INVALID_CALL) (0x887A0001) | The method call is invalid. For example, a method's parameter may not be a valid pointer. |
| D3DERR_WASSTILLDRAWING (replaced with DXGI_ERROR_WAS_STILL_DRAWING) (0x887A000A) | The previous blit operation that is transferring information to or from this surface is incomplete. |
| E_FAIL (0x80004005) | Attempted to create a device with the debug layer enabled and the layer is not installed. |
| E_INVALIDARG (0x80070057) | An invalid parameter was passed to the returning function. |
| E_OUTOFMEMORY (0x8007000E) | Direct3D could not allocate sufficient memory to complete the call. |
| E_NOTIMPL (0x80004001) | The method call isn't implemented with the passed parameter combination. |
| S_FALSE ((HRESULT)1L) | Alternate success value, indicating a successful but nonstandard completion (the precise meaning depends on context). |
| S_OK ((HRESULT)0L) | No error occurred. |

For more return codes, see [DXGI_ERROR](/windows/desktop/direct3ddxgi/dxgi-error).

## Related topics

* [Direct3D 11 Reference](d3d11-graphics-reference.md)