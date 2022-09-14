---
description: Before painting, the system must prepare the display device for drawing operations.
ms.assetid: a3802aa7-deec-4151-b1b1-4cd38f769864
title: Display Devices
ms.topic: article
ms.date: 05/31/2018
---

# Display Devices

Before painting, the system must prepare the display device for drawing operations. A display device context defines a set of graphic objects and their associated attributes, and the graphic modes that affect output. The system prepares each display device context for output to a window, setting the drawing objects, colors, and modes for the window instead of the display device. When the application supplies the display device context through calls to GDI functions, GDI uses the information in the context to generate output in the specified window without intruding on other windows or other parts of the screen.

The system provides five kinds of display device contexts.



| Type                                           | Meaning                                                                                                                                                          |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [common](common-display-device-contexts.md)   | Permits drawing in the client area of a specified window.                                                                                                        |
| [class](class-display-device-contexts.md)     | Permits drawing in the client area of a specified window.                                                                                                        |
| [parent](parent-display-device-contexts.md)   | Permits drawing anywhere in the window. Although the parent device context also permits drawing in the parent window, it is not intended to be used in this way. |
| [private](private-display-device-contexts.md) | Permits drawing in the client area of a specified window.                                                                                                        |
| [window](window-display-device-contexts.md)   | Permits drawing anywhere in the window.                                                                                                                          |



 

The system supplies a common, class, parent, or private device context to a window based on the type of display device context specified in that window's class style. The system supplies a window device context only when the application explicitly requests one for example, by calling the [**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc) or [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) function. In all cases, an application can use the [**WindowFromDC**](/windows/desktop/api/Winuser/nf-winuser-windowfromdc) function to determine which window a display DC currently represents.

This section provides information on the following topics.

-   [Display Device Context Cache](display-device-context-cache.md)
-   [Display Device Context Defaults](display-device-context-defaults.md)
-   [Common Display Device Contexts](common-display-device-contexts.md)
-   [Private Display Device Contexts](private-display-device-contexts.md)
-   [Parent Display Device Contexts](parent-display-device-contexts.md)
-   [Class Display Device Contexts](class-display-device-contexts.md)
-   [Window Display Device Contexts](window-display-device-contexts.md)
-   [Parent Display Device Contexts](parent-display-device-contexts.md)

 

 



