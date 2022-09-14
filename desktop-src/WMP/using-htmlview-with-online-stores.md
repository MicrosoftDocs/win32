---
title: Using HTMLView with Online Stores
description: Using HTMLView with Online Stores
ms.assetid: 78de7ef3-400c-4411-8ade-35c421805df8
keywords:
- Windows Media Player online stores,HTMLView
- online stores,HTMLView
- type 1 online stores,HTMLView
- type 2 online stores,HTMLView
- HTMLView,online stores
ms.topic: article
ms.date: 05/31/2018
---

# Using HTMLView with Online Stores

Windows Media Player prompts users for permission to display HTMLView content in **Now Playing**. Online stores can disable this prompt by specifying a base URL value in the **HTMLView** element of the ServiceInfo document. When Windows Media Player opens a playlist that specifies HTMLView content to display, the Player compares the base URL from the ServiceInfo document of the current active online store to the base URL of the HTMLView content. If they match, Windows Media Player displays the HTMLView content without prompting the user.

## Related topics

<dl> <dt>

[**Displaying Web Pages in Windows Media Player**](displaying-web-pages-in-windows-media-player.md)
</dt> <dt>

[**HTMLView Element**](htmlview-element.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> </dl>

 

 




