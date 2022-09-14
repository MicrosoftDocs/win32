---
title: Playlists and the PlaylistCollection Object
description: Playlists and the PlaylistCollection Object
ms.assetid: 63c8955b-34ad-447b-b734-657207bcecbb
keywords:
- Windows Media Player,playlists
- Windows Media Player object model,playlists
- object model,playlists
- Windows Media Player Mobile,playlists
- Windows Media Player ActiveX control,playlists
- Windows Media Player Mobile ActiveX control,playlists
- ActiveX control,playlists
- playlists,PlaylistCollection object
- metafile playlists,PlaylistCollection object
- Windows Media metafile playlists,PlaylistCollection object
- PlaylistCollection object
ms.topic: article
ms.date: 05/31/2018
---

# Playlists and the PlaylistCollection Object

The **PlaylistCollection** object gives you access to playlists in the library and has methods for creating new, empty playlists and new playlists from metafiles.

## Working with Existing Playlists

The *PlaylistCollection*.**getAll** and *PlaylistCollection*.**getByName** methods each return a **PlaylistArray** object, which can contain multiple playlists.

The *PlaylistCollection*.**getAll** method returns all of the existing playlists that are in the library. For example, you can call this method and then retrieve the playlists in the **PlaylistArray** object to determine whether a given playlist name has already been used, or to display all of the playlists to the user. The sample code in [Playlist Attributes](playlist-attributes.md) uses the **getAll** method.

The *PlaylistCollection*.**getByName** method returns all of the playlists with a given name. You can use this method to handle each of those playlists separately.

You can also use the **getByName** method to retrieve a unique playlist by name. In that case, the **PlaylistArray** object has only one element. The following C# example demonstrates this technique.


```C++
IWMPPlaylistArray PlayListArray;
IWMPPlaylist Playlist;
// Store the playlist named "BluesTest" in the array
PlayListArray = Player.playlistCollection.getByName("BluesTest");
// Retrieve the first playlist in the collection.
Playlist = PlaylistArray.Item(0);

```



## Working with New Playlists

You can use the *PlaylistCollection*.**newPlaylist** method to create a new, empty playlist. The method returns a reference to the new **Playlist** object. You can then call the *Playlist*.**appendItem** method to add media items to the playlist.

You can also create a new playlist based on a playlist metafile. First, pass the name of the playlist and the path to the metafile to the *Player*.**newPlaylist** method. That method returns a reference to the new **Playlist** object. Then, pass the new **Playlist** object to the *PlaylistCollection*.**importPlaylist** method to add it to the library.

Notice the difference between the *PlaylistCollection*.**newPlaylist** method and the *Player*.**newPlaylist** method. The **PlaylistCollection** method creates a new, empty playlist and adds it to the library. The **Player** method creates a new, populated **Playlist** object but does not add it to the library.

Throughout this topic, the **Player** object was defined in the following manner:


```C++
AxWMPLib.AxWindowsMediaPlayer Player;
using WMPLib;

```



The following C# example demonstrates importing a playlist from a metafile. The *strPListName* argument specifies the name of the new playlist. The *strMetaFileName* specifies the name of the metafile from which the playlist is imported.


```C++
private IWMPPlaylist importPlaylist(string strPlaylistName, string strMetaFileName)
{
    IWMPPlaylist  NewPlaylist;
    IWMPPlaylist  ImportPlaylist;

    NewPlaylist = Player.newPlaylist(strPlaylistName, strMetaFileName);
    ImportPlaylist = Player.playlistCollection.importPlaylist(NewPlaylist);

    return ImportPlaylist;
}

```



## Related topics

<dl> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> <dt>

[**Player.newPlaylist**](player-newplaylist.md)
</dt> <dt>

[**Playlist.appendItem**](playlist-appenditem.md)
</dt> <dt>

[**PlaylistArray Object**](playlistarray-object.md)
</dt> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> <dt>

[**Playlists and Media Items**](playlists-and-media-items.md)
</dt> </dl>

 

 




