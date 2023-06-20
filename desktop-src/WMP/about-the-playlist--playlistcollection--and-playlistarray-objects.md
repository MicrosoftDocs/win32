---
title: About the Playlist, PlaylistCollection, and PlaylistArray Objects
description: About the Playlist, PlaylistCollection, and PlaylistArray Objects
ms.assetid: 19867944-c836-4b7e-ada3-f696905e6327
keywords:
- Windows Media Player,Playlist object
- Windows Media Player object model,Playlist object
- object model,Playlist object
- Windows Media Player ActiveX control,Playlist object
- ActiveX control,Playlist object
- Windows Media Player Mobile ActiveX control,Playlist object
- Windows Media Player Mobile,Playlist object
- Playlist object
- Windows Media Player,PlaylistCollection object
- Windows Media Player object model,PlaylistCollection object
- object model,PlaylistCollection object
- Windows Media Player ActiveX control,PlaylistCollection object
- ActiveX control,PlaylistCollection object
- Windows Media Player Mobile ActiveX control,PlaylistCollection object
- Windows Media Player Mobile,PlaylistCollection object
- PlaylistCollection object
- Windows Media Player,PlaylistArray object
- Windows Media Player object model,PlaylistArray object
- object model,PlaylistArray object
- Windows Media Player ActiveX control,PlaylistArray object
- ActiveX control,PlaylistArray object
- Windows Media Player Mobile ActiveX control,PlaylistArray object
- Windows Media Player Mobile,PlaylistArray object
- PlaylistArray object
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Playlist, PlaylistCollection, and PlaylistArray Objects

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Playlist**, **PlaylistCollection**, and **PlaylistArray** objects govern the playlists that Windows Media Player can use to specify the order in which content will be played. You get the **PlaylistCollection** object from the **playlistCollection** property of the **Player** object. The **playlistCollection** property returns the **PlaylistCollection** object. You can only access the properties of the **PlaylistCollection** object after you have created it. For example, to create a new playlist, you must first get the **PlaylistCollection** object and then use a method on that object.


```C++
player.playlistcollection.newplaylist('myplaylist');
```



You can get the current playlist by using the **currentPlaylist** property. For example, to get the name of the current playlist, use the following code:


```C++
myname = player.currentplaylist.name;
```



The **PlaylistArray** object is returned by the **getAll** and **getByName** methods of the **PlaylistCollection** object. To get the number of playlists, for example, use the following code:


```C++
howmany = player.playlistcollection.getAll().count;
```



To retrieve a known playlist by name, use the following code:


```C++
if (player.playlistcollection.getbyname('myplaylist').count == 1) {
    pl = player.playlistcollection.getbyname('myplaylist').item(0);
}
```



## Related topics

<dl> <dt>

[**Player Object Model for Scripting Languages**](player-object-model-for-scripting-languages.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**PlaylistArray Object**](playlistarray-object.md)
</dt> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> </dl>

 

 




