---
title: IHolographicCameraRenderingParametersInterop
description: A nano-COM interface that allows COM interop with the [HolographicCameraRenderingParameters](/uwp/api/windows.graphics.holographic.holographiccamerarenderingparameters) class for applications that use Direct3D 12 for holographic rendering.
ms.localizationpriority: low
ms.topic: reference
ms.date: 12/13/2019
---

# IHolographicCameraRenderingParametersInterop interface

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is implemented in 
Windows 10, version 1903 (10.0; Build 18362), but the `Windows.Graphics.Holographic.Interop.h` header file is available starting in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

The **IHolographicCameraRenderingParametersInterop** interface is a nano-COM interface that is used to commit Direct3D 12 buffer resources for presentation during the corresponding [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe).

The **IHolographicCameraRenderingParametersInterop** interface allows COM interop with the [HolographicCameraRenderingParameters](/uwp/api/windows.graphics.holographic.holographiccamerarenderingparameters) WinRT class for applications that use Direct3D 12 for holographic rendering. Nano-COM allows Direct3D 12 objects to be used as parameters for API calls directly, rather than going through a container object.

## Inheritance
The **IHolographicCameraRenderingParametersInterop** interface inherits from the [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable) interface.

## Remarks
To use this interface in [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/), retrieve the [HolographicCameraRenderingParameters](/uwp/api/windows.graphics.holographic.holographiccamerarenderingparameters) object from the [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe), and then QueryInterface for the **IHolographicCameraRenderingParametersInterop** interface.

```cppwinrt
auto holographicCameraRenderingParameters { holographicFrame.GetRenderingParameters(m_cameraPose) };
winrt::com_ptr<IHolographicCameraRenderingParametersInterop> holographicCameraRenderingParametersInterop
{
    holographicCameraRenderingParameters.as<IHolographicCameraRenderingParametersInterop>();
};
```

To use this interface in C++/CX, first cast the [HolographicCameraRenderingParameters](/uwp/api/windows.graphics.holographic.holographiccamerarenderingparameters) object (after retrieving it from the [HolographicFrame](/uwp/api/windows.graphics.holographic.holographicframe)) to [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable)\*. Then QueryInterface for the **IHolographicCameraRenderingParametersInterop** interface from the **IInspectable** pointer.

```cppcx
auto holographicCameraRenderingParameters = 
    holographicFrame->GetRenderingParameters(m_cameraPose);
Microsoft::WRL::ComPtr<IHolographicCameraRenderingParametersInterop> 
    holographicCameraRenderingParametersInterop;
{
    Microsoft::WRL::ComPtr<IInspectable> iInspectable = reinterpret_cast<IInspectable*>(holographicCameraRenderingParameters);
    DX::ThrowIfFailed(iInspectable.As(&holographicCameraRenderingParametersInterop));
}
```

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.graphics.holographic.interop.h |