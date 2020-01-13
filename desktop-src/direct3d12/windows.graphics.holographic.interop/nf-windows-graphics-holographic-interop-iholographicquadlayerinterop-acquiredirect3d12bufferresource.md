---
title: IHolographicQuadLayerInterop::AcquireDirect3D12BufferResource
description: Acquires a Direct3D 12 buffer resource.
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicQuadLayerInterop::AcquireDirect3D12BufferResource method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available starting in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **AcquireDirect3D12BufferResource** method transitions ownership of a Direct3D 12 content buffer resource from the platform to the app. If the app already owns control of the resource, the acquisition is considered to be a success.

After committing a resource to a [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe) by calling [IHolographicQuadLayerUpdateParametersInterop::CommitDirect3D12Resource](/windows/win32/api/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerupdateparametersinterop-commitdirect3d12resource), your application should consider control of that resource to be relinquished to the system until such a time as it is reacquired by the app using this method. The system owns the buffer until it is no longer needed for presenting the quad layer. To determine whether the system has relinquished control of the buffer, call **AcquireDirect3D12BufferResource** or **AcquireDirect3D12BufferResourceWithTimeout**. If the buffer cannot be acquired by the time your application is ready to start rendering a new update for the quad layer, then you should create a new resource and add it to the buffer queue or limit the queue size by waiting for a buffer to become available.

If the buffer is not ready to be acquired when this method is called, the method call will fail and immediately return the error code **E_NOTREADY**.

Your application can limit the queue size by calling [AcquireDirect3D12BufferResourceWithTimeout](/windows/win32/api/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-acquiredirect3d12bufferresourcewithtimeout) to wait until a resource becomes available before queuing more work.

## Syntax

```cpp
HRESULT AcquireDirect3D12BufferResource(
  ID3D12Resource *pResourceToAcquire,
  ID3D12CommandQueue *pCommandQueue
);
```

## Parameters

`pResourceToAcquire`
Type: **[ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource)\***

The Direct3D 12 resource to acquire. The resource will be in the **D3D12_RESOURCE_STATE_COMMON** state when it is acquired.

`pCommandQueue`
Type: **[ID3D12CommandQueue](/windows/win32/api/d3d12/nn-d3d12-id3d12commandqueue)\***

The Direct3D 12 command queue to use for transitioning the state of this resource when acquiring it for your application.

## Returns
**S_OK** if successful, otherwise returns an [HRESULT](/windows/win32/com/structure-of-com-error-codes) error code indicating the reason for failure. Also see [COM Error Codes (UI, Audio, DirectX, Codec)](/windows/win32/com/com-error-codes-10).

## See also
[AcquireDirect3D12BufferResourceWithTimeout](/windows/win32/api/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-acquiredirect3d12bufferresourcewithtimeout)

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |