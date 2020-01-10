---
title: Windows.Graphics.Holographic.Interop.h header
description: This section covers APIs for Direct3D 12-based graphics programming.
ms.assetid: C4958E15-28BA-4275-882B-244D4CC22E1A
ms.localizationpriority: low
ms.topic: article
ms.date: 04/19/2019
ms.custom: 19H1
---

# Windows.Graphics.Holographic.Interop.h header

## Description

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available only in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

This header is used to interoperate with types in the [Windows.Graphics.Holographic](/uwp/api/windows.graphics.holographic) namespace.

| Interface | Method |
|-|-|
| [**IHolographicCameraInterop**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nn-windows-graphics-holographic-interop-iholographiccamerainterop) | |
| | [**AcquireDirect3D12BufferResource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographiccamerainterop-acquiredirect3d12bufferresource) |
| | [**AcquireDirect3D12BufferResourceWithTimeout**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographiccamerainterop-acquiredirect3d12bufferresourcewithtimeout) |
| | [**CreateDirect3D12BackBufferResource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographiccamerainterop-createdirect3d12backbufferresource) |
| | [**CreateDirect3D12HardwareProtectedBackBufferResource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographiccamerainterop-createdirect3d12hardwareprotectedbackbufferresource) |
| | [**UnacquireDirect3D12BufferResource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographiccamerainterop-unacquiredirect3d12bufferresource) |
| [**IHolographicCameraRenderingParametersInterop**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nn-windows-graphics-holographic-interop-iholographiccamerarenderingparametersinterop) | |
| | [**CommitDirect3D12Resource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographiccamerarenderingparametersinterop-commitdirect3d12resource) |
| | [**CommitDirect3D12ResourceWithDepthData**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographiccamerarenderingparametersinterop-commitdirect3d12resourcewithdepthdata) |
| [**IHolographicQuadLayerInterop**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nn-windows-graphics-holographic-interop-iholographicquadlayerinterop) | |
| | [**AcquireDirect3D12BufferResource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-acquiredirect3d12bufferresource) |
| | [**AcquireDirect3D12BufferResourceWithTimeout**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-acquiredirect3d12bufferresourcewithtimeout) |
| | [**CreateDirect3D12ContentBufferResource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-createdirect3d12contentbufferresource) |
| | [**CreateDirect3D12HardwareProtectedContentBufferResource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-createdirect3d12hardwareprotectedcontentbufferresource) |
| | [**UnacquireDirect3D12BufferResource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerinterop-unacquiredirect3d12bufferresource) |
| [**IHolographicQuadLayerUpdateParametersInterop**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nn-windows-graphics-holographic-interop-iholographicquadlayerupdateparametersinterop) | |
| | [**CommitDirect3D12Resource**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nf-windows-graphics-holographic-interop-iholographicquadlayerupdateparametersinterop-commitdirect3d12resource) |