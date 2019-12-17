---
title: IHolographicCameraRenderingParametersInterop::CommitDirect3D12ResourceWithDepthData
description: Commits a Direct3D 12 buffer for presentation on outputs associated with the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera).
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicCameraRenderingParametersInterop::CommitDirect3D12ResourceWithDepthData method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available only in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Commits a Direct3D 12 buffer for presentation on outputs associated with the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera). The buffer must have been created by calling [CreateDirect3D12BackBufferResource](/windows/win32/api/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographiccamerainterop-createdirect3d12backbufferresource) or [CreateDirect3D12HardwareProtectedBackBufferResource](nf-windows-graphics-holographic-interop-iholographiccamerainterop-createdirect3d12hardwareprotectedbackbufferresource.md) on the same [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera).

This method also accepts an optional depth buffer parameter, along with fence and fence value for app work completion on that buffer. This depth buffer will be used for image stabilization when showing the frame it is committed to. The depth buffer must contain depth data correlated with geometry used to draw holograms in the color buffer, which is submitted at the same time. The depth buffer should not contain depth data for invisible content, such as depth data used for occlusion.

## Syntax

```cpp
HRESULT CommitDirect3D12ResourceWithDepthData(
  ID3D12Resource *pColorResourceToCommit,
  ID3D12Fence *pColorResourceFence,
  UINT64 colorResourceFenceSignalValue,
  ID3D12Resource *pDepthResourceToCommit,
  ID3D12Fence *pDepthResourceFence,
  UINT64 depthResourceFenceSignalValue
);
```

## Parameters

`pColorResourceToCommit`
Type: **[ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource)\***

The Direct3D 12 texture resource with content to display when presenting the [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe) used to retrieve this object.

`pColorResourceFence`
Type: **[ID3D12Fence](/windows/win32/api/d3d12/nn-d3d12-id3d12fence)\***

A fence used to signal work completion on `pColorResourceToCommit`. The platform relies upon this fence to queue work on the GPU that reads from the buffer.

`colorResourceFenceSignalValue`
Type: **[UINT64](/windows/win32/winprog/windows-data-types)**

The fence value used to signal work completion on the texture resource. The platform relies upon this fence value to queue work on the GPU that reads from the buffer.

`pDepthResourceToCommit`
Type: **[ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource)\***

The Direct3D 12 depth buffer with depth data for image stabilization. Typically used as the depth stencil when rendering to `pColorResourceToCommit`, or derived from the same rendering pass.

`pDepthResourceFence`
Type: **[ID3D12Fence](/windows/win32/api/d3d12/nn-d3d12-id3d12fence)\***

A fence used to signal work completion on `pDepthResourceToCommit`. The platform relies upon this fence to queue work on the GPU that reads from the depth buffer.

`depthResourceFenceSignalValue`
Type: **[UINT64](/windows/win32/winprog/windows-data-types)**

The value used to signal work completion on the depth resource fence. The platform relies upon this fence value to queue work on the GPU that reads from the depth buffer.

## Returns
**S_OK** if successful, otherwise returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) error code indicating the reason for failure. Also see [COM Error Codes (UI, Audio, DirectX, Codec)](/windows/win32/com/com-error-codes-10).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |