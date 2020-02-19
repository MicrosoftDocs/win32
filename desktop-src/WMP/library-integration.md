---
title: Library Integration
description: Library Integration
ms.assetid: 6ff1b379-983b-4cd7-8142-27523a7a03e7
keywords:
- Windows Media Player online stores,library integration
- online stores,library integration
- type 1 online stores,library integration
- Windows Media Player online stores,task panes
- online stores,task panes
- type 1 online stores,task panes
- Windows Media Player,task panes
- Windows Media Player library,integrating
- library,integrating
ms.topic: article
ms.date: 05/31/2018
---

# Library Integration

The Windows Media Player user interface is organized into feature areas, called *task panes*, which encapsulate the various high-level features of the program. These include the **Library**, **Sync**, and **Burn** task panes (among others). The **Library** task pane enables users to work with the library; the **Sync** task pane enables users to synchronize digital media files to a portable device; and the **Burn** task pane enables users to burn digital media files to a CD or DVD.

> [!Note]  
> The **Library** task pane is sometimes called the **Browse** task pane.

 

Each of these task panes has some level of integration with the library. For example, if the user wants to burn music to a CD, it makes sense to let the user choose the music to burn by browsing the library and simply dragging and dropping media items into a list. This means that users can view and use an online store catalog that is fully integrated into the library when working in the **Library**, **Sync**, and **Burn** task panes. The [WMPTaskType](/previous-versions/windows/desktop/api/contentpartner/ne-contentpartner-wmptasktype) enumeration contains values that represent these three task panes so they can be identified programmatically.

Each of these three task panes is organized into three major parts. The first part is the library tree-view control. This control provides the user with a hierarchical view of the Windows Media Player library, including categorization features by song, artist, album, and so forth. The second task pane part is the details pane. This pane provides detailed information organized according to the category currently selected in the library tree-view control. For example, if the user has clicked **Songs** in the tree view, the details pane will show the song titles currently in the library, along with other information such as length and album title. The third part is the list pane, or *basket*. Users can drag and drop media items onto the basket to build lists, such as playlists, sync lists, and burn lists.

When an online store catalog is integrated with the library, the online store appears as a top-level category, or *node*, in the library tree-view control. (Only one online store catalog is visible to the user at a time.) When a user chooses to view the online store catalog by clicking the node, the details pane shows information about the music in the online store catalog. This includes music the user has purchased or rented, and also music the user has not yet acquired.

The top-level online store node has a set of child nodes provided by Windows Media Player. For example, the top-level online store node has Radio, Artist, and Album child nodes, among others. The top-level online store node can also have up to eight custom child nodes provided by the online store. Windows Media Player creates a custom child node for any list that has a list identifier in the range 0 through 7. The online store specifies the identifier of a list in the [list.csv](list-csv.md) file that is part of the store's catalog.

Windows Media Player retrieves an icon for each of the online store's custom tree nodes by calling [IWMPContentPartner::GetItemInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getiteminfo), passing CPListIDIcon in the *bstrInfoName* parameter.

As the user navigates through the catalog, Windows Media Player makes calls to **IWMPContentPartner::GetItemInfo** to retrieve metadata from the content partner plug-in about the music items the user selects. This metadata provides information to the Player so that the Player can display details about the catalog items. For example, if the user selects an album, Windows Media Player retrieves the album art URL so that the user can see the album cover art.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> </dl>

 

 




