---
title: Media.isMemberOf method
description: The isMemberOf method returns a value indicating whether the media item is a member of the specified playlist.
ms.assetid: 'e620741f-6807-4a61-ba9b-f45426d6e33e'
keywords:
- isMemberOf method Windows Media Player
- isMemberOf method Windows Media Player , Media class
- Media class Windows Media Player , isMemberOf method
topic_type:
- apiref
api_name:
- Media.isMemberOf
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media.isMemberOf method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isMemberOf** method returns a value indicating whether the media item is a member of the specified playlist.

## Syntax


```JScript
bRetVal = Media.isMemberOf(
  playlist
)
```



## Parameters

<dl> <dt>

*playlist* \[in\]
</dt> <dd>

**Playlist** object that might contain the media item.

</dd> </dl>

## Return value

This method returns a **Boolean**.

## Remarks

This method is cannot check playlists retrieved through the **MediaCollection** object. To test whether a media item is a member of a particular named playlist, retrieve the playlist with *player*.*playlistCollection*.**getByName**(*name*).**item**(0). This method can also be used with CD playlists and metafile playlists.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example uses *Media*.**isMemberOf** to test whether the current media item is a member of the playlist named Sample Playlist. If it is not, the current media item is appended to the sample playlist. The **Player** object was created with ID = "Player".


```JScript
// Store the playlist object named Sample Playlist.
var sPlaylist = Player.playlistcollection.getbyname("Sample Playlist").item(0);

// Test whether the current media item is a member of Sample Playlist.
 var answer = ((Player.currentMedia.isMemberOf(sPlaylist))?"Yes":"No");

// If the current media item is not a member of Sample Playlist,
// append the current media item to the playlist.
if (answer == "No"){
   sPlaylist.appendItem(Player.currentMedia);
}

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Media Object**](media-object.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





