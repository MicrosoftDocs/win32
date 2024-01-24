---
title: Location and Selected Item
description: Location and Selected Item
ms.assetid: 9556e01f-1f75-4089-9e62-b41a9aa53e93
keywords:
- Windows Media Player online stores,locations
- online stores,locations
- type 1 online stores,locations
- Windows Media Player online stores,library locations
- online stores,library locations
- type 1 online stores,library locations
- Windows Media Player online stores,selected items
- online stores,selected items
- type 1 online stores,selected items
- Windows Media Player library,locations
- Windows Media Player library,selected items
- library,locations
- library,selected items
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Location and Selected Item

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player uses the following five items to characterize its current view of online store content:

-   task
-   library location type
-   library location ID
-   selected item type
-   selected item ID

Typically, you can think of the view in Windows Media Player as a container of items. The container has a type, and an item has a type. All the items in a container have the same type. Location types and item types are both specified by the [library location constants](library-location-constants.md). For example, if the current view is showing an individual album, the library location type is CPAlbumID, and, because an album contains tracks, the selected item type is CPTrackID.

The following table shows the location and item types for several containers.



| Description of container                              | Library location type | Selected item type |
|-------------------------------------------------------|-----------------------|--------------------|
| An album that is a container of tracks                | CPAlbumID             | CPTrackID          |
| A list that is a container of tracks                  | CPListID              | CPTrackID          |
| A list that is a container of albums                  | CPListID              | CPAlbumID          |
| A radio station that is a container of lists          | CPRadioID             | CPListID           |
| The set of all albums, which is a container of albums | AllCPAlbumIDs         | CPAlbumID          |
| The set of all genres, which is a container of genres | AllCPGenreIDs         | CPGenreID          |



 

The tabs in Windows Media Player represent different tasks. The Player displays online store content in three different task panes: **Library**, **Burn**, and **Sync**. The Library task pane is also called the **Browse** task pane. Sometimes, a task pane is called a *feature*, so you might see terms like *Burn feature* and *Sync feature* in this documentation.

The following examples show how Windows Media Player uses the five pieces of information (task, library location type, library location ID, selected item type, selected Item ID) to characterize different views.

In the **Burn** task pane, the Player is displaying an album as a container of tracks. The album has an ID of 250. In the view, the selected item is the track that has an ID of 800. Note that 800 is the ID of the track in the online store's catalog, not the number of the track on the album.



| Item                  | Value     |
|-----------------------|-----------|
| task                  | Burn      |
| library location type | CPAlbumID |
| library location ID   | 250       |
| selected item type    | CPTrackID |
| selected item ID      | 800       |



 

In the **Sync** task pane, the Player is displaying the set of all albums, which is a container of albums. In the view, the selected item is the album that has an ID of 300. Note that the library location ID is not applicable to this view.



| Item                  | Value         |
|-----------------------|---------------|
| task                  | Sync          |
| library location type | AllCPAlbumIDs |
| library location ID   | N/A           |
| selected item type    | CPAlbumID     |
| selected item ID      | 300           |



 

In the tree-view control, the root node for the online store is selected. In this case, there is no container, and consequently, there are no items. The entire **Library** task pane is displaying a discovery page.



| Item                  | Value           |
|-----------------------|-----------------|
| task                  | Browse          |
| library location type | RootLocation    |
| library location ID   | N/A             |
| selected item type    | UnknownLocation |
| selected item ID      | N/A             |



 

In the **Sync** task pane, the Player is displaying the year 2002 as a container of tracks. In the view, the selected item is the track that has an ID of 450.



| Item                  | Value           |
|-----------------------|-----------------|
| task                  | Sync            |
| library location type | ReleaseDateYear |
| library location ID   | 2002            |
| selected item type    | CPTrackID       |
| selected item ID      | 450             |



 

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> <dt>

[**Discovery Pages**](discovery-pages.md)
</dt> </dl>

 

 




