---
title: PlaylistCollection.setDeleted method
description: The setDeleted method moves a playlist to the deleted items folder.
ms.assetid: c41f7e89-11c8-4d55-91eb-a89e6f39e56b
keywords:
- setDeleted method Windows Media Player
- setDeleted method Windows Media Player , PlaylistCollection class
- PlaylistCollection class Windows Media Player , setDeleted method
topic_type:
- apiref
api_name:
- PlaylistCollection.setDeleted
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlaylistCollection.setDeleted method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **setDeleted** method moves a playlist to the deleted items folder.

## Syntax


```JScript
PlaylistCollection.setDeleted(
  playlist,
  true
)
```



## Parameters

<dl> <dt>

*playlist* \[in\]
</dt> <dd>

The **Playlist** object to be moved.

</dd> <dt>

*true* \[in\]
</dt> <dd>

Always specify this value.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

**Windows Media Player 10 Mobile**: This method is not supported.

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0, Windows Media Player version 7.1, or Windows Media Player for Windows XP. This method is not supported for Windows Media Player 9 Series or later.<br/> |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl>                                                                                                              |



## See also

<dl> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> </dl>

 

 





