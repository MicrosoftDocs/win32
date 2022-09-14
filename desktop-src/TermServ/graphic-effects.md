---
title: Graphic effects
description: A list of features that should be disabled when running as a remote session in a Remote Desktop Services environment.
ms.assetid: 229a1058-acba-4d4b-ba52-824dda4f91a5
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Graphic effects

A Remote Desktop Services server relies on the network to transmit all input and output to its client terminals. Consequently, applications that make excessive use of graphic effects can affect performance for all Remote Desktop Services clients by slowing down the network. In addition, the slower transmission speed over a network might cause these special effects to appear less pleasing than they would be in a local video environment.

In particular, applications should disable or minimize the use of the following features when running in a Remote Desktop Services environment as a remote session:

-   Splash screens—graphical product or company information displayed while an application is starting. Transmitting a splash screen to a Remote Desktop Connection (RDC) client consumes extra network bandwidth and forces the user to wait before accessing the application.
-   Animations, which consume both CPU time and network bandwidth.
-   Direct input or output to the screen. If you need to read bits from the screen, maintain a separate, off-screen copy of the video buffer. Similarly, if you need to do elaborate screen output—for example, overlaying several images to arrive at a final composite screen—do that work in an off-screen buffer, and then send the results to the actual video buffer.

For more information about detecting remote sessions, see [Detecting the Remote Desktop Services Environment](detecting-the-terminal-services-environment.md).

Use the Microsoft Foundation Class library, or MFC, whenever possible. The MFC has a long list of tried-and-true classes for performing a wide variety of tasks. Most of these classes work well in a Remote Desktop Services environment—usually much better than re-engineered solutions. A good example is the class that provides context-sensitive help text—help text that appears on-screen when the mouse pointer hovers over a button or menu item. If an application uses the MFC implementation to provide this feature, it will work reasonably well on the desktop system. But if the application implements this feature by using dialog boxes or an alternate approach, the final result might not function as well in a Remote Desktop Services environment.

 

 




