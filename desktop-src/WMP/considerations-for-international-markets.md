---
title: Considerations for International Markets
description: Considerations for International Markets
ms.assetid: 890a280d-a4e0-4349-960d-ca8ac1872ee6
keywords:
- Windows Media Player online stores,international markets
- online stores,international markets
- type 1 online stores,international markets
- type 2 online stores,international markets
- international markets
- Windows Media Player online stores,ServiceInfo document
- online stores,ServiceInfo document
- type 1 online stores,ServiceInfo document
- type 2 online stores,ServiceInfo document
- ServiceInfo document
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Considerations for International Markets

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If your company creates online stores for multiple markets, you must provide Microsoft with the URL of a ServiceInfo document for each market. You can do this one of the following two ways:

-   Create a separate ServiceInfo document for each market. In this case, you provide Microsoft with URLs that point to individual ServiceInfo documents for each online store in each market.
-   Create a single ServiceInfo document for all markets. When you do this, you provide Microsoft with the same URL for each market. Your ServiceInfo document, created as an ASP page, can then dynamically detect the user's location based on query string parameters.

Windows Media Player appends a query string to the ServiceInfo URL request that provides information about the user's locale and location settings. If your online store uses this information to determine which content to display, you should dynamically append these values to your own URLs in your ServiceInfo document. This is the best way to ensure that your webpage URLs will always contain the parameters you expect.

Once you have determined the user's location and language preference, you may want to persist this information for future sessions. You can do this using any of the techniques you would normally use in a webpage, such as cookies, or by using your COM object.

## Related topics

<dl> <dt>

[**Creating the ServiceInfo Document Dynamically**](creating-the-serviceinfo-document-dynamically.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**ServiceInfo Element**](serviceinfo-element.md)
</dt> </dl>

 

 




