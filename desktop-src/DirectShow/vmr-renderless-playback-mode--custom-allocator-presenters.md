---
description: VMR Renderless Playback Mode (Custom Allocator-Presenters)
ms.assetid: 0381f862-2f16-4b4d-be48-40f7fe151585
title: VMR Renderless Playback Mode (Custom Allocator-Presenters)
ms.topic: article
ms.date: 05/31/2018
---

# VMR Renderless Playback Mode (Custom Allocator-Presenters)

In renderless playback mode, the VMR does not perform the rendering. Instead, it uses a custom allocator-presenter supplied by the application. This mode is useful for games and other types of applications that have sophisticated video effects. Renderless playback mode enables the applications to create and control its own DirectDraw surface (VMR-7) or Direct3D surface (VMR-9), and to access the video bits at presentation time.

In renderless mode, the VMR-9 does not automatically load its mixer component.

In renderless playback mode, the application does the following tasks:

-   Manages the playback window.
-   Allocates the DirectDraw or Direct3D object and the final frame buffer.
-   Notifies the rest of the playback system of the object being used.
-   Presents the frame buffer at the correct time.
-   Handles all resolution-mode changes, monitor changes, and surface losses. It must advise the rest of the playback system of these events.

The VMR does the following:

-   Handles all timing related to presenting the video frame.
-   Provides quality-control information to the application and the rest of the playback system.
-   Presents a consistent interface to the upstream components of the playback system, which are not aware that the application is providing the frame buffer allocation and performing the rendering.
-   Provides any mixing of video streams that may be required prior to rendering.

Because deinterlacing is performed by the mixer, the allocator-presenter always received deinterlaced frames. For more information, see [Setting Deinterlace Preferences](setting-deinterlace-preferences.md).

For more information about providing a custom allocator-presenter, see the following topics:

-   [Supplying a Custom Allocator-Presenter for VMR-7](supplying-a-custom-allocator-presenter-for-vmr-7.md)
-   [Supplying a Custom Allocator-Presenter for VMR-9](supplying-a-custom-allocator-presenter-for-vmr-9.md)
-   [Synchronizing the VMR to the Monitor's Refresh Rate](synchronizing-the-vmr-to-the-monitors-refresh-rate.md)

 

 



