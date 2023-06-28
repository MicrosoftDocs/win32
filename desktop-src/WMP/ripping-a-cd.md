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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Ripping a CD

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

There are two ways to rip a CD by using the Windows Media Player control. Windows Media Player 9 can rip CDs by using **IWMPPlayerServices::setTaskPane**. Windows Media Player 11 introduces the **IWMPCdromRip** interface for ripping CDs. This interface provides more functionality than **IWMPPlayerServices::setTaskPane**, and it is recommended that you use **IWMPCdromRip** if it is available.

The following sections describe how to rip a CD by using Windows Media Player.

-   [Ripping by Using the IWMPCdromRip Interface](ripping-by-using-the-iwmpcdromrip-interface.md)
-   [Ripping by Using IWMPPlayerServices::setTaskPane](ripping-by-using-iwmpplayerservices--settaskpane.md)

## Related topics

<dl> <dt>

[**Player Control Guide**](player-control-guide.md)
</dt> </dl>

 

 




