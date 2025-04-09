---
UID: NF:winuser.EnterMoveSizeLoop
description: Begin dragging or sizing a window in response to input.
tech.root: winmsg
title: EnterMoveSizeLoop function
ms.topic: reference
ms.date: 3/22/2025
req.lib: 
req.dll: User32.dll
api_type:
 - DllExport
api_location:
 - user32.dll
api_name:
 - EnterMoveSizeLoop
f1_keywords:
 - EnterMoveSizeLoop
 - winuser/EnterMoveSizeLoop
dev_langs:
 - c++
helpviewer_keywords:
 - EnterMoveSizeLoop
targetos: Windows
ms.localizationpriority: low
---

# EnterMoveSizeLoop function

EnterMoveSizeLoop allows an app to begin dragging or sizing a window in
response to input.

## Syntax

```cpp
enum MOVESIZE_OPERATION
{
    MSO_SIZE_LEFT =             1,
    MSO_SIZE_RIGHT =            2,
    MSO_SIZE_TOP =              3,
    MSO_SIZE_TOPLEFT =          4,
    MSO_SIZE_TOPRIGHT =         5,
    MSO_SIZE_BOTTOM =           6,
    MSO_SIZE_BOTTOMLEFT =       7,
    MSO_SIZE_BOTTOMRIGHT =      8,
    MSO_MOVE =                  9,
};

BOOL EnterMoveSizeLoop(
    HWND hwnd,
    POINT ptCursor,
    MOVESIZE_OPERATION moveSizeCode);
```

## Parameters

`hwnd`

The window that will be moved or sized in response to input. It must
be a top level window owned by the current process.

`ptCursor`

The cursor position, in screen coordinates. This is the position of the down
input event that caused this API to be caused. Each round of the MoveSize loop
(moving/sizing the window to keep up with the cursor) drags from this original
point.

`moveSizeCode`

Indicates if the operation is a move (`MSO_MOVE`), or a size. When moving, the
window is moved on each mouse move to stay the same position relative to the
mouse cursor. When sizing, one or two sides of the window are moved to keep up
with the cursor, depending on the size code (`MSO_SIZE_TOP`,
`MSO_SIZE_TOPLEFT`, etc).

## Return value

Type: **BOOL**

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error
information, call GetLastError.

## Remarks

> [!TIP]
> At this time, this function does not have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`User32.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

`EnterMoveSizeLoop` causes the window to enter the MoveSize loop, moving or
sizing the window in response to mouse, touch, or pen input. Applications
typically enter the loop while processing input over the title bar or resize
borders, using default processing
([DefWindowProc](/windows/desktop/api/winuser/nf-winuser-defwindowproca)) for
messages like
[WM_NCLBUTTONDOWN](../../inputdev/wm-nclbuttondown.md).

The caller provides a point, indicating the location of the down event. This is
where the user clicked (or pressed). While in the MoveSize loop, each time the
mouse moves, the new cursor position is used to adjust the window position,
depending on the provided size code (MSO_MOVE, MSO_SIZE_LEFT, etc).

`EnterMoveSizeLoop` should be called in response to a mouse or pointer down
input message.

If the window belongs to another thread, the call returns immediately. Input
capture is redirected to the thread the window is on. If the window belongs to
the calling thread, the call returns only after the mouse or pointer contact is
released (at the end of the drag operation).

This API does not support Keyboard MoveSize (alt-space, move/size).

## Requirements

The window must be a top-level window owned by the current process.

The window must have the same DPI Awareness as the calling thread.


| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | User32.dll |
