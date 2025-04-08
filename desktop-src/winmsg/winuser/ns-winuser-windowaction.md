---
UID: NS:winuser.WINDOW_ACTION
description: Structure defining changes to a top-level window that can be applied using ApplyWindowAction.
tech.root: winmsg
title: WINDOW_ACTION structure
ms.topic: reference
ms.date: 3/22/2025
req.lib: 
req.dll: User32.dll
api_type:
 - DllExport
api_location:
 - user32.dll
api_name:
 - WINDOW_ACTION
f1_keywords:
 - WINDOW_ACTION
 - winuser/WINDOW_ACTION
dev_langs:
 - c++
helpviewer_keywords:
 - WINDOW_ACTION
targetos: Windows
ms.localizationpriority: low
---

# WINDOW_ACTION structure

Used by the API
[ApplyWindowAction](nf-winuser-applywindowaction.md)
and
[WM_INTERCEPTED_WINDOW_ACTION](ns-winuser-wminterceptedwindowaction.md)
. This structure describes one or more changes to a top level window's position,
size, state, and other related fields.

## Syntax

```cpp
enum WINDOW_ACTION_KINDS
{
    WAK_NONE                    = 0x0000,

    WAK_VISIBILITY              = 0x0001,
    WAK_POSITION                = 0x0002,
    WAK_SIZE                    = 0x0004,
    WAK_INSERT_AFTER            = 0x0008,
    WAK_ACTIVATE                = 0x0010,
    WAK_PLACEMENT_STATE         = 0x0020,
    WAK_NORMAL_RECT             = 0x0040,
    WAK_MOVE_TO_MONITOR         = 0x0080,
    WAK_FIT_TO_MONITOR          = 0x0100,
    WAK_DISPLAY_CHANGE          = 0x0200,
    WAK_SYSTEM_OPERATION        = 0x0400,
};

enum WINDOW_ACTION_MODIFIERS
{
    WAM_NONE                    = 0x0000,

    WAM_FRAME_BOUNDS            = 0x0001,
    WAM_ACTIVATE_FOREGROUND     = 0x0002,
    WAM_ACTIVATE_INPUT          = 0x0004,
    WAM_ACTIVATE_NO_ZORDER      = 0x0008,
    WAM_INSERT_AFTER_NO_OWNER   = 0x0010,
    WAM_RESTORE_TO_NORMAL       = 0x0020,
    WAM_RESTORE_TO_MAXIMIZED    = 0x0040,
    WAM_RESTORE_TO_ARRANGED     = 0x0080,
    WAM_WORK_AREA               = 0x0100,
    WAM_DPI                     = 0x0200,
    WAM_SCALED_TO_MONITOR       = 0x0400,
};

enum WINDOW_PLACEMENT_STATE
{
    WPS_NORMAL                  = 0,
    WPS_MAXIMIZED               = 1,
    WPS_MINIMIZED               = 2,
    WPS_ARRANGED                = 3,
};

struct WINDOW_ACTION
{
    WINDOW_ACTION_KINDS         kinds;
    WINDOW_ACTION_MODIFIERS     modifiers;

    BOOL                        visible;
    POINT                       position;
    SIZE                        size;
    HWND                        insertAfter;
    WINDOW_PLACEMENT_STATE      placementState;
    RECT                        normalRect;
    RECT                        workArea;
    UINT                        dpi;
    POINT                       pointOnMonitor;
    UINT                        monitorTopologyId;
};
```

## Members

`kinds`

Type: **WINDOW_ACTION_KINDS**

The kinds field indicates one or more changes to make to the window. If no
kinds values are set, the action is 'empty' (no changes).

| Kind                  | Meaning   |
|-----------------------|------------|
| WAK_VISIBILITY        | Shows or hides the window, depending on `visible` field. |
| WAK_POSITION          | Moves the window to the value in the `position` field, specified in screen coordinates. |
| WAK_SIZE              | Sizes the window to the value in the `size` field. By default this size is scaled to the window's current DPI.|
| WAK_INSERT_AFTER      | Moves the window in Z-Order, to be after (below) the window in the `insertAfter` field. |
| WAK_ACTIVATE          | Activates the window, like [SetActiveWindow](/windows/win32/api/winuser/nf-winuser-setactivewindow)|
| WAK_PLACEMENT_STATE   | Sets the state of the window, depending on the value in the `placementState` field. |
| WAK_NORMAL_RECT       | Sets the normal (or restore) position to the `normalRect` field. |
| WAK_MOVE_TO_MONITOR   | Moves the window to the provided monitor, specified by the `pointOnMonitor` field. |
| WAK_FIT_TO_MONITOR    | Ensures the window's normal position is within the bounds of the monitor's work area. |
| WAK_DISPLAY_CHANGE    | Indicates this action is in response to a display change. |
| WAK_SYSTEM_OPERATION  | Indicates this action is in response to a system operation, like a hotkey. |

`modifiers`

Type: **WINDOW_ACTION_MODIFIERS**

