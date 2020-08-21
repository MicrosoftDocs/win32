---
title: High contrast parameter
description: The high contrast parameter indicates whether the user wants a high contrast between the colors used for foreground and background visuals.
ms.assetid: ec89c4ce-4e8b-4e1f-a349-fbd47431d675
ms.topic: article
ms.date: 05/31/2018
---

# High contrast parameter

The high contrast parameter indicates whether the user wants a high contrast between the colors used for foreground and background visuals.

The user controls the setting of the high contrast parameter by using the Ease of Access Center in Control Panel, or another application for customizing the environment. Applications use the **SPI\_GETHIGHCONTRAST** and **SPI\_SETHIGHCONTRAST** flags with the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function to get and set the high contrast parameter.

During initialization and when processing [**WM\_SYSCOLORCHANGE**](/windows/desktop/gdi/wm-syscolorchange) messages, applications should determine the state of the high contrast parameter. To make this determination, applications should call [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) with the **SPI\_GETHIGHCONTRAST** flag to obtain a [**HIGHCONTRAST**](/windows/win32/api/winuser/ns-winuser-highcontrasta) structure. If the **dwFlags** member of the **HIGHCONTRAST** structure has the **HCF\_HIGHCONTRASTON** bit set, then the high contrast feature is enabled, and applications should do the following:

-   Map all colors to a single pair of foreground and background colors. Use the [**GetSysColor**](/windows/desktop/api/winuser/nf-winuser-getsyscolor) function to determine the appropriate foreground and background colors, using either a combination of **COLOR\_WINDOWTEXT** and **COLOR\_WINDOW** or a combination of **COLOR\_BTNTEXT** and **COLOR\_BTNFACE**. The **GetSysColor** function returns the colors selected by the user through the Control Panel.
-   Omit any bitmapped images that would typically be displayed behind text. Such images are visually distracting to a user who needs high contrast.
-   Images that would typically be drawn in multiple colors should be drawn using the foreground and background colors selected for text.

Also, applications use the **SPI\_GETDISABLEOVERLAPPEDCONTENT** and **SPI\_SETDISABLEOVERLAPPEDCONTENT** flags with the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function to get and set overlapped content parameter. Display features such as background images, textured backgrounds, water marks on documents, alpha blending, and transparency can reduce the contrast between the foreground and background, making it harder for users with low vision to see objects on the screen. This flag enables applications to determine whether such overlapped content has been disabled

 

 