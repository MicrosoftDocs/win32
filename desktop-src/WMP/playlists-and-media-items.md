---
title: Playlists and Media Items
description: Playlists and Media Items
ms.assetid: 281c744d-380e-4200-8585-a3f378bc1c36
keywords:
- Windows Media Player,playlists
- Windows Media Player object model,playlists
- object model,playlists
- Windows Media Player Mobile,playlists
- Windows Media Player ActiveX control,playlists
- Windows Media Player Mobile ActiveX control,playlists
- ActiveX control,playlists
- playlists,media items
- metafile playlists,media items
- Windows Media metafile playlists,media items
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Playlists and Media Items

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A playlist is a set of media items. A **Playlist** object can manipulate the **Media** objects that represent those items.

## Retrieving Media Items

For an existing playlist, you can read the *Playlist*.**count** property to determine how many media items are in the playlist, and you can get a reference to the **Media** object corresponding to a specific item using the *Playlist*.**item** property.

The following C# example retrieves an object reference to a specific media item. (Throughout this topic, the variable *pList* is a reference to a **Playlist** object.)


```C++
currMedia = pList.Item(0);

```



The following C# example retrieves the names of all the media items in a playlist and puts them in a ListBox named lstOutput.


```C++
for (j=0; j < pList.count; j++)
{
    strItemName = pList.get_Item(j).name;
    lstOutput.Items.Add(strItemName);
}

```



## Adding Items to a Playlist

You can add a media item to the end of a playlist or at a specific position in a playlist, using the *Playlist*.**appendItem** and *Playlist*.**insertItem** methods.

Throughout this topic, the **Player** object was defined in the following manner:


```C++
AxWMPLib.AxWindowsMediaPlayer Player;
using WMPLib;

```



The following C# example demonstrates both techniques by adding the current media item to a playlist named "BluesTest", first at the end and then at the beginning of the playlist.


```C++
IWMPPlaylistCollection pListColl;
IWMPPlaylistArray pListArray;
IWMPPlaylist pList;

// Initialize the Media object
IWMPMedia currMedia = Player.currentMedia;

if(currMedia != null)
{
    // Retrieve the playlist collection
    pListColl = Player.playlistCollection;

    // Retrieve a playlist array containing
    // playlists named BluesTest
    pListArray = pListColl.getByName("BluesTest");

    // Retrieve the first element with this name from the
    // array.
    pList = pListArray.Item(0);

    // Add the current item to the end, and then, the beginning
    // of the specified playlist.
    pList.appendItem(currMedia);
    pList.insertItem(0, currMedia);
}

```



When you create a new, empty playlist by using the *PlaylistCollection*.**newPlaylist** method, you can add media items to it by repeatedly calling the *Playlist*.**appendItem** method.

## Manipulating Media Items in a Playlist

You can change the position of a media item in the playlist by using the *Playlist*.**moveItem** method. You specify the item by its current index, and then you specify the new index. The following C# example moves an item from index 5 to index 0 within a playlist.


```C++
// Move the 6th item to the beginning
// of the specified playlist.
pList.moveItem(5, 0);

```



You can remove a media item from the playlist by using the **Playlist**.**removeItem** method. Note that if the removed item was not the final item in the playlist, the index values of the subsequent items change. The following C# example removes the specified item.


```C++
// Remove the currently playing item from the
// specified playlist.
pList.removeItem(currMedia);

```



> [!Note]  
> Users can change the contents of a playlist outside of your application. Whenever you manipulate the items in a playlist, you should monitor and handle the playlist-related events of the Windows Media Player control to ensure that your code works correctly. These events are *Player*.**CurrentPlaylistChange** and *Player*.**PlaylistChange**.

 

## Related topics

<dl> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> </dl>

 

 