The modifiers field indicate non-default behavior when interpreting other
changes set in the action. Each modifier requires one or more kind flags.

| Modifier                  | Meaning   |
|---------------------------|------------|
| WAM_FRAME_BOUNDS          | The provided position and size do not include invisible resize borders. See `DWMWA_EXTENDED_FRAME_BOUNDS` ([DWMWINDOWATTRIBUTE](/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute)). |
| WAM_ACTIVATE_FOREGROUND   | The window being activated is in foreground. Activating the window will cause it to be the foreground window. |
| WAM_ACTIVATE_INPUT        | The activation is in response to input handling. |
| WAM_ACTIVATE_NO_ZORDER    | The activation should not raise the window to top, which is done by default. |
| WAM_INSERT_AFTER_NO_OWNER | The change to the window's Z-Order (insert after window) should not also move windows owned to this window, which is done by default. |
| WAM_RESTORE_TO_NORMAL     | Used if Minimizing the window (provided placement state is WPS_MINIMIZED). The window should restore to 'normal', not Maximized or Arranged. |
| WAM_RESTORE_TO_MAXIMIZED  | Used if Minimizing the window (provided placement state is WPS_MINIMIZED). The window should restore to Maximized, not Arranged or normal. |
| WAM_RESTORE_TO_ARRANGED   | Used if Minimizing the window (provided placement state is WPS_MINIMIZED). The window should restore to Arranged, not Maximized or normal. This requires the provided position and size are set to the arranged position. |
| WAM_WORK_AREA             | The work area indicates the provided position and size is from the past (for a different work area than the one the position is now on). This position is adjusted as needed to fit the current monitor. |
| WAM_DPI                   | The DPI scale for the provided size. By default, the size is assumed scaled to the window's current DPI. |
| WAM_SCALED_TO_MONITOR     | The `pointOnMonitor` field specifies a monitor, which is used to know the DPI scale factor of the provided position and size. The window will, after applying the action, be scaling to this monitor, even if the position and size are mostly on another monitor. |

`visible`

Used if `WAK_VISIBLE` to indicate if the window should be shown or hidden.
Changing the window's visibility sets or clears the `WS_VISIBLE` window style.

`position`

Used if `WAK_POSITION`. This is the new position (top/left) of the window, in
screen coordinates.

`size`

Used if `WAK_SIZE`. This is the new size of the window. By default, this is
expected to be scaled to the window's current DPI.

`insertAfter`

Used if `WAK_INSERT_AFTER`. This is the window the window being moved should be
after, or below, in Z-Order.

This value can be a valid top-level window or one
of many special values like `HWND_TOP` and `HWND_TOPMOST`. These are the same
values accepted by the APIs
[SetWindowPos](/windows/win32/api/winuser/nf-winuser-setwindowpos)
and
[DeferWindowPos](/windows/win32/api/winuser/nf-winuser-deferwindowpos)
as the `hWndInsertAfter` parameter.

`placementState`

Used if `WAK_PLACEMENT_STATE`. Setting the state of a window moves the window
between four exclusive states, where the window's position has special meaning.

 - Maximized windows generally fit their monitor's work area.
 - Minimized windows are off-screen (if the taskbar is enabled).
 - Arranged (or snapped) windows generally fit part of the monitor's work area
   (halfs, corners, columns, etc).
 - Normal (or restored) windows are not in one of the other special states.

While Maximized, Minimized, or Arranged, the window has a 'normal' position,
separate from its current position. The normal position is the last position
of the window that wasn't Maximized, Minimized, or Arranged. Restoring the
window from one of the three special states returns the window to the normal
position.

The API [ShowWindow](/windows/win32/api/winuser/nf-winuser-showwindow) allows
you to set all states other than Arranged. For example, `SW_MAXIMIZE`,
`SW_RESTORE`. Unlike the SW_ commands, setting the state in a `WINDOW_ACTION`
does not imply activation or visibility. To use
[ApplyWindowAction](nf-winuser-applywindowaction.md)
to do the equivalent of `SW_MAXIMIZE`, the action would also set `WAK_ACTIVATE`
and `WAK_VISIBILITY`, and set `visible` to true.

If the state is `WPS_ARRANGED`, the position and size fields must be set. While
not required, arranged positions generally will also set the `WAM_FRAME_BOUNDS`
flag as well, indicating the position is the visible bounds of the window, not
including invisible resize borders. (Arranged positions typically align the
window visibly with the monitor edges, without gaps for invisible resize area.)

`normalRect`

Used if `WAK_NORMAL_RECT`. This sets the normal (or restore) rect, and must be
used with `WAK_PLACEMENT_STATE`.

If setting `WPS_NORMAL`, the normal rect is equivalent to setting the position
and size.

If setting `WPS_MAXIMIZED`, `WPS_MINIMIZED`, or `WPS_ARRANGED`, the normal rect
is independent of the position and size of the window. This overrides the
default normal rect (the last non-Maximized/Minimized/Arranged position of the
window).

`workArea`

