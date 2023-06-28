---
title: Information Common to Type 1 and Type 2 Online Stores
description: Information Common to Type 1 and Type 2 Online Stores
ms.assetid: 20463d9a-bf10-4b68-b13d-452c788ce21b
keywords:
- Windows Media Player online stores,type 1 online stores
- online stores,type 1 online stores
- type 1 online stores,about
- Windows Media Player,type 1 online stores
- Windows Media Player online stores,type 2 online stores
- online stores,type 2 online stores
- type 2 online stores,about
- Windows Media Player,type 2 online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Information Common to Type 1 and Type 2 Online Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

Windows Media Player supports two kinds of online stores: type 1 and type 2. Type 1 stores are supported by Windows Media Player 11. Type 2 stores are supported by Windows Media Player 10 and Windows Media Player 11. Type 2 stores provide a basic level of integration with the Player's user interface, and Type 1 stores provide a deeper integration. For more information about the difference between type 1 and type 2 stores, see [Windows Media Player Online Stores](windows-media-player-online-stores.md).

The following sections provide information that applies to both type 1 and type 2 online stores.



| Section                                                                                                                | Description                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [Adding the ContentDistributor Attribute](adding-the-contentdistributor-attribute.md)                                 | Describes how to specify an attribute value that identifies content that you provided.                                        |
| [Creating the ServiceInfo Document Dynamically](creating-the-serviceinfo-document-dynamically.md)                     | Describes how to use ASP to create your ServiceInfo document.                                                                 |
| [Playing Digital Media from Online Store Web Pages](playing-digital-media-from-online-store-web-pages.md)             | Describes how to play digital media content in online store service task panes.                                               |
| [Using HTMLView with Online Stores](using-htmlview-with-online-stores.md)                                             | Describes how online store providers can bypass the dialog box that prompts users for permission to display HTMLView content. |
| [Integrating the Info Center View Feature](integrating-the-info-center-view-feature.md)                               | Describes how online stores provide the Info Center View feature.                                                             |
| [Matching the Windows Media Player Colors](matching-the-windows-media-player-colors.md)                               | Describes how to match your webpage colors to Windows Media Player colors.                                                    |
| [Using Auto Playlists to Organize Content in the Library](using-auto-playlists-to-organize-content-in-the-library.md) | Describes how online store providers can add Windows Media Player auto playlists to their named node in **Media Library**.    |
| [Detecting the Player](detecting-the-player.md)                                                                       | Describes how to determine the version of Windows Media Player in which an online store webpage is hosted.                    |
| [Setting the Initial Online Store](setting-the-initial-online-store.md)                                               | Describes the features available to specify the first online store that the user sees after installing Windows Media Player.  |
| [Co-Branding Online Stores](co-branding-online-stores.md)                                                             | Describes how computer manufacturers can co-brand with online store providers.                                                |
| [Considerations for International Markets](considerations-for-international-markets.md)                               | Discusses considerations for online stores that serve international markets.                                                  |
| [Setup Command-line Parameters for Online Stores](setup-command-line-parameters-for-online-stores.md)                 | Provides information about command-line parameters for Windows Media Player setup.                                            |
| [Exclusive Online Stores](exclusive-online-stores.md)                                                                 | Describes how to embed the Player control in an application and have only one online store available to the user.             |
| [Private Online Stores](private-online-stores.md)                                                                     | Provides information about the registry entries required for private online stores.                                           |
| [ServiceInfo Document](serviceinfo-document.md)                                                                       | Provides information about an XML document that online stores must provide.                                                   |



 

## Related topics

<dl> <dt>

[**Windows Media Player Online Stores**](windows-media-player-online-stores.md)
</dt> </dl>

 

 




