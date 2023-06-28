---
title: PlaylistCollection.isDeleted method
description: The isDeleted method retrieves a value indicating whether the specified playlist is in the deleted items folder.
ms.assetid: '5023927a-5d1a-4b61-8122-476947d537c4'
keywords:
- isDeleted method Windows Media Player
- isDeleted method Windows Media Player , PlaylistCollection class
- PlaylistCollection class Windows Media Player , isDeleted method
topic_type:
- apiref
api_name:
- PlaylistCollection.isDeleted
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PlaylistCollection.isDeleted method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isDeleted** method retrieves a value indicating whether the specified playlist is in the deleted items folder.

## Syntax


```JScript
bRetVal = PlaylistCollection.isDeleted(
  playlist
)
```



## Parameters

<dl> <dt>

*playlist* \[in\]
</dt> <dd>

The **Playlist** object to be searched for.

</dd> </dl>

## Return value

This method returns a **Boolean**.

**Windows Media Player 10 Mobile**: This method always returns **false**.

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0, Windows Media Player version 7.1, or Windows Media Player for Windows XP. This method is not supported for Windows Media Player 9 Series or later.<br/> |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl>                                                                                                              |



## See also

<dl> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> </dl>

 

 





