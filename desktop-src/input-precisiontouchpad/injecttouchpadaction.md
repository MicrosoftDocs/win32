---
title: InjectTouchpadAction function (Winuser.h)
description: Injects the specified touchpad action using the specified synthetic pointer device.
ms.topic: reference
ms.date: 03/28/2026
---

# InjectTouchpadAction function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Injects the specified action, using the specified device as the originator.

## Syntax

```cpp
WINUSERAPI
BOOL
WINAPI
InjectTouchpadAction(
    HSYNTHETICPOINTERDEVICE hDevice,
    TOUCHPAD_ACTION action);
```

## Parameters

<dl>
<dt><em>hDevice</em></dt>
<dd>

A handle to a synthetic pointer device previously created using [**CreateSyntheticPointerDevice2**](createsyntheticpointerdevice2.md).

</dd>
<dt><em>action</em></dt>
<dd>

A value from the [**TOUCHPAD_ACTION**](#touchpad_action) enumeration specifying the action to inject.

</dd>
</dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## TOUCHPAD_ACTION

Represents the action being injected.

```cpp
typedef enum tagTOUCHPAD_ACTION
{
    TA_3FINGER_TAP,
    TA_3FINGER_PRESS,
    TA_3FINGER_RELEASE,
    TA_4FINGER_TAP,
    TA_4FINGER_PRESS,
    TA_4FINGER_RELEASE,
    TA_5FINGER_TAP,
    TA_5FINGER_PRESS,
    TA_5FINGER_RELEASE,
    TA_INERTIA_STOP,
    TA_INERTIA_END,
} TOUCHPAD_ACTION;
```

| Value | Meaning |
|-------|---------|
| **TA_3FINGER_TAP** | Injects a three-finger tap gesture. |
| **TA_3FINGER_PRESS** | Injects a three-finger button press gesture. |
| **TA_3FINGER_RELEASE** | Injects a three-finger button release gesture. |
| **TA_4FINGER_TAP** | Injects a four-finger tap gesture. |
| **TA_4FINGER_PRESS** | Injects a four-finger button press gesture. |
| **TA_4FINGER_RELEASE** | Injects a four-finger button release gesture. |
| **TA_5FINGER_TAP** | Injects a five-finger tap gesture. |
| **TA_5FINGER_PRESS** | Injects a five-finger button press gesture. |
| **TA_5FINGER_RELEASE** | Injects a five-finger button release gesture. |
| **TA_INERTIA_STOP** | Produces a **WM_STOPINERTIA** message to the tracked inertia window. |
| **TA_INERTIA_END** | Produces a **WM_ENDINERTIA** message to the tracked inertia window. |

## Remarks

This API is designed to be used in conjunction with an injected touchpad device created with the **SDCO_TOUCHPAD_GESTURE_ONLY** option. If the touchpad is not gesture-only, the system will produce these actions in response to processing the touchpad's input.

The finger tap/press/release actions correspond to the global touchpad gestures. See [**TouchpadGesturesController**](touchpadgesturescontroller.md) for more information about how these gestures are handled.

The inertia actions produce **WM_STOPINERTIA** or **WM_ENDINERTIA** messages, respectively. See [**ReportWindowContentInertia**](reportwindowcontentinertia.md) for more information about inertia handling.

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 \[desktop apps only\] |
| Minimum supported server | None supported |
| Header | Winuser.h (include Windows.h) |
| Library | User32.lib |
| DLL | User32.dll (ordinal 2803) |

## See also

- [**CreateSyntheticPointerDevice2**](createsyntheticpointerdevice2.md)
- [**TouchpadGesturesController**](touchpadgesturescontroller.md)
- [**ReportWindowContentInertia**](reportwindowcontentinertia.md)
- [Precision Touchpad Programming Guide](precision-touchpad-guide.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
