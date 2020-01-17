---
title: IHolographicQuadLayerUpdateParametersInterop::CommitDirect3D12Resource
description: Commits a Direct3D 12 buffer for presentation on outputs associated with any [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) to which the quad layer is attached.
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicQuadLayerUpdateParametersInterop::CommitDirect3D12Resource method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available starting in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **CommitDirect3D12Resource** method commits a Direct3D 12 buffer for presentation on outputs associated with any [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) to which the quad layer is attached. The buffer must have been created by calling [CreateDirect3D12ContentBufferResource](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-createdirect3d12contentbufferresource) or [CreateDirect3D12HardwareProtectedContentBufferResource](nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-createdirect3d12hardwareprotectedcontentbufferresource.md) on the same [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer) corresponding to this update parameters object, and the buffer must have been acquired by your application prior to rendering.

## Syntax

```cpp
HRESULT CommitDirect3D12Resource(
  ID3D12Resource *pColorResourceToCommit,
  ID3D12Fence *pColorResourceFence,
  UINT64 colorResourceFenceSignalValue
);
```

## Parameters

`pColorResourceToCommit`
Type: **[ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource)\***

The Direct3D 12 texture resource with content to display when rendering the [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer) corresponding to this update parameters object. The content will also be displayed during any subsequent frames, until another content buffer update is provided for this [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer).

`pColorResourceFence`
Type: **[ID3D12Fence](/windows/win32/api/d3d12/nn-d3d12-id3d12fence)\***

A fence used to signal app work completion on the content buffer resource indicated by *pColorResourceToCommit*. Completion of this fence at the value indicated by *colorResourceFenceSignalValue* signals transfer of control of the content buffer resource from your application to the platform in the GPU work queue. The platform relies upon this fence, and the value indicated in *colorResourceFenceSignalValue*, to queue work on the GPU that reads from the content buffer.

`colorResourceFenceSignalValue`
Type: **[UINT64](/windows/win32/winprog/windows-data-types)**

The value used to signal work completion on *pColorResourceFence*. The platform relies upon this fence value to queue work on the GPU that reads from the content buffer.

## Returns
**S_OK** if successful, otherwise returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) error code indicating the reason for failure. Also see [COM Error Codes (UI, Audio, DirectX, Codec)](/windows/win32/com/com-error-codes-10).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |