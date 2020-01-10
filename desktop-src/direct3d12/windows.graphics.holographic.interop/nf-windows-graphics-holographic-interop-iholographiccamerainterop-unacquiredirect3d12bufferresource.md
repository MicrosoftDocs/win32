---
title: IHolographicCameraInterop::UnacquireDirect3D12BufferResource
description: Un-acquires a Direct3D 12 buffer resource.
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicCameraInterop::UnacquireDirect3D12BufferResource method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available only in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Un-acquires a Direct3D 12 buffer resource.

A resource that has been acquired, but not submitted, can be un-acquired to return control of the buffer back to the platform. A resource that has been un-acquired can be re-acquired at a later time. 

## Syntax

```cpp
HRESULT UnacquireDirect3D12BufferResource(
  ID3D12Resource *pResourceToUnacquire
);
```

## Parameters

`pResourceToUnacquire`
Type: **[ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource)\***

The Direct3D 12 resource to relinquish control of. The resource should be in the **D3D12_RESOURCE_STATE_COMMON** state when it is un-acquired.

## Returns
**S_OK** if successful, otherwise returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) error code indicating the reason for failure. Also see [COM Error Codes (UI, Audio, DirectX, Codec)](/windows/win32/com/com-error-codes-10).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |