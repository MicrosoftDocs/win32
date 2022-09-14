---
title: Ripping a CD
description: Ripping a CD
ms.assetid: f5c1b5bf-d616-48cb-8690-e0237c56e402
keywords:
- Windows Media Player,CD ripping
- Windows Media Player object model,CD ripping
- object model,CD ripping
- Windows Media Player ActiveX control,CD ripping
- ActiveX control,CD ripping
- Windows Media Player Mobile ActiveX control,CD ripping
- Windows Media Player Mobile,CD ripping
- CD ripping,about
- ripping CDs,about
ms.topic: article
ms.date: 05/31/2018
---

# Ripping a CD

There are two ways to rip a CD by using the Windows Media Player control. Windows Media Player 9 can rip CDs by using **IWMPPlayerServices::setTaskPane**. Windows Media Player 11 introduces the **IWMPCdromRip** interface for ripping CDs. This interface provides more functionality than **IWMPPlayerServices::setTaskPane**, and it is recommended that you use **IWMPCdromRip** if it is available.

The following sections describe how to rip a CD by using Windows Media Player.

-   [Ripping by Using the IWMPCdromRip Interface](ripping-by-using-the-iwmpcdromrip-interface.md)
-   [Ripping by Using IWMPPlayerServices::setTaskPane](ripping-by-using-iwmpplayerservices--settaskpane.md)

## Related topics

<dl> <dt>

[**Player Control Guide**](player-control-guide.md)
</dt> </dl>

 

 




