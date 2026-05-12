---
title: IPointerDeviceInterop interface (Windows.Devices.Input.Interop.h)
description: Interop interface on PointerDevice that exposes the device HANDLE for use with Win32 APIs such as GetPointerDevice.
ms.topic: reference
ms.date: 03/28/2026
---

# IPointerDeviceInterop interface

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

[**Windows.Devices.Input.PointerDevice**](/uwp/api/windows.devices.input.pointerdevice) supports a new interop interface, **Windows.Devices.Input.IPointerDeviceInterop**. This interface exposes a property on the **PointerDevice** that returns the **HANDLE** corresponding to the device. This is the same handle used by Win32 APIs such as [**GetPointerDevice**](/windows/win32/api/winuser/nf-winuser-getpointerdevice).

**Namespace:** Windows.Devices.Input

**Header:** Windows.Devices.Input.Interop.h

## Syntax

```cpp
DECLARE_INTERFACE_IID_(IPointerDeviceInterop, IUnknown, "5CF79B90-F6A6-4741-99FB-A87D72924C05")
{
    IFACEMETHOD(get_IsDeviceHandleSupported)(
        _Out_ BOOL* value
    ) PURE;

    IFACEMETHOD(get_DeviceHandle)(
        _Outptr_ HANDLE * value
    ) PURE;
};
```

## Members

### get\_IsDeviceHandleSupported

```cpp
IFACEMETHOD(get_IsDeviceHandleSupported)(
    _Out_ BOOL* value
) PURE;
```

Returns whether the **DeviceHandle** property is supported on the system. The handle should only be queried if supported.

<dl>
<dt><em>value</em></dt>
<dd>

Receives **TRUE** if the device handle is supported; otherwise **FALSE**.

</dd>
</dl>

### get\_DeviceHandle

```cpp
IFACEMETHOD(get_DeviceHandle)(
    _Outptr_ HANDLE * value
) PURE;
```

Returns the pointer device handle corresponding to the device. This handle does not need to be closed.

<dl>
<dt><em>value</em></dt>
<dd>

Receives the **HANDLE** for the pointer device.

</dd>
</dl>

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 \[desktop apps only\] |
| Header | Windows.Devices.Input.Interop.h |
| IID | 5CF79B90-F6A6-4741-99FB-A87D72924C05 |

## See also

- [**PointerDevice**](/uwp/api/windows.devices.input.pointerdevice)
- [**IPointerPointPhysicalPosition**](ipointerpointphysicalposition.md)
- [**GetPointerDevice**](/windows/win32/api/winuser/nf-winuser-getpointerdevice)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
