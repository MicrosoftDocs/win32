---
title: Album Info Integration
description: Album Info Integration
ms.assetid: c59c0c1b-eddc-4061-87cc-a5c44ae0c15d
keywords:
- Windows Media Player online stores,album info integration
- online stores,album info integration
- type 2 online stores,album info integration
- Windows Media Player online stores,integrating album info
- online stores,integrating album info
- type 2 online stores,integrating album info
- Windows Media Player,integrating album info
- Windows Media Player,album info integration
- album info integration
- integrating album info
ms.topic: article
ms.date: 05/31/2018
---

# Album Info Integration

Windows Media Player enables users to request detailed information about the CD or DVD from which digital media content originated by clicking a button, such as **More Info**. When the user clicks the button, Windows Media Player 10 or later calls on the current music store to display the album details. When this happens, the Player opens the album information pane and displays the webpage specified by the **URL** attribute of the **AlbumInfo** element of the ServiceInfo document.

Windows Media Player appends a query string to the URL to provide information to the online store about the content the user requested. The query string includes attributes like **Title**, **Album**, and **Artist**, which the online store can use to determine the correct album to display. The reference documentation for the **AlbumInfo** element provides the complete list of query string attributes and their descriptions.

## Guidelines for Album Info

When creating your album information webpage, use the following guidelines:

-   The page must clearly identify the online store providing the information. You can do this by prominently displaying your logo, for example.
-   The page must include a link to your company's privacy statement.
-   Avoid page navigation within the album information feature whenever possible. You should navigate to your online store for most activities.
-   We recommend that you provide valuable information without requiring the user to install programs or log in to your online store.

## Related topics

<dl> <dt>

[**About Type 2 Online Stores**](about-type-2-online-stores.md)
</dt> <dt>

[**AlbumInfo Element**](albuminfo-element.md)
</dt> </dl>

 

 




