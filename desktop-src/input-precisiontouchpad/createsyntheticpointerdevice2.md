---
title: CreateSyntheticPointerDevice2 function (Winuser.h)
description: Creates a synthetic pointer device using extended parameters, enabling touchpad input injection with physical device dimensions.
ms.topic: reference
ms.date: 03/28/2026
---

# CreateSyntheticPointerDevice2 function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates a synthetic pointer device using the associated parameters. Input can be injected using this device via [**InjectSyntheticPointerInput**](/windows/win32/api/winuser/nf-winuser-injectsyntheticpointerinput). When the injection device is no longer needed, it should be cleaned up via [**DestroySyntheticPointerDevice**](/windows/win32/api/winuser/nf-winuser-destroysyntheticpointerdevice).

## Syntax

```cpp
WINUSERAPI
HSYNTHETICPOINTERDEVICE
WINAPI
CreateSyntheticPointerDevice2(
    _In_ SYNTHETIC_DEVICE_CREATION_PARAMS* pParams);
```

## Parameters

<dl>
<dt><em>pParams</em></dt>
<dd>

A pointer to a [**SYNTHETIC_DEVICE_CREATION_PARAMS**](#synthetic_device_creation_params) structure containing the parameters for the device.

</dd>
</dl>

## Return value

If the function succeeds, the return value is a handle to the synthetic pointer device.

If the function fails, the return value is **NULL**. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

The existing [**CreateSyntheticPointerDevice**](/windows/win32/api/winuser/nf-winuser-createsyntheticpointerdevice) cannot be used to create touchpad devices, because touchpads must be created with a physical size.

## SYNTHETIC_DEVICE_CREATION_OPTIONS

Options for creating a synthetic pointer device.

```cpp
typedef enum tagSYNTHETIC_DEVICE_CREATION_OPTIONS
{
    SDCO_NONE                   = 0x0,
    SDCO_PHYSICAL_SIZE          = 0x1,
    SDCO_TOUCHPAD_GESTURE_ONLY  = 0x2,
} SYNTHETIC_DEVICE_CREATION_OPTIONS;
DEFINE_ENUM_FLAG_OPERATORS(SYNTHETIC_DEVICE_CREATION_OPTIONS)
```

| Value | Meaning |
|-------|---------|
| **SDCO_NONE** (0x0) | No special options. |
| **SDCO_PHYSICAL_SIZE** (0x1) | The injected input is relative to the device instead of to its mapped display(s). If specified, the device's dimensions must be provided. When injecting input using **InjectSyntheticPointerInput**, the input coordinates should be specified in the pointer info's **ptHimetricLocation** field instead of **ptPixelLocation**. |
| **SDCO_TOUCHPAD_GESTURE_ONLY** (0x2) | The injected touchpad input will always be treated as a gesture and cannot be recognized as mouse motion or clicks. If not specified, then the system will treat the injected touchpad input identically to physical touchpad input. |

## SYNTHETIC_DEVICE_CREATION_PARAMS

A structure representing the parameters for creating a synthetic injection device.

```cpp
typedef struct tagSYNTHETIC_DEVICE_CREATION_PARAMS
{
    POINTER_INPUT_TYPE pointerType;
    ULONG maxCount;
    POINTER_FEEDBACK_MODE feedbackMode;
    HMONITOR hMonitor;
    ULONG deviceWidth;
    ULONG deviceHeight;
    SYNTHETIC_DEVICE_CREATION_OPTIONS options;
} SYNTHETIC_DEVICE_CREATION_PARAMS;
```

### Members

<dl>
<dt><em>pointerType</em></dt>
<dd>

The type of device being created (**PT_TOUCH**, **PT_PEN**, or **PT_TOUCHPAD**).

</dd>
<dt><em>maxCount</em></dt>
<dd>

The maximum number of contacts that can be injected simultaneously.

</dd>
<dt><em>feedbackMode</em></dt>
<dd>

The mode in which the injected input has visual feedback rendered.

</dd>
<dt><em>hMonitor</em></dt>
<dd>

The monitor to which the injected input is mapped, if applicable.

</dd>
<dt><em>deviceWidth</em></dt>
<dd>

The physical width of the device in himetric (1/100th of a millimeter).

</dd>
<dt><em>deviceHeight</em></dt>
<dd>

The physical height of the device in himetric (1/100th of a millimeter).

</dd>
<dt><em>options</em></dt>
<dd>

Zero or more options from [**SYNTHETIC_DEVICE_CREATION_OPTIONS**](#synthetic_device_creation_options).

</dd>
</dl>

### Remarks

The **pointerType** and **options** fields control the valid values for the other fields:

**PT_TOUCH**:
- *maxCount* must be greater than 0 and less than or equal to 256.
- *feedbackMode* must be **POINTER_FEEDBACK_DEFAULT**, **POINTER_FEEDBACK_INDIRECT**, or **POINTER_FEEDBACK_NONE**.
- *hMonitor* can be **nullptr** (input is mapped to the virtual desktop) or a valid monitor.
- *deviceWidth* and *deviceHeight* must be non-zero if **SDCO_PHYSICAL_SIZE** is specified and zero if not.
- Only **SDCO_PHYSICAL_SIZE** is valid for options (or **SDCO_NONE**).

**PT_PEN**:
- *maxCount* must be 1.
- *feedbackMode* must be **POINTER_FEEDBACK_DEFAULT**, **POINTER_FEEDBACK_INDIRECT**, or **POINTER_FEEDBACK_NONE**.
- *hMonitor* can be **nullptr** or a valid monitor.
- *deviceWidth* and *deviceHeight* must be non-zero if **SDCO_PHYSICAL_SIZE** is specified and zero if not.
- Only **SDCO_PHYSICAL_SIZE** is valid for options (or **SDCO_NONE**).

**PT_TOUCHPAD**:
- *maxCount* must be greater than 0 and less than or equal to 5.
- *feedbackMode* must be **POINTER_FEEDBACK_NONE**.
- *hMonitor* must be **nullptr** (touchpad input is always mapped to the virtual desktop via the mouse location).
- *deviceWidth* and *deviceHeight* must be non-zero.
- **SDCO_PHYSICAL_SIZE** must be specified in options, **SDCO_TOUCHPAD_GESTURE_ONLY** is optional.

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 \[desktop apps only\] |
| Minimum supported server | None supported |
| Header | Winuser.h (include Windows.h) |
| Library | User32.lib |
| DLL | User32.dll (ordinal 2690) |

## See also

- [**InjectTouchpadAction**](injecttouchpadaction.md)
- [**InjectSyntheticPointerInput**](/windows/win32/api/winuser/nf-winuser-injectsyntheticpointerinput)
- [**DestroySyntheticPointerDevice**](/windows/win32/api/winuser/nf-winuser-destroysyntheticpointerdevice)
- [**CreateSyntheticPointerDevice**](/windows/win32/api/winuser/nf-winuser-createsyntheticpointerdevice)
- [Precision Touchpad Programming Guide](precision-touchpad-guide.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
