---
title: Static and Auto Playlists
description: Static and Auto Playlists
ms.assetid: 708c236e-8f3c-4188-aefb-eda7da598944
keywords:
- Windows Media Player,playlists
- Windows Media Player object model,playlists
- object model,playlists
- Windows Media Player Mobile,playlists
- Windows Media Player ActiveX control,playlists
- Windows Media Player Mobile ActiveX control,playlists
- ActiveX control,playlists
- playlists,static
- metafile playlists,static
- Windows Media metafile playlists,static
- static playlists
- auto playlists
- playlists,auto
- metafile playlists,auto
- Windows Media metafile playlists,auto
ms.topic: article
ms.date: 05/31/2018
---

# Static and Auto Playlists

There are two types of playlists:

-   Static playlists, which include specific media items
-   Auto playlists, which search the library every time they are opened and may contain different media items at different times. An auto playlist is the result of a database query.

To import a static playlist from a metafile, first call *Player*.**newPlaylist** to create a **Playlist** object based on the data in the metafile, and then pass that object to *PlaylistCollection*.**importPlaylist** to add the playlist to the library.

To import an auto playlist from a metafile, use *MediaCollection*.**add**. For more information, see [Playlists and the MediaCollection Object](playlists-and-the-mediacollection-object.md).

To import a static playlist from an auto playlist metafile, use *Player*.**newPlaylist** and *PlaylistCollection*.**importPlaylist** as described earlier. The auto playlist will be executed once and a static playlist will be created based on the result of that execution.

Using an auto playlist to query the user's library is not supported for webpages that users access over the Internet.

The following C# example code demonstrates importing an auto playlist metafile as a static playlist. To run this sample, create an auto playlist by using the library user interface, and then include the correct path to the auto playlist metafile in this code.


```C++
private void addStaticPlaylist()
{
    IWMPPlaylist pList;

    pList = Player.newPlaylist("NewImportedList", "\\\\myServer\\myPath\\artistcollection.wpl");
    if (pList.count == 0)
        MessageBox.Show("The specified playlist is empty.");
    else
        Player.playlistCollection.importPlaylist(pList);
}

```



## Related topics

<dl> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> </dl>

 

 




