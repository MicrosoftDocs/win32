---
title: About Type 1 Online Stores
description: About Type 1 Online Stores
ms.assetid: 754b0097-5d28-4c1f-9847-a19cf23beaea
keywords:
- Windows Media Player online stores,type 1 online stores
- online stores,type 1 online stores
- type 1 online stores,about
- Windows Media Player,type 1 online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Type 1 Online Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

Microsoft Windows Media Player 11 supports two kinds of online stores: type 1 and type 2. Type 1 stores are more deeply integrated into Windows Media Player than type 2 stores. A type 1 online store provides a downloadable music catalog so that Windows Media Player can make the store's content available to the user as if the content were in the user's local media library.

A type 1 online store must provide a plug-in that implements the [IWMPContentPartner](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartner) interface. As the user navigates in the Windows Media Player user interface, the Player calls the plug-in so that the online store can enhance the user's experience by providing webpages that are displayed in the Player.

Features of type 1 online stores that distinguish them from type 2 stores include the following:

-   **Ease of use.** Users can browse for music from the online store catalog using the same, familiar Windows Media Player user interface that they currently use to manage their personal library. Users can view only a single online store catalog in the Browse feature at any particular time.
-   **Convenience.** Users can sample or purchase music without switching from the Browse feature to another part of the Windows Media Player user interface.
-   **Rich features.** Because the online store catalog is stored in a fashion similar to the user's library, many of the Windows Media Player library features can be applied to the catalog. For example, users can use the Browse feature's word wheel to filter the online store catalog.

For an online store provider, the advantages of providing a type 1 store rather than a type 2 store include the following:

-   A highly visible custom node in the Windows Media Player library tree.
-   A system designed for music purchases.
-   Improved connections to Player processes.
-   A better, easier-to-use download manager.
-   The ability to navigate between various features in the Player (including opening specific library tree nodes).
-   Notifications about license expiration for subscription content.
-   Notifications for working with connected portable music players.

The following sections provide overview information about type 1 online stores.



| Section                                                                                              | Description                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Music Catalog](music-catalog.md)                                                                   | Describes the music catalog provided by the online store. Describes the catalog compiler provided by Microsoft.                                                                     |
| [Content Containers](content-containers.md)                                                         | Describes the content container interface ([IWMPContentContainer](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentcontainer)), which is used to represent a collection of media items to be purchased or downloaded. |
| [Library Integration](library-integration.md)                                                       | Describes how the online store's music catalog is integrated into the Player's library view.                                                                                        |
| [Discovery Pages](discovery-pages.md)                                                               | Describes the interaction between Windows Media Player and webpages provided by the online store.                                                                                   |
| [Context Menus](context-menus.md)                                                                   | Describes how the online store can provide context menus as the user navigates the Player's user interface.                                                                         |
| [Audio Streams](audio-streams.md)                                                                   | Describes how the online store provides Windows Media Player with the URL for streaming audio content.                                                                              |
| [ServiceInfo Document for a Type 1 Online Store](serviceinfo-document-for-a-type-1-online-store.md) | Describes the ServiceInfo XML document provided by a type 1 online store.                                                                                                           |
| [Type 1 Online Store Plug-in](type-1-online-store-plug-in.md)                                       | Describes the plug-in that a type 1 online store must provide.                                                                                                                      |



 

## Related topics

<dl> <dt>

[**Type 1 Online Stores**](type-1-online-stores.md)
</dt> </dl>

 

 




