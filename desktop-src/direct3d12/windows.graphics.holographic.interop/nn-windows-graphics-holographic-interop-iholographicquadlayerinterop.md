---
title: IHolographicQuadLayerInterop
description: A nano-COM interface that allows COM interop with the [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer) Windows Runtime class for apps that use Direct3D 12 for holographic rendering.
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicQuadLayerInterop interface

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available starting in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **IHolographicQuadLayerInterop** interface is a nano-COM interface, used to create Direct3D 12 content buffers for a [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer) Windows Runtime object. This is an initialization step for using Direct3D 12 with Windows Mixed Reality quad layers. It also allows your application to acquire ownership of content buffers for rendering, prior to committing them with the [**IHolographicQuadLayerUpdateParametersInterop**](/windows/win32/direct3d12/windows.graphics.holographic.interop/nn-windows-graphics-holographic-interop-iholographicquadlayerupdateparametersinterop) interface.

Your application can use **IHolographicQuadLayerInterop** to initialize Direct3D 12 content buffer resources for holographic quad layers. Nano-COM allows pointers to Direct3D 12 objects to be passed directly as parameters for API calls, instead of using a Windows Runtime container object.

Your application manages its own pool of holographic content buffer resources. It can create additional buffers as needed in order to continue rendering smoothly. On most devices, this will be three or four buffers. Your application should start with at least two buffers in the pool. Your application can dynamically detect when it needs to create a new buffer by looking for failed attempts to immediately acquire buffers that were previously committed for presentation. A quad layer content buffer will continue to be presented each frame until a new buffer is committed.

A buffer created by a [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer) object can be used only with that object. It should be released when the **HolographicQuadLayer** is released, or when the Direct3D 12 device needs to be recreated&mdash;whichever happens first. The buffer must not be in the GPU pipeline when it is released&mdash;Direct3D 12 fences should be used to ensure that this condition is met prior to releasing the buffer object.

## Inheritance
The **IHolographicQuadLayerInterop** interface inherits from the [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable) interface.

## Remarks
To use this interface in [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/), QueryInterface for the **IHolographicQuadLayerInterop** interface from the [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer) object.

Note that you can use the [HolographicViewConfiguration](/uwp/api/windows.graphics.holographic.holographicviewconfiguration) API to determine the available options for buffer format.

```cppwinrt
m_quadLayer = HolographicQuadLayer{ {1024, 1024} };
winrt::com_ptr<IHolographicQuadLayerInterop> quadLayerInterop{
    m_quadLayer.as<IHolographicQuadLayerInterop>() };

// Create/acquire buffer.
if (!m_D3D12ContentBuffer[m_contentBufferIndex])
{
    D3D12_RESOURCE_DESC bufferDesc{ sourceDesc };
    bufferDesc.Format = DXGI_FORMAT_R8G8B8A8_UNORM;
    bufferDesc.SampleDesc.Count = 1;
    bufferDesc.SampleDesc.Quality = 0;
    bufferDesc.MipLevels = 1;

    winrt::check_hresult(
        quadLayerInterop->CreateDirect3D12ContentBufferResource(
            m_deviceResources->GetD3D12Device(),
            &bufferDesc,
            &m_D3D12ContentBuffer[m_contentBufferIndex]));
}
```

To use this interface in C++/CX, cast the [HolographicQuadLayer](/uwp/api/windows.graphics.holographic.holographicquadlayer) object to [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable)\*. Then QueryInterface for the **IHolographicQuadLayerInterop** interface from the **IInspectable** pointer.

```cppcx
m_quadLayer = ref new HolographicQuadLayer();
Microsoft::WRL::ComPtr<IHolographicQuadLayerInterop> quadLayerInterop;
{
    Microsoft::WRL::ComPtr<IInspectable> iInspectable = reinterpret_cast<IInspectable*>(m_quadLayer);
    DX::ThrowIfFailed(iInspectable.As(&quadLayerInterop));
}

// Create/acquire buffer.
if (!m_D3D12ContentBuffer[m_contentBufferIndex])
{
    D3D12_RESOURCE_DESC bufferDesc = sourceDesc;
    bufferDesc.Format = DXGI_FORMAT_R8G8B8A8_UNORM;
    bufferDesc.SampleDesc.Count = 1;
    bufferDesc.SampleDesc.Quality = 0;
    bufferDesc.MipLevels = 1;

    DX::ThrowIfFailed(quadLayerInterop->CreateDirect3D12ContentBufferResource(
        m_deviceResources->GetD3D12Device(),
        &bufferDesc,
        &m_D3D12ContentBuffer[m_contentBufferIndex]));
}
```

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |