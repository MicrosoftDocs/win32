---
title: IHolographicQuadLayerUpdateParametersInterop
description: A nano-COM interface that allows COM interop with the [HolographicQuadLayerUpdateParameters](/uwp/api/windows.graphics.holographic.holographicquadlayerupdateparameters) class for applications that use Direct3D 12 for holographic rendering.
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicQuadLayerUpdateParametersInterop interface

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available only in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **IHolographicQuadLayerUpdateParametersInterop** interface is a nano-COM interface, used to commit Direct3D 12 buffer resources for quad layer rendering in the corresponding [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe).

The interface allows COM interop with the [HolographicQuadLayerUpdateParameters](/uwp/api/windows.graphics.holographic.holographicquadlayerupdateparameters) class for applications that use Direct3D 12 for holographic rendering. Nano-COM allows Direct3D 12 objects to be used directly as parameters for API calls, rather than going through a container object.

## Inheritance
The **IHolographicQuadLayerUpdateParametersInterop** interface inherits from the [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable) interface.

## Remarks
To use this interface in [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/), retrieve the [HolographicQuadLayerUpdateParameters](/uwp/api/windows.graphics.holographic.holographicquadlayerupdateparameters) object from the [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe), and then QueryInterface for the **IHolographicQuadLayerUpdateParametersInterop** interface.

```cppwinrt
auto quadLayerParameters{ holographicFrame.GetQuadLayerUpdateParameters(m_quadLayer) };
winrt::com_ptr<IHolographicQuadLayerUpdateParametersInterop> quadLayerParametersInterop{
    quadLayerParameters.as<IHolographicQuadLayerUpdateParametersInterop>() };
```

To use this interface in C++/CX, first cast the [HolographicQuadLayerUpdateParameters](/uwp/api/windows.graphics.holographic.holographicquadlayerupdateparameters) object (after retrieving it from the [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe)) to [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable)\*. Then QueryInterface for the **IHolographicQuadLayerUpdateParametersInterop** interface from the **IInspectable** pointer.

```cppcx
auto quadLayerParameters = holographicFrame->GetQuadLayerUpdateParameters(m_quadLayer);
Microsoft::WRL::ComPtr<IHolographicQuadLayerUpdateParametersInterop> quadLayerParametersInterop;
{
    Microsoft::WRL::ComPtr<IInspectable> iInspectable = reinterpret_cast<IInspectable*>(quadLayerParameters);
    DX::ThrowIfFailed(iInspectable.As(&quadLayerParamsInterop));
}
```

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |