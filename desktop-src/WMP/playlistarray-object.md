---
title: PlaylistArray Object
description: The PlaylistArray object provides a way to access playlists by index number.
ms.assetid: 8a29f36c-9c7c-4bc7-9adb-b34cc4231d81
keywords:
- PlaylistArray Object Windows Media Player
topic_type:
- apiref
api_name:
- PlaylistArray Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# PlaylistArray Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PlaylistArray** object provides a way to access playlists by index number.

The **PlaylistArray** object supports the following property.



| Property                         | Description                                              |
|----------------------------------|----------------------------------------------------------|
| [count](playlistarray-count.md) | Retrieves the number of playlists in the playlist array. |



 

The **PlaylistArray** object supports the following method.



| Method                         | Description                                                              |
|--------------------------------|--------------------------------------------------------------------------|
| [item](playlistarray-item.md) | Retrieves the [Playlist](playlist-object.md) object at the given index. |



 

The **PlaylistArray** object is accessed through the following methods.



| Object                                              | Method                                                                                 |
|-----------------------------------------------------|----------------------------------------------------------------------------------------|
| [PlaylistCollection](playlistcollection-object.md) | [getAll](playlistcollection-getall.md), [getByName](playlistcollection-getbyname.md) |



 

For purposes of illustration, *player*.*playlistCollection*.**getAll** is used in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