Used if `WAM_WORK_AREA`. This specifies the work area of the monitor that the
provided position and size were from. The window position is adjusted as needed
to fit the work area of the monitor that the window is moving to.

By default, the current or provided window position is assumed to be fit to the
monitor it is mostly on.

`dpi`

Used if `WAM_DPI`. This indicates the DPI value, base 96, that should be used to
scale the provided size. By default, the provided size is assumed scaled to the
window's current DPI,
[GetDpiForWindow](/windows/win32/api/winuser/nf-winuser-getdpiforwindow).

`pointOnMonitor`

Used if `WAK_MOVE_TO_MONITOR` or `WAM_SCALED_TO_MONITOR`.

If `WAK_MOVE_TO_MONITOR`, this point is used to pick the monitor to move the
window to.

If `WAM_SCALED_TO_MONITOR`, this point is used to pick the monitor that the
window is scaling to.

`monitorTopologyId`

Used if `WAK_DISPLAY_CHANGE`. The display change kind is used only by Intercept
windows (see
[ConvertToInterceptWindow](nf-winuser-converttointerceptwindow.md)
,
[WM_INTERCEPTED_WINDOW_ACTION](ns-winuser-wminterceptedwindowaction.md)
). Intercept windows receiving an action with the display change flag must set
this flag and topology ID when applying the action.

When moved in response to a display change, the system chooses the appropriate
action depending on the monitor topology. Intercept windows can query the
monitor topology as part of deciding how to handle the intercepted action, and
compare this topology ID with the API
[GetCurrentMonitorTopologyId](nf-winuser-getcurrentmonitortopologyid.md)
to know if the topology has changed since the intercepted display change action.

If an Intercept window finds that the monitor topology ID changes before it
processes the intercepted display change action, it can call
[ApplyWindowAction](nf-winuser-applywindowaction.md)
with `WAK_DISPLAY_CHANGE` and a `monitorTopologyId` of 0 to re-generate the
display change action for the current monitor topology.

## Remarks

The `WAK_DISPLAY_CHANGE` and `WAK_SYSTEM_OPERATION` flags are only used by
Intercept windows (ones that have called
[ConvertToInterceptWindow](nf-winuser-converttointerceptwindow.md)
). When an intercept window receives an action with either of these flags set,
applying the action will have additional (internal) behavior. Failing to apply
the action will cause the window to behave unexpectedly.

 - An Intercept window receives a `WAK_DISPLAY_CHANGE` action when it is moved
 in response to a display change. It must set this flag and the same
 `monitorTopologyID` when applying the action. This is used by the system to
 move the window appropriately when the monitor topology changes.

 - An Intercept window receives a `WAK_SYSTEM_OPERATION` when moved by the
 system, for example a hotkey like Windows+Left. After the window applies the
 action, the system may do additional work, like show the Snap Assist UI, which
 allows the user to snap other windows next to this one.

Some values or combinations of fields in the `WINDOW_ACTION` are not valid:

| Fields | Restrictions |
|-------------------------------|------------|
| Max/Min/Arrange Position      | If setting state to Arranged, the action must also set a position and size. If setting Maximized/Minimized, the action may specify the position and size, which sets the Max/Min position explicitly. Setting the Maximize/Minimize position cannot be used with `WAK_MOVE_TO_MONITOR`. |
| Frame Bounds                  | If `WAM_FRAME_BOUNDS` is set, the position and size fields must also be set. |
| Insert After                  | If `WAK_INSERT_AFTER`, the `insertAfter` field must be a valid window or a special value like `HWND_TOP`. |
| Normal Rect                   | If `WAK_NORMAL_RECT`, the `WAK_PLACEMENT_STATE` flag must also be set. If setting the state to WPS_NORMAL, setting the normal rect cannot be done while also setting the position or size (for normal windows, the position and normal position are the same). |
| Point on Monitor              | The `WAK_MOVE_TO_MONITOR` and `WAM_SCALED_TO_MONITOR` flags both use the `pointOnMonitor` field. These flags cannot be used together. `WAM_SCALED_TO_MONITOR` requires also setting the position and size, and it cannot be used if the action sets the state to Maximized/Minimized/Arranged. `WAM_SCALED_TO_MONITOR` also cannot be used with the `WAK_FIT_TO_MONITOR`, `WAM_WORK_AREA`, or `WAM_DPI` flags. |
| Work Area                     | If `WAM_WORK_AREA` is set, the `workArea` field must be a non-empty rect. |
| Dpi                           | If `WAM_DPI` is set, the `dpi` field must be greater or equal to 96 (100% DPI). |
| 'Restore To' State            | The `WAM_RESTORE_TO_NORMAL`, `WAM_RESTORE_TO_MAXIMIZED`, and `WAM_RESTORE_TO_ARRANGED` flags require that the placement state be set to `WPS_MINIMIZED`. Only one of the three 'restore to' flags can be set. If `WAM_RESTORE_TO_ARRANGED`, the position and size fields must be set, and are interpretted as the restore to arrange position (not the Minimize position). |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | User32.dll |
