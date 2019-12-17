---
title: IHolographicCameraInterop
description: Extends [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) to allow 2D texture resources to be created and used as content buffers for apps using Direct3D 12 for holographic rendering.
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicCameraInterop interface

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available only in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Extends [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) to allow 2D texture resources to be created and used as content buffers for apps using Direct3D 12 for holographic rendering.

Your application can use this interface to do holographic rendering using Direct3D 12 with minimal overhead. Nano-COM allows Direct3D 12 objects to be used as parameters for API calls directly, rather than by using a container object to pass pointers to devices and resources.

The **IHolographicCameraInterop** interface allows your application to create Direct3D 12 surfaces that interoperate with Windows Mixed Reality APIs. It also allows your application to acquire surfaces for rendering, and subsequently to commit those surfaces before presenting a [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe).

Your application manages its own pool of holographic buffer resources; it can create additional surfaces as needed in order to continue rendering smoothly. On most devices, this will be 3 or 4 surfaces. Your application should start with at least 2 surfaces in the pool. Your application can dynamically detect when it needs to create a new surface by looking for failed attempts to immediately acquire surfaces that were previously committed for presentation.

A buffer created by a [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) object can be used only with that object. It should be released when the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) is released, or when the Direct3D 12 device needs to be recreated&mdash;whichever happens first.

## Inheritance
The **IHolographicCameraInterop** interface inherits from the [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable) interface.

## Remarks
To use this interface in [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/), QueryInterface for the **IHolographicCameraInterop** interface from the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) object.

```cppwinrt
winrt::com_ptr<IHolographicCameraInterop> spCameraInterop{
    m_holographicCamera.as<IHolographicCameraInterop>() };

D3D12_RESOURCE_DESC bufferDesc{};
bufferDesc.Format = SelectFormatUsingHolographicViewConfiguration(m_holographicCamera.ViewConfiguration());
bufferDesc.SampleDesc.Count = 1;
bufferDesc.SampleDesc.Quality = 0;
bufferDesc.MipLevels = 1;
bufferDesc.Width = static_cast<UINT64>(m_holographicCamera.ViewConfiguration().RenderTargetSize().Width);
bufferDesc.Height = static_cast<UINT64>(m_holographicCamera.ViewConfiguration().RenderTargetSize().Height);

winrt::check_hresult(spCameraInterop->CreateDirect3D12BackBufferResource(
    m_deviceResources->GetD3D12Device(),
    &bufferDesc,
    &m_D3D12BackBuffer[m_contentBufferIndex]));
```

Note that you can use the [HolographicViewConfiguration](/uwp/api/windows.graphics.holographic.holographicviewconfiguration) API to determine the available options for buffer format, and to acquire information about render target size for the [HolographicDisplay](/uwp/api/windows.graphics.holographic.holographicdisplay). If your application needs to change the buffer size for Direct3D 12 buffers from the default render target size for the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera), it should still request a new render target size using the [HolographicViewConfiguration::RequestRenderTargetSize method](/uwp/api/windows.graphics.holographic.holographicviewconfiguration.requestrendertargetsize), and create buffers using the size chosen by that method.

Your Direct3D 12 application can use a viewport size chosen independently by the application. In that case, you must call the [HolographicCameraPose.OverrideViewport](/uwp/api/windows.graphics.holographic.holographiccamerapose.overrideviewport) method each frame to inform the platform about the viewport used for rendering.

To use this interface in C++/CX, cast the [HolographicCamera](/uwp/api/windows.graphics.holographic.holographiccamera) object to [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable)\*. Then QueryInterface for the **IHolographicCameraInterop** interface from the **IInspectable** pointer.

```cppcx
Microsoft::WRL::ComPtr<IInspectable> spCamera = reinterpret_cast<IInspectable*>(m_holographicCamera);
Microsoft::WRL::ComPtr<IHolographicCameraInterop> spCameraInterop;
DX::ThrowIfFailed(spCamera.As(&spCameraInterop));

D3D12_RESOURCE_DESC bufferDesc {};
bufferDesc.Format = SelectFormatUsingHolographicViewConfiguration(m_holographicCamera->ViewConfiguration);
bufferDesc.SampleDesc.Count = 1;
bufferDesc.SampleDesc.Quality = 0;
bufferDesc.MipLevels = 1;
bufferDesc.Width = static_cast<UINT64>(m_holographicCamera->ViewConfiguration->RenderTargetSize.Width);
bufferDesc.Height = static_cast<UINT64>(m_holographicCamera->ViewConfiguration->RenderTargetSize.Height);

DX::ThrowIfFailed(spCameraInterop->CreateDirect3D12BackBufferResource(
    m_deviceResources->GetD3D12Device(),
    &bufferDesc,
    &m_D3D12BackBuffer[m_contentBufferIndex]));
```

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |