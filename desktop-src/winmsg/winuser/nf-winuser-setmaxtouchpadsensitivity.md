---
UID: NF:winuser.SetMaxTouchpadSensitivity
description: Forces the system to use the maximum touchpad sensitivity setting for the current process, disabling accidental activation prevention (AAP).
tech.root: winmsg
title: SetMaxTouchpadSensitivity function
ms.topic: reference
ms.date: 03/31/2026
req.lib: User32.lib
req.dll: User32.dll
topic_type:
- APIRef
api_type:
 - DllExport
api_location:
 - user32.dll
api_name:
 - SetMaxTouchpadSensitivity
f1_keywords:
 - SetMaxTouchpadSensitivity
 - winuser/SetMaxTouchpadSensitivity
dev_langs:
 - c++
helpviewer_keywords:
 - SetMaxTouchpadSensitivity
targetos: Windows
ms.localizationpriority: low
---

# SetMaxTouchpadSensitivity function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

**SetMaxTouchpadSensitivity** allows the system to handle touchpad input when the current process is in foreground as if the user had selected "Most Sensitive" for the touchpad's sensitivity setting, resulting in the touchpad input being unaffected by any simultaneous keyboard input that may be occurring.

## Syntax

```cpp
BOOL SetMaxTouchpadSensitivity(
    BOOL forceMaxSensitivity);
```

## Parameters

<dl>
<dt><em>forceMaxSensitivity</em> [in]</dt>
<dd>

If **TRUE**, the system will use the maximum touchpad sensitivity setting while the foreground window is owned by the current process. If **FALSE**, the user's setting will be used.

</dd>
</dl>

## Return value

Type: **BOOL**

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

[Accidental Activation Prevention](/windows-hardware/design/component-guidelines/touchpad-accidental-activation-prevention) (AAP) is a touchpad feature that suppresses mouse moves or taps generated from the touchpad that happen a certain time after keyboard input. AAP ensures that when a user is typing on their laptop keyboard they do not accidentally cause mouse input with their palm.

There are scenarios where it is not desirable to have AAP active. For instance, certain video games use WASD keys to move a character while the mouse (or touchpad) simultaneously rotates the camera. With AAP enabled (the default), when the user holds down W, the game will not receive any subsequent mouse input from the touchpad until the AAP timeout expires.

Users can work around this by setting the "Touchpad sensitivity" option to "Most sensitive" in the Settings app, but most users will not know about this setting. **SetMaxTouchpadSensitivity** allows applications to temporarily override the AAP behavior when needed, without requiring the user to change their system settings.

## Example

The following example shows how **SetMaxTouchpadSensitivity** could be integrated into a game engine to force maximum sensitivity when enabling third/first person controls (WASD and mouse) and restore the user's setting when those controls are no longer needed.

```cpp
// Called when switching to the keyboard being used for first/third person controls.
void SwitchKeyboardToGameInput()
{
    ...
    SetMaxTouchpadSensitivity(TRUE);
    ...
}

// Called when the keyboard can be used for text entry.
void SwitchToKeyboardAsTextEntry()
{
    ...
    SetMaxTouchpadSensitivity(FALSE);
    ...
}
```

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11 \[desktop apps only\] |
| **Target Platform** | Windows |
| **Header** | Winuser.h (include Windows.h) |
| **Library** | User32.lib |
| **DLL** | User32.dll (ordinal 2806) |
