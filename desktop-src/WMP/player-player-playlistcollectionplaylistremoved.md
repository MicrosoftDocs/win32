---
title: Player.PlaylistCollectionPlaylistRemoved event
description: The PlaylistCollectionPlaylistRemoved event occurs when a playlist is removed from the playlist collection. | Player.PlaylistCollectionPlaylistRemoved event
ms.assetid: 2405be98-b4c2-4b4e-bea6-0c48a3e26f18
keywords:
- PlaylistCollectionPlaylistRemoved event Windows Media Player
- PlaylistCollectionPlaylistRemoved event Windows Media Player , Player class
- Player class Windows Media Player , PlaylistCollectionPlaylistRemoved event
topic_type:
- apiref
api_name:
- Player.PlaylistCollectionPlaylistRemoved
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.PlaylistCollectionPlaylistRemoved event

The **PlaylistCollectionPlaylistRemoved** event occurs when a playlist is removed from the playlist collection.

## Syntax


```JScript
Player.PlaylistCollectionPlaylistRemoved(
  bstrPlaylistName
)
```



## Parameters

<dl> <dt>

*bstrPlaylistName* 
</dt> <dd>

**String** specifying the name of the playlist that was removed.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**PlaylistCollection.getByName**](playlistcollection-getbyname.md)
</dt> </dl>

 

 





