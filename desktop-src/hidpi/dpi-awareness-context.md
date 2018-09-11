---
title: DPI_AWARENESS_CONTEXT handle
description: Identifies the awareness context for a window.
ms.assetid: BFD54A9F-642B-4A3A-BBB9-F3A80779251D
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DPI\_AWARENESS\_CONTEXT handle

Identifies the awareness context for a window.

## Syntax

``` syntax
#define DPI_AWARENESS_CONTEXT_UNAWARE              ((DPI_AWARENESS_CONTEXT)-1)
#define DPI_AWARENESS_CONTEXT_SYSTEM_AWARE         ((DPI_AWARENESS_CONTEXT)-2)
#define DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE    ((DPI_AWARENESS_CONTEXT)-3)
#define DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 ((DPI_AWARENESS_CONTEXT)-4)
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

 

 




