---
title: ServiceInfo Document for a Type 1 Online Store
description: ServiceInfo Document for a Type 1 Online Store
ms.assetid: '9ca424a1-c29a-4078-8d56-9d0fea52f150'
keywords:
- Windows Media Player online stores,ServiceInfo document
- online stores,ServiceInfo document
- type 1 online stores,ServiceInfo document
- ServiceInfo document
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ServiceInfo Document for a Type 1 Online Store

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Type 1 online stores must provide Microsoft with the URL of an XML document that describes the online store. Windows Media Player 11 uses this document to determine how to configure the user interface to host the online store.

The ServiceInfo document for a type 1 store provides the following information to Windows Media Player:

-   Information used to configure the **Online Stores** button (also called a tab), such as the button text, the button color, and the tooltip for the button.
-   URLs for images that Windows Media Player displays to identify the online store.
-   URLs of webpages, provided by the online store, that Windows Media Player hosts in its user interface.
-   URL where Windows Media Player can retrieve the online store's plug-in so that the plug-in can be installed on the user's computer.

When Windows Media Player retrieves the ServiceInfo document from the Web, it appends a query string to the URL. The query string contains parameters that provide information about the user's locale and geographic location and the version of Windows Media Player.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> <dt>

[**Creating the ServiceInfo Document Dynamically**](creating-the-serviceinfo-document-dynamically.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 




