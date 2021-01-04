---
title: DPI_AWARENESS_CONTEXT handle (windef.h)
description: Identifies the awareness context for a window.
ms.assetid: BFD54A9F-642B-4A3A-BBB9-F3A80779251D
ms.topic: article
ms.date: 10/04/2018
---

# DPI\_AWARENESS\_CONTEXT handle

Identifies the awareness context for a window.

## Syntax

``` syntax
#define DPI_AWARENESS_CONTEXT_UNAWARE              ((DPI_AWARENESS_CONTEXT)-1)
#define DPI_AWARENESS_CONTEXT_SYSTEM_AWARE         ((DPI_AWARENESS_CONTEXT)-2)
#define DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE    ((DPI_AWARENESS_CONTEXT)-3)
#define DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 ((DPI_AWARENESS_CONTEXT)-4)
#define DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED    ((DPI_AWARENESS_CONTEXT)-5)
```

## Constants

**DPI\_AWARENESS\_CONTEXT\_UNAWARE**<dl> DPI unaware. This window does not scale for DPI changes and is always assumed to have a scale factor of 100% (96 DPI). It will be automatically scaled by the system on any other DPI setting.  
</dl>

**DPI\_AWARENESS\_CONTEXT\_SYSTEM\_AWARE**<dl> System DPI aware. This window does not scale for DPI changes. It will query for the DPI once and use that value for the lifetime of the process. If the DPI changes, the process will not adjust to the new DPI value. It will be automatically scaled up or down by the system when the DPI changes from the system value.  
</dl>

**DPI\_AWARENESS\_CONTEXT\_PER\_MONITOR\_AWARE**<dl> Per monitor DPI aware. This window checks for the DPI when it is created and adjusts the scale factor whenever the DPI changes. These processes are not automatically scaled by the system.  
</dl>

**DPI\_AWARENESS\_CONTEXT\_PER\_MONITOR\_AWARE\_V2**<dl> Also known as **Per Monitor v2**. An advancement over the original per-monitor DPI awareness mode, which enables applications to access new DPI-related scaling behaviors on a per top-level window basis.  
Per Monitor v2 was made available in the Creators Update of Windows 10, and is not available on earlier versions of the operating system.  
The additional behaviors introduced are as follows:

-   **Child window DPI change notifications** - In Per Monitor v2 contexts, the entire window tree is notified of any DPI changes that occur.
-   **Scaling of non-client area** - All windows will automatically have their non-client area drawn in a DPI sensitive fashion. Calls to [**EnableNonClientDpiScaling**](/windows/desktop/api/Winuser/nf-winuser-enablenonclientdpiscaling) are unnecessary.
-   **Scaling of Win32 menus** - All NTUSER menus created in Per Monitor v2 contexts will be scaling in a per-monitor fashion.
-   **Dialog Scaling** - Win32 dialogs created in Per Monitor v2 contexts will automatically respond to DPI changes.
-   **Improved scaling of comctl32 controls** - Various comctl32 controls have improved DPI scaling behavior in Per Monitor v2 contexts.
-   **Improved theming behavior** - UxTheme handles opened in the context of a Per Monitor v2 window will operate in terms of the DPI associated with that window.

  
</dl>

**DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED**

DPI unaware with improved quality of GDI-based content. This mode behaves similarly to DPI_AWARENESS_CONTEXT_UNAWARE, but also enables the system to automatically improve the rendering quality of text and other GDI-based primitives when the window is displayed on a high-DPI monitor.

For more details, see [Improving the high-DPI experience in GDI-based Desktop apps](https://blogs.windows.com/buildingapps/2017/05/19/improving-high-dpi-experience-gdi-based-desktop-apps/#Uwv9gY1SvpbgQ4dK.97).

DPI_AWARENESS_CONTEXT_UNAWARE_GDISCALED was introduced in the October 2018 update of Windows 10 (also known as version 1809).


## Requirements

| Requirement | Value |
|----|-----------|
| Minimum supported client<br/> | Windows 10, version 1607 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | None supported <br/>  |
| Header<br/>                   | <dl> <dt>windef.h</dt> </dl> |

## See also

<dl> <dt>

[**AreDpiAwarenessContextsEqual**](/windows/desktop/api/winuser/nf-winuser-aredpiawarenesscontextsequal)
</dt> <dt>

[**GetAwarenessFromDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-getawarenessfromdpiawarenesscontext)
</dt> </dl>

[**GetDpiFromDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-getdpifromdpiawarenesscontext)
</dt> </dl>

[**GetThreadDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-getthreaddpiawarenesscontext)
</dt> </dl>

[**GetWindowDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-getwindowdpiawarenesscontext)
</dt> </dl>

[**IsValidDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-isvaliddpiawarenesscontext)
</dt> </dl>

[**SetProcessDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiawarenesscontext)
</dt> </dl>

[**SetThreadDpiAwarenessContext**](/windows/desktop/api/winuser/nf-winuser-setthreaddpiawarenesscontext)
