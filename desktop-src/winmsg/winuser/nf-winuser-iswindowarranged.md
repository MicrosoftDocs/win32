---
UID: NF:winuser.IsWindowArranged
ms.topic: reference
tech.root: winmsg
title: IsWindowArranged
ms.date: 03/24/2023
targetos: Windows
description: Determines whether the specified window is arranged (that is, whether it's snapped).
prerelease: true
req.assembly: 
req.construct-type: function
req.ddi-compliance: 
req.dll: User32.dll
req.header: winuser.h
req.idl: 
req.include-header: 
req.irql: 
req.kmdf-ver: 
req.lib: User32.lib
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: Windows 10, version 1903
req.target-min-winversvr: 
req.target-type: 
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - DllExport
api_location:
 - User32.dll
api_name:
 - IsWindowArranged
f1_keywords:
 - IsWindowArranged
 - dstorage/IsWindowArranged
dev_langs:
 - c++
helpviewer_keywords:
 - IsWindowArranged
---

# IsWindowArranged function (winuser.h)

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

Determines whether the specified window is arranged (that is, whether it's snapped). You should treat snapped as a window state similar to maximized or minimized. Also see [Snap your windows](https://support.microsoft.com/windows/snap-your-windows-885a9b1e-a983-a3b1-16cd-c531795e6241).

## Syntax

```cpp
BOOL IsWindowArranged(
  [in] HWND hwnd
);
```

## Parameters

`hwnd`

Type: **HWND**

A handle to the window to be tested.

## Return value

Type: **BOOL**

A nonzero value if the window is arranged; otherwise, zero.

## Remarks

At this time, this function does not have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`User32.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

A snapped window (see [Snap your windows](https://support.microsoft.com/windows/snap-your-windows-885a9b1e-a983-a3b1-16cd-c531795e6241)) is considered to be arranged. You should treat arrange as a window state similar to maximize. Arranged, maximize, and minimize are mutually exclusive states. An arranged window can be restored to its original size and position. Restoring a window from minimize can make a window arranged if the window was arranged before it was minimized. When calling [GetWindowPlacement](/windows/win32/api/winuser/nf-winuser-getwindowplacement), keep in mind that the *showCmd* member on the returned [WINDOWPLACEMENT](/windows/win32/api/winuser/ns-winuser-windowplacement) can have a value of **SW_SHOWNORMAL** even if the window is arranged.

## Example

```cpp
// Check whether the window is in the restored state.
BOOL IsRestored(HWND hwnd)
{
  if (IsIconic(hwnd) || IsZoomed(hwnd) || IsWindowArranged(hwnd))
  {
    return false;
  }
  return true;
}
```

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, version 1903 |
| **Minimum supported server** | |
| **Target platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | User32.dll |
| **API set** | Not yet released. |

## See also

* [IsIconic](/windows/win32/api/winuser/nf-winuser-isiconic)
* [IsZoomed](/windows/win32/api/winuser/nf-winuser-iszoomed)
* [Windows](/windows/win32/winmsg/windows)
* [Snap your windows](https://support.microsoft.com/windows/snap-your-windows-885a9b1e-a983-a3b1-16cd-c531795e6241)
