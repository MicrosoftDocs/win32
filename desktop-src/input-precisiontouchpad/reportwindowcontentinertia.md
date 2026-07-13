---
title: ReportWindowContentInertia function (Winuser.h)
description: Reports to the system whether the specified window's content is in a state of inertia, enabling proper handling of subsequent touchpad input.
ms.topic: reference
ms.date: 03/28/2026
---

# ReportWindowContentInertia function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Reports to the system whether the specified window's content is in a state of inertia.

## Syntax

```cpp
WINUSERAPI
BOOL
WINAPI
ReportWindowContentInertia(
    HWND hWnd,
    BOOL bStartInertia);
```

## Parameters

<dl>
<dt><em>hWnd</em></dt>
<dd>

A handle to the window whose content inertia state is being reported.

</dd>
<dt><em>bStartInertia</em></dt>
<dd>

**TRUE** to report that the window's content has entered inertia; **FALSE** to report that inertia has stopped.

</dd>
</dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero.

## Remarks

Window content is "in inertia" if it continues to move after having been manipulated by input after the input stream has concluded. Report this inertia so that touchpad input can properly halt this motion when appropriate.

If a window is in inertia, the system changes how it responds to touchpad input:

- Shortly after new touchpad input arrives, the system will send **WM_STOPINERTIA** to the window. The application should react to this message by halting the motion of its content, but not necessarily transitioning out of the "in inertia" state if it has optimizations for repeated gestures manipulating the same content (for example, hit-testing input favoring content in inertia, or remembering the existing content velocity).
- If the system determines that the touchpad input is attempting to halt the content motion, the system will send **WM_ENDINERTIA** to the window. The application should react to this message by halting the motion of its content and exiting the "in inertia" state.

Example scenarios:

- The user performs a quick tap: **WM_ENDINERTIA** is sent. Mouse input is not produced — the tap only resulted in ending inertia.
- The user holds a finger on the touchpad and then lifts it: **WM_STOPINERTIA** followed by **WM_ENDINERTIA**.
- The user performs a quick two-finger gesture: No inertia messages. Repeated gestures are intended to be handled without needlessly halting the content.
- The user holds a finger (or two) on the touchpad and then performs a two-finger gesture: **WM_STOPINERTIA**. By dwelling before performing the gesture, it was possible the user was attempting to halt the content.

Although in most cases, receiving **WM_STOPINERTIA** is followed either by **WM_ENDINERTIA** or another touchpad gesture, it is not guaranteed. If applications implement a special content state upon receiving **WM_STOPINERTIA**, that state should be exited after some amount of time. Similarly, **WM_ENDINERTIA** may not necessarily be preceded by **WM_STOPINERTIA** if the touchpad input stream is short.

Reporting inertia is important for properly handling touchpad input. If a window's content is in inertia and it is not reported to the system, then tapping the touchpad will result in the normal behavior of a click (mouse left-down and left-up). The application may end up treating this mouse input as interacting with the content in motion, possibly resulting in performing an action the user did not intend.

For inertia caused by touch or pen input, the system does not need to specially handle the input with respect to inertia, because the window whose content is in inertia is typically the same one that receives the subsequent input. For touchpad input, contrarily, the system makes a decision before the application receives any input. Reporting inertia caused by touch or pen input is still recommended so that if the user attempts to stop the inertia with their touchpad, then the expected behavior occurs.

The system only keeps track of a single window in inertia. If inertia is already active when this API is called to report inertia starting on a different window, the previous inertia information will be replaced.

If reporting inertia starting, the specified window must be owned by the current thread and the thread must have retrieved input in the last two seconds. It should subsequently be reported as stopped once the window's content motion stops (unless the window received either **WM_STOPINERTIA** or **WM_ENDINERTIA**, in which case it is not necessary to report inertia stopping). Reporting inertia stopping will be silently ignored if the system is no longer tracking inertia, if the tracked window does not match the specified window, or if the tracked window is owned by a different process.

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 \[desktop apps only\] |
| Minimum supported server | None supported |
| Header | Winuser.h (include Windows.h) |
| Library | User32.lib |
| DLL | User32.dll (ordinal 2695) |

## See also

- [**RegisterTouchpadCapableWindow**](registertouchpadcapable.md)
- [**ProcessPointerFramesInteractionContext2**](processpointerframesinteractioncontext2.md)
- [Precision Touchpad Programming Guide](precision-touchpad-guide.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
