---
description: VMR Modes of Operation
ms.assetid: 98244af1-5934-4d1c-b9c3-7a414b065fe7
title: VMR Modes of Operation
ms.topic: article
ms.date: 05/31/2018
---

# VMR Modes of Operation

The component architecture of the VMR enables applications to configure it in various ways, depending on how rendering is to be performed. The following table shows the three presentation modes and the two mixing modes, and the components that are present for each configuration.



| Mode       | Single Stream                                                                     | Multiple Streams (Mixing Mode)                                                                                             |
|------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Windowed   | Allocator-presenterCore Synchronization Unit<br/> Window Manager<br/> | MixerCompositor\*<br/> Allocator-presenter<br/> Core Synchronization Unit<br/> Window Manager<br/> |
| Windowless | Allocator-presenterCore Synchronization Unit<br/>                           | MixerCompositor\*<br/> Allocator-presenter<br/> Core Synchronization Unit<br/>                           |
| Renderless | Allocator-presenter (provided by application)Core Synchronization Unit<br/> | MixerCompositor\*<br/> Allocator-presenter (provided by application)<br/> Core Synchronization Unit<br/> |



 

\* Indicates that the application has the option to provide a custom component or use the default component.

In all configurations, the main point to remember when you create filter graphs with the VMR is that you must configure the VMR before you connect it.

For all configurations, pins cannot be dynamically added or removed after the VMR is connected to the upstream filter, but they can be connected and disconnected. If the application is unsure how many pins will be needed, it should configure the VMR for the maximum number that might be needed. The presence of unused input pins on the filter does not degrade rendering performance. Unlike the old Overlay Mixer, the VMR has no output pin because it does not require a separate filter for window management.

The following sections describe how to configure the VMR for a given mode:

-   [VMR Windowed (Compatibility) Mode](vmr-windowed--compatibility--mode.md)
-   [VMR Windowless Mode](vmr-windowless-mode.md)
-   [VMR with Multiple Streams (Mixing Mode)](vmr-with-multiple-streams--mixing-mode.md)
-   [YUV Mixing Mode](yuv-mixing-mode.md)
-   [Positioning and Moving Video Rectangles in Composition Space](positioning-and-moving-video-rectangles-in-composition-space.md)
-   [VMR Renderless Playback Mode (Custom Allocator-Presenters)](vmr-renderless-playback-mode--custom-allocator-presenters.md)
-   [DirectDraw Exclusive Mode](directdraw-exclusive-mode.md)

 

 




