---
description: Handling Disc Ejections
ms.assetid: c43dd795-749b-4ca7-8510-71d62e0076b3
title: Handling Disc Ejections
ms.topic: article
ms.date: 05/31/2018
---

# Handling Disc Ejections

When the user ejects a DVD from the drive, the DVD Navigator sends your application an EC\_DVD\_DISC\_EJECTED message. The application can safely ignore this message and let the DVD Navigator manage the graph's state. An application can also handle the EC\_DVD\_DISC\_EJECTED method to implement custom behavior when a disc is ejected. If you handle the message, you must set the DVD\_ResetOnStop flag to **TRUE** with the [**SetOption**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-setoption) method and then call [**IMediaControl::Stop**](/windows/desktop/api/Control/nf-control-imediacontrol-stop) before closing the application or playing another disc.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



