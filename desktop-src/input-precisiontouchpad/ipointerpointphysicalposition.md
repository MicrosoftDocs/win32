---
title: IPointerPointPhysicalPosition interface (Windows.UI.Input)
description: Exposes properties on PointerPoint for retrieving the pointer's location in device-relative coordinates rather than display-independent pixels.
ms.topic: reference
ms.date: 03/28/2026
---

# IPointerPointPhysicalPosition interface

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

[**Windows.UI.Input.PointerPoint**](/uwp/api/windows.ui.input.pointerpoint) supports a new interface, **Windows.UI.Input.IPointerPointPhysicalPosition**. This interface exposes a property on the **PointerPoint** that returns the pointer's location in device-relative coordinates, rather than display-independent pixels.

**Namespace:** Windows.UI.Input

## Members

### IsPhysicalPositionSupported

```cpp
Boolean IsPhysicalPositionSupported { get; };
```

Returns whether the **PhysicalPosition** property is supported on the system. It should only be queried if supported.

### PhysicalPosition

```cpp
Windows.Foundation.Point PhysicalPosition { get; };
```

Returns the position of the pointer relative to the device. The device's dimensions can be queried using the **PhysicalDeviceRect** property on [**Windows.Devices.Input.PointerDevice**](/uwp/api/windows.devices.input.pointerdevice). Both of these properties use units where 96 represents one inch.

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 |
| Namespace | Windows.UI.Input |
| API contract | Windows.Foundation.UniversalApiContract (version 19) |
| IID | 003185a3-a5e7-4859-9c0b-89340204806c |

## See also

- [**PointerPoint**](/uwp/api/windows.ui.input.pointerpoint)
- [**PhysicalGestureRecognizer**](physicalgesturerecognizer.md)
- [**IPointerDeviceInterop**](ipointerdeviceinterop.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
