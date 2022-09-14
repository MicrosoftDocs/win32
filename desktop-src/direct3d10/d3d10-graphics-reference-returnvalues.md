---
description: The following table contains return codes from API functions.
ms.assetid: 7b67d428-d000-4c3e-adc1-b5fc67a15a6a
title: Direct3D 10 Return Codes
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 10 Return Codes

The following table contains return codes from API functions.



| HRESULT                                         | Description                                                                                                                                           |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D10\_ERROR\_FILE\_NOT\_FOUND                  | The file was not found.                                                                                                                               |
| D3D10\_ERROR\_TOO\_MANY\_UNIQUE\_STATE\_OBJECTS | There are too many unique instances of a particular type of [state object](d3d10-graphics-programming-guide-api-features-state-objects.md).          |
| D3DERR\_INVALIDCALL                             | The method call is invalid. For example, a method's parameter may not be a valid pointer.                                                             |
| D3DERR\_WASSTILLDRAWING                         | The previous blit operation that is transferring information to or from this surface is incomplete.                                                   |
| E\_FAIL                                         | Attempted to create a device with the [debug layer](d3d10-graphics-programming-guide-api-features-layers.md) enabled and the layer is not installed. |
| E\_INVALIDARG                                   | An invalid parameter was passed to the returning function.                                                                                            |
| E\_OUTOFMEMORY                                  | Direct3D could not allocate sufficient memory to complete the call.                                                                                   |
| E\_NOTIMPL                                      | The method call isn't implemented with the passed parameter combination.                                                                              |
| S\_FALSE                                        | Alternate success value, indicating a successful but nonstandard completion (the precise meaning depends on context).                                 |
| S\_OK                                           | No error occurred.                                                                                                                                    |



 

To write code that handles [HRESULT values](../winprog/windows-data-types.md) robustly, use the SUCCEEDED(hr) and FAILED(hr) macros.

## Related topics

<dl> <dt>

[Direct3D Reference](d3d10-graphics-reference-d3d10.md)
</dt> <dt>

[Reference for Direct3D 10](d3d10-graphics-reference.md)
</dt> </dl>

 

 
