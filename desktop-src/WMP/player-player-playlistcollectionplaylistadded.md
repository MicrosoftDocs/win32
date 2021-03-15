---
title: Player.PlaylistCollectionPlaylistAdded event
description: The PlaylistCollectionPlaylistAdded event occurs when a playlist is added to the playlist collection. | Player.PlaylistCollectionPlaylistAdded event
ms.assetid: 07acb5e6-d832-4f0b-a6bb-2b7ba27c368d
keywords:
- PlaylistCollectionPlaylistAdded event Windows Media Player
- PlaylistCollectionPlaylistAdded event Windows Media Player , Player class
- Player class Windows Media Player , PlaylistCollectionPlaylistAdded event
topic_type:
- apiref
api_name:
- Player.PlaylistCollectionPlaylistAdded
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.PlaylistCollectionPlaylistAdded event

The **PlaylistCollectionPlaylistAdded** event occurs when a playlist is added to the playlist collection.

## Syntax


```JScript
Player.PlaylistCollectionPlaylistAdded(
  bstrPlaylistName
)
```



## Parameters

<dl> <dt>

*bstrPlaylistName* 
</dt> <dd>

**String** specifying the name of the playlist that was added.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The name of the playlist that was added can be used to retrieve the corresponding **Playlist** object using the *PlaylistCollection*.**getByName** method.

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

 

 





