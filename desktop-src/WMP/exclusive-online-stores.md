---
title: Exclusive Online Stores
description: Exclusive Online Stores
ms.assetid: f2b7f9a7-2299-48f4-b915-2c1a5e0d68bb
keywords:
- Windows Media Player online stores,exclusive
- online stores,exclusive
- type 1 online stores,exclusive
- type 2 online stores,exclusive
- exclusive online stores
ms.topic: article
ms.date: 05/31/2018
---

# Exclusive Online Stores

With Windows Media Player 11, an application that embeds the Player control remotely can specify an exclusive online store. In that case, the service selector in Windows Media Player is disabled, and only the specified online store is available to the user. Also, Windows Media Player adopts the color specified by the **Color** element of the exclusive online store's ServiceInfo document.

To specify an exclusive online store, an application must append ExclusiveService:*keyname* to the end of the string that it returns from [IWMPRemoteMediaServices::GetServiceType](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpremotemediaservices-getservicetype). For example, suppose Proseware is the key name given to a particular online store. If **GetServiceType** returns the string "Remote ExclusiveService:Proseware", then Proseware will be the only online store available in the remotely embedded Player control.

An application can limit Windows Media Player to an exclusive online store only if Windows Media Player is not already running when the application is launched. It is the application's responsibility to inform the user that he or she must close Windows Media Player before running the application.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> </dl>

 

 




