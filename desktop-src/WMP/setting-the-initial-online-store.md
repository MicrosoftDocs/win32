---
title: Setting the Initial Online Store
description: Setting the Initial Online Store
ms.assetid: 86d98936-8f20-4395-be5f-37800162aa89
keywords:
- Windows Media Player online stores,setting initial online stores
- online stores,setting initial online stores
- type 1 online stores,setting initial online stores
- type 2 online stores,setting initial online stores
- Windows Media Player online stores,first online store viewed
- online stores,first online store viewed
- type 1 online stores,first online store viewed
- type 2 online stores,first online store viewed
- first online store viewed
- setting initial online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting the Initial Online Store

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

For details about redistributing Windows Media Player software with your application, see [Redistributing Windows Media Player Software](redistributing-windows-media-player-software.md).

When a user first installs Windows Media Player, the setup application sets the initial active online store to a default chosen by Microsoft. Personal computer original equipment manufacturers (OEMs) can choose to change this setting.

To specify and configure the first online store that the user sees when he or she installs Windows Media Player, you must:

-   Create a ServiceInfo document that you install on the user's hard disk. This document contains the information about how to configure the initial active online store.
-   Append a set of command-line parameters when running the setup application.

There are three scenarios for installing Windows Media Player and setting the initial online store. The following sections provide more details about each scenario:

-   [Installing While Offline](installing-while-offline.md)
-   [Installing from a CD While Online](installing-from-a-cd-while-online.md)
-   [Installing from the Web While Online](installing-from-the-web-while-online.md)

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> <dt>

[**Setup Command-line Parameters for Online Stores**](setup-command-line-parameters-for-online-stores.md)
</dt> </dl>

 

 




