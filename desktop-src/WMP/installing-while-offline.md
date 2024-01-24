---
title: Installing While Offline
description: Installing While Offline
ms.assetid: 29d80b6b-161d-44a7-b91e-70766b849c55
keywords:
- Windows Media Player online stores,installing while offline
- online stores,installing while offline
- type 1 online stores,installing while offline
- type 2 online stores,installing while offline
- Windows Media Player online stores,offline installs
- online stores,offline installs
- type 1 online stores,offline installs
- type 2 online stores,offline installs
- installing online stores while offline
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Installing While Offline

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Users can install Windows Media Player while not connected to the Internet. When this happens, Windows Media Player setup locates the ServiceInfo.xml document specified by the *ServiceInfo* command line parameter. If the **Key** attribute matches the *DefaultService* command line parameter, setup applies information from the following elements to Windows Media Player:

-   FriendlyName. The friendly name of the online store is shown in the Windows Media Player user interface.
-   Color. The specified colors are applied to the taskbar and buttons.
-   ServiceTask1, ServiceTask2, and ServiceTask3. The ButtonText and ButtonTip child elements are set. The URL attribute is not set. URL is set once the user connects to the Internet and Windows Media Player retrieves its list of online stores in the normal fashion.
-   Image. The MenuURL and ServiceLargeURL attributes are set. These URLs must point to images you installed on the user's hard disk by using the file:// protocol.

When the user attempts to view the online store, Windows Media Player displays a message informing the user that an Internet connection is required.

## Related topics

<dl> <dt>

[**Color Element**](color-element.md)
</dt> <dt>

[**FriendlyName Element**](friendlyname-element.md)
</dt> <dt>

[**Image Element**](image-element.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**ServiceInfo Element**](serviceinfo-element.md)
</dt> <dt>

[**ServiceTask1 Element**](servicetask1-element.md)
</dt> <dt>

[**ServiceTask2 Element**](servicetask2-element.md)
</dt> <dt>

[**ServiceTask3 Element**](servicetask3-element.md)
</dt> <dt>

[**Setting the Initial Online Store**](setting-the-initial-online-store.md)
</dt> <dt>

[**Setup Command-line Parameters for Online Stores**](setup-command-line-parameters-for-online-stores.md)
</dt> </dl>

 

 




