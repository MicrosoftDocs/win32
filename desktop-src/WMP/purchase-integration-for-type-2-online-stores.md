---
title: Purchase Integration for Type 2 Online Stores
description: Purchase Integration for Type 2 Online Stores
ms.assetid: aedaa6a0-d559-44b7-9c14-2abf44478b1c
keywords:
- Windows Media Player online stores,purchase integration
- online stores,purchase integration
- type 2 online stores,purchase integration
- Windows Media Player online stores,integrating purchases
- online stores,integrating purchases
- type 2 online stores,integrating purchases
- Windows Media Player,purchase integration
- Windows Media Player,integrating purchases
- purchase integration
- integrating purchases
ms.topic: article
ms.date: 05/31/2018
---

# Purchase Integration for Type 2 Online Stores

When Windows Media Player plays digital media content or the user chooses **Find Album Info**, the Player offers the user a link to buy the CD or DVD from which the content originated if such a link is available. When the user clicks the link, Windows Media Player 10 or later calls on the current music store to handle the purchase request. When this happens, the Player navigates to the first service task pane (in Windows Media Player 10) or the Online Stores tab (in Windows Media Player 11) and displays the webpage specified by the **MediaPlayerURL** attribute of the **BuyCD** element of the ServiceInfo document. (The **MediaCenterURL** and **BrowserURL** attributes are used in a similar manner to handle calls from Windows XP Media Center Edition 2004 and Windows XP Service Pack 2).

Windows Media Player appends a query string to the URL to provide information to the online store about the content the user chose to purchase. The query string includes attributes like **Title**, **Album**, and **Artist**, which the online store can use to determine the correct album to sell. The reference documentation for the **BuyCD** element provides the complete list of query string attributes and their descriptions.

## Guidelines for the BuyCD Page

When creating your BuyCD webpage, use the following guidelines:

-   The page must clearly identify the online store providing the information. You can do this by prominently displaying your logo, for example.
-   The page must include a link to your company's privacy statement.
-   It is best to provide initial purchasing information without requiring the user to install programs or log in to your online store.

## Related topics

<dl> <dt>

[**About Type 2 Online Stores**](about-type-2-online-stores.md)
</dt> <dt>

[**BuyCD Element**](buycd-element.md)
</dt> </dl>

 

 




