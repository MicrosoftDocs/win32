---
title: IHolographicCameraInterop
description: Extends [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) to allow 2D texture resources to be created and used as back buffers for holographic rendering in Direct3D 12.
ms.localizationpriority: low
ms.topic: reference
ms.date: 1/10/2020
---

# IHolographicCameraInterop interface

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available starting in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **IHolographicCameraInterop** interface is a nano-COM interface which is used to create Direct3D 12 back buffer resources for a [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) WinRT API object. This is an initialization step for using Direct3D 12 with Windows Mixed Reality. This interface also allows your application to acquire ownership of content buffers for rendering, prior to committing them with the [HolographicCameraRenderingParametersInterop API](/windows/win32/direct3d12/windows.graphics.holographic.interop/nn-windows-graphics-holographic-interop-iholographiccamerarenderingparametersinterop) interface.

Your application can use this interface to initialize holographic rendering using Direct3D 12. Nano-COM allows pointers to Direct3D 12 objects to be passed as parameters for API calls directly, instead of using a WinRT container object.

Your application manages its own pool of holographic buffer resources for use as render targets (back buffers) for each HolographicCamera. It can create additional buffers as needed in order to continue rendering smoothly. On most devices, this will be 3 or 4 surfaces. Your application should start with at least 2 buffers in the pool. Your application can dynamically detect when it needs to create a new buffer by looking for unsuccessful attempts to immediately acquire buffers that were previously committed for presentation. Your application must commit a buffer for a [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) that is included on the HolographicFrame unless the primary layer is disabled for that camera, in which case your app must not commit a buffer for that camera.

A buffer created by a [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) object can be used only with that object. It should be released when the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) is released, or when the Direct3D 12 device needs to be recreated&mdash;whichever happens first. The buffer must not be in the GPU pipeline when it is released - Direct3D 12 fences should be used to ensure that this condition is met prior to releasing the buffer object.

## Inheritance
The **IHolographicCameraInterop** interface inherits from the [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable) interface.

## Remarks
To use this interface in [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/), QueryInterface for the **IHolographicCameraInterop** interface from the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) object.

```cppwinrt
winrt::com_ptr<IHolographicCameraInterop> spCameraInterop {
    m_holographicCamera.as<IHolographicCameraInterop>() };

D3D12_RESOURCE_DESC bufferDesc { };
bufferDesc.Format =
  SelectFormatUsingHolographicViewConfiguration(
    m_holographicCamera.ViewConfiguration());
bufferDesc.SampleDesc.Count = 1;
bufferDesc.SampleDesc.Quality = 0;
bufferDesc.MipLevels = 1;
bufferDesc.Width = static_cast<UINT64>(
  m_holographicCamera.ViewConfiguration().RenderTargetSize().Width);
bufferDesc.Height = static_cast<UINT64>(
  m_holographicCamera.ViewConfiguration().RenderTargetSize().Height);

winrt::check_hresult(
  spCameraInterop->CreateDirect3D12BackBufferResource(
    m_deviceResources->GetD3D12Device(),
    &bufferDesc,
    &m_D3D12BackBuffer[m_contentBufferIndex]));
```

Note that you can use the [HolographicViewConfiguration](/uwp/api/windows.graphics.holographic.holographicviewconfiguration) API to determine the available options for buffer format, and to acquire information about render target size for the corresponding output - for example, the [HolographicDisplay](/uwp/api/windows.graphics.holographic.holographicdisplay). If your application needs to change the buffer size for Direct3D 12 buffers from the default render target size for the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera), it should either request a new render target size using the [HolographicViewConfiguration::RequestRenderTargetSize method](/uwp/api/windows.graphics.holographic.holographicviewconfiguration.requestrendertargetsize) and create buffers using the size returned by that method, or choose an arbitrary size and override the viewport as described in the following paragraph.

Your Direct3D 12 application can use a viewport size chosen independently by the application. In that case, you must call the [HolographicCameraPose.OverrideViewport](/uwp/api/windows.graphics.holographic.holographiccamerapose.overrideviewport) method each frame to inform the platform about the viewport used for rendering.

To use this interface in [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/), QueryInterface for the  **IHolographicCameraInterop** interface interface from the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) object.. The following code excerpt is from the [Windows Mixed Reality D3D12 app template](https://marketplace.visualstudio.com/items?itemName=WindowsMixedRealityteam.WindowsMixedRealityAppTemplatesVSIX), which includes boilerplate code for most APIs that are provided in the Windows.Graphics.Holographic.Interop.h header:

```cppwinrt
winrt::com_ptr<IHolographicCameraInterop> spCameraInterop = 
    m_holographicCamera.as<IHolographicCameraInterop>();
winrt::check_hresult(
    spCameraInterop->CreateDirect3D12BackBufferResource(
        spD3D12Device.get(),
        &bufferDesc,
        m_spD3D12BackBuffer[bufferSlot].put()));
```

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |