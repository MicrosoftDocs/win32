---
title: PlaylistCollection.remove method
description: The remove method removes a playlist from the library. | PlaylistCollection.remove method
ms.assetid: '3327ba59-5f46-4df0-ba95-c338b019277d'
keywords:
- remove method Windows Media Player
- remove method Windows Media Player , PlaylistCollection class
- PlaylistCollection class Windows Media Player , remove method
topic_type:
- apiref
api_name:
- PlaylistCollection.remove
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlaylistCollection.remove method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **remove** method removes a playlist from the library.

## Syntax


```JScript
PlaylistCollection.remove(
  playlist
)
```



## Parameters

<dl> <dt>

*playlist* \[in\]
</dt> <dd>

The **Playlist** object to be removed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> <dt>

[**PlaylistCollection.importPlaylist**](playlistcollection-importplaylist.md)
</dt> <dt>

[**PlaylistCollection.newPlaylist**](playlistcollection-newplaylist.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





